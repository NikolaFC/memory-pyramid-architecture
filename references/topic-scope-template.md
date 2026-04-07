# Topic `_scope.md` Template

> 用途：为每个正式专题定义边界（管什么 / 不管什么），给 LLM 路由提供稳定依据。

---

## 1) 通用模板

```yaml
---
topic: <topic-slug>
name: <专题名称>
status: active | candidate | paused | archived
owner: main
last_updated: YYYY-MM-DD
aliases:
  - <别名1>
  - <别名2>
includes:
  - <属于本专题的内容1>
  - <属于本专题的内容2>
excludes:
  - <不属于本专题的内容1>
  - <不属于本专题的内容2>
primary_questions:
  - <本专题核心要回答的问题1>
  - <本专题核心要回答的问题2>
related_topics:
  - <related-topic-1>
  - <related-topic-2>
routing_hints:
  when_to_append_existing:
    - <条件1>
    - <条件2>
  when_to_create_subtopic:
    - <条件1>
  when_to_link_only:
    - <条件1>
promotion_rules:
  min_repeated_sessions: 2
  min_independent_questions: 2
  require_lint_pass: true
---
```

---

## 2) 推荐正文结构

```markdown
# <专题名称>

## Scope Summary
一句话定义本专题职责。

## In Scope
- ...

## Out of Scope
- ...

## Canonical Pages
- [页面A](./pages/a.md)
- [页面B](./pages/b.md)

## Open Questions
- ...

## Change Log
- YYYY-MM-DD: 初始创建
```

---

## 3) 示例：`finance/_scope.md`

```yaml
---
topic: finance
name: Finance
status: active
owner: main
last_updated: 2026-04-05
aliases: [markets, investing, trading]
includes:
  - 资产价格行为与市场结构
  - 宏观变量对市场的传导
  - 风险管理与仓位管理
excludes:
  - 纯地区政治史（无市场映射）
  - 纯外交议程细节（无资产影响）
primary_questions:
  - 这件事如何影响股市/期货/加密资产？
  - 对仓位、节奏、风险敞口有什么影响？
related_topics: [macro, geopolitics, policy]
routing_hints:
  when_to_append_existing:
    - 讨论核心是“市场影响/资产定价”
  when_to_create_subtopic:
    - 出现稳定可复用分支（如 geopolitical-market-impact）
  when_to_link_only:
    - 讨论核心是地缘机制本身而非市场影响
promotion_rules:
  min_repeated_sessions: 2
  min_independent_questions: 2
  require_lint_pass: true
---
```

---

## 4) 使用建议

1. 每个正式专题都应有 `_scope.md`
2. 路由前先读 primary topic 的 `_scope.md`
3. `_scope.md` 变更后，需在变更日志写明原因
4. 遇到跨域争议时，优先用 `related_topics + link-only`，不要强行并库
