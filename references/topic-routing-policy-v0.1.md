# Topic Routing Policy v0.1

> 目标：让 LLM 在维护本地知识库时，稳定判断“补充已有专题 / 新建候选专题 / 建立跨专题链接”，避免一刀切分类导致知识污染。

---

## 1. 设计原则

1. **先路由，后定稿**：允许不确定，先进入候选区。
2. **主归属 + 相关链接**：一个知识单元可以有一个 primary topic，同时关联多个 related topics。
3. **可回滚**：任何路由都可在 lint 阶段被改判。
4. **避免冲动建库**：新 topic 先 candidate，再按阈值晋升。
5. **职责分离**：
   - `memory/*` 负责时间记忆与执行基线
   - `docs/kb/*` 负责稳定知识
   - `kb_workbench/*` 负责施工与试验

---

## 2. 路由输出（四态）

每个新知识单元（source chunk）必须输出以下四类之一：

### A) `append-existing`
补充已有专题。

适用条件（建议满足 ≥2 条）：
- 与已有专题主问题高度一致
- 术语/实体重合度高
- 使用场景一致（检索时用户会在同一专题下找）

### B) `append-subtopic`
作为已有专题的子页/子视角。

适用条件：
- 与父专题强相关，但信息层级更窄
- 已有专题中反复出现该子领域
- 独立成页可提升可读性

### C) `new-candidate-topic`
创建候选专题（非正式）。

适用条件：
- 主题具独立性，但证据不足以立即升为正式专题
- 与多个专题有交叉，暂时难以确定归属
- 当前置信度不足

### D) `link-only`
不并入/不新建，只做跨专题链接。

适用条件：
- 与已有专题相关但不属于其核心范围
- 主要价值在“影响关系”而非“内容并库”

---

## 3. 决策因子（打分参考）

对每条新知识，按 0-2 分评估：

- **Scope Fit（范围匹配）**：是否符合专题 `_scope.md` 的 includes/excludes
- **Intent Match（问题意图匹配）**：用户真正想解决的问题属于哪个专题
- **Entity Overlap（实体重合）**：关键实体/术语与专题重合程度
- **Retrieval Expectation（检索预期）**：未来检索时用户会去哪里找
- **Operational Relevance（执行相关性）**：是否会改变当前策略或决策

建议阈值：
- 高置信（总分 ≥7）：可 `append-existing` 或 `append-subtopic`
- 中置信（总分 4-6）：`new-candidate-topic`
- 低置信（总分 ≤3）：`link-only` + `open_questions`

---

## 4. Candidate → 正式专题的晋升阈值

`new-candidate-topic` 满足任一条件可提请晋升：

1. 在 **≥2 个 session/thread** 被重复讨论
2. 能支持 **≥2 个独立核心问题**
3. 与现有专题发生 **重复 scope 冲突**
4. compile 后内容达到“可独立检索价值”
5. 有明确长期维护需求（非一次性热点）

> 注意：满足阈值 ≠ 自动晋升；仍需 lint 通过并由 Main 执行 promote。

---

## 5. 权限边界（默认）

- **Main**：唯一可执行 `promote` 到 `docs/kb/*`、`memory/topics/*`、`memory/SHARED_MEMORY.md`
- **Thread / Subagent**：仅可写 `memory/kb_workbench/*`（raw/compiled/lint/open_questions）
- **禁止**：未 lint 的结论直接写入 canonical memory

---

## 6. Finance × Geopolitics 路由示例

### 示例输入
“地缘政治冲突如何影响股市、商品期货和加密资产？”

### 建议路由
- primary: `finance`（因为核心问题是市场影响）
- related: `geopolitics`, `macro`
- output: `append-subtopic` → `finance/geopolitical-market-impact`

### 另一个输入
“某地区制裁体系的政治演化路径是什么？”

### 建议路由
- primary: `geopolitics`
- related: `finance`（仅作为影响路径）
- output: `link-only`（若 finance 仅受影响，不做并库）

---

## 7. 最小执行要求（MVP）

每次 route 至少写出：

```yaml
routing:
  decision: append-existing | append-subtopic | new-candidate-topic | link-only
  primary_topic: <slug>
  related_topics: [<slug1>, <slug2>]
  confidence: high | medium | low
  reason: <1-3条简述>
  next_action: compile | add-open-question | lint | promote-request
```

---

## 8. 与 Memory Pyramid 的关系

本策略**不替代**记忆金字塔；只补“专题知识运营”能力：
- 金字塔：时间记忆压缩与检索
- Topic Routing：专题知识归属与演化
- 两者共同形成“记忆 + 知识库”的闭环
