# KB Gardener Workflow v0.1

> 目标：把“被动检索”升级为“主动维护”，让本地知识库持续变好。

---

## 1. 角色定义

- **Memory Pyramid（现有）**：管理时间记忆（realtime → structured → knowledge）
- **KB Gardener（新增）**：管理专题知识生命周期（ingest → route → compile → enrich → lint → promote）

两者关系：
- 金字塔负责“记住我们做过什么”
- Gardener 负责“把值得长期复用的知识沉淀到 KB”

---

## 2. 目录约定

### 2.1 工作台（可脏，可草稿）

`memory/kb_workbench/<topic-slug>/`

建议结构：

```text
memory/kb_workbench/<topic-slug>/
├── raw/
│   └── YYYY-MM-DD-<source>.md
├── compiled/
│   └── YYYY-MM-DD-<note>.md
├── lint/
│   └── YYYY-MM-DD-report.md
├── open_questions.md
└── routing.md
```

### 2.2 正式库（canonical）

`docs/kb/<topic-slug>/`

建议结构：

```text
docs/kb/<topic-slug>/
├── _scope.md
├── index.md
└── pages/
    ├── <page1>.md
    └── <page2>.md
```

---

## 3. 六步流水线

## Step 1: Ingest

触发来源：
- 新链接/文章/PDF/repo
- 同主题连续讨论
- 用户显式要求“整理成 KB”

输出：`raw/*`

---

## Step 2: Route

按照 `Topic Routing Policy v0.1` 产出四态之一：
- append-existing
- append-subtopic
- new-candidate-topic
- link-only

输出：`routing.md` 更新一条记录（含置信度与理由）

---

## Step 3: Compile

把 raw 信息整理为结构化笔记：
- 核心结论
- 依据来源
- 与已有知识差异
- 待验证点

输出：`compiled/*`

---

## Step 4: Enrich

补充知识图谱连接：
- backlinks
- related topics
- 术语映射
- open questions

输出：更新 `compiled/*` 与 `open_questions.md`

---

## Step 5: Lint

检查五类质量门：
1. **Source**：来源是否可追溯
2. **Novelty**：是否只是旧内容重复
3. **Consistency**：与现有 canonical 内容是否冲突
4. **Scope Fit**：是否违反 `_scope.md`
5. **Freshness**：是否已过时或时效不明

输出：`lint/*`（通过/拒绝 + 原因 + 建议动作）

---

## Step 6: Promote

仅当 lint 通过，才允许升入正式层：
- `docs/kb/*`（专题正式内容）
- `memory/topics/*`（长期主题记忆，按需）
- `memory/SHARED_MEMORY.md`（仅执行基线相关）

权限：默认仅 Main 可 promote。

---

## 4. 自动触发器（建议）

| 触发器 | 动作 |
|---|---|
| 新来源进入（link/pdf/repo） | ingest |
| 同话题 2+ 次讨论 | route + compile |
| 用户说“整理成KB/形成方案” | compile + enrich |
| compile 完成 | lint |
| 话题被重新打开 | re-lint + refresh |
| 结论要进 canonical | promote-request |

---

## 5. 最小治理规则（MVP）

1. 未 lint 内容禁止直接进入 `docs/kb/*`
2. `SHARED_MEMORY.md` 只写执行基线，不写专题长文
3. 遇到跨域冲突优先 `link-only`，避免强并库
4. 路由置信度为 medium/low 时必须进入 candidate 流程
5. 每次 promote 必须写明：来源、差异、回滚路径

---

## 6. 与现有系统兼容性

- 不改动现有记忆金字塔 cron
- 不替换 `docs/`，仅补充“工作台 + 质量门 + 晋升流程”
- 可渐进上线：先从单专题试点（例如 `karpathy-llm-kb`）

---

## 7. 试点建议（Karpathy 话题）

第一阶段只做：
1. 建立 `memory/kb_workbench/karpathy-llm-kb/`
2. 写 1 篇 compile 笔记
3. 跑 1 次 lint 报告
4. 通过后再 promote 到 `docs/kb/karpathy-llm-kb/`

通过标准：
- 路由稳定（重复运行结果一致）
- lint 可发现真实问题而非形式化打勾
- promote 内容可被后续跨 session 检索并复用
