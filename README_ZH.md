# OpenClaw 记忆金字塔架构

**当前版本：1.1.0**
**最后更新：2026-05-07**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-blue.svg)](https://openclaw.ai)

> 🏗️ 为 OpenClaw 打造的四层记忆基线架构，针对夜猫子工作流优化。

本仓库记录的是**可公开复用的基线**。真实生产环境可以在其上增加 live status、session transcript 索引、短期记忆晋升、dreaming、KB Gardener、skill/evolver 边界等能力；这些应称为 **production overlay（生产叠加层）**，不是不兼容的“2.0 重写版”。

## ✨ 特性

- 🏗️ **四层金字塔**：原始来源 → 结构化日志 → 知识沉淀 → 导航索引
- 🌙 **夜猫子友好**：22:00-07:00 活动归属前一晚
- 🔄 **核心自动化**：Late Hour Sync → Micro-Sync → Daily Review → Weekly Compound
- 📊 **检索友好**：memory 文件与 session transcript 可进入 OpenClaw memory index / QMD
- ⚡ **低 token 成本**：优先读复盘和专题层，必要时再展开原始会话
- 🧩 **可叠加生产能力**：生产私有扩展不污染公开基线

## 🚀 快速开始

```bash
git clone https://github.com/<owner>/memory-pyramid-architecture.git
cd memory-pyramid-architecture
python3 scripts/init.py
python3 scripts/verify_suite.py
python3 scripts/hygiene_scan.py
python3 scripts/sync_drift_check.py
```

随后在 OpenClaw 环境中确认 cron 与 memory index 状态。

## 🏗️ 架构概览

```text
Layer 1: Navigation 导航层
└── MEMORY.md

Layer 2: Knowledge 知识层
├── memory/topics/            长期专题真相
├── memory/daily_reviews/     每日复盘
└── memory/weekly_distills/   每周蒸馏

Layer 3: Structured Logs 结构化日志层
├── memory/YYYY-MM-DD.md
└── memory/YYYY-MM-DD-last-night.md

Layer 4: Raw Sources 原始来源层
├── OpenClaw session transcripts / memory index  当前 OpenClaw 推荐主来源
└── memory/realtime-YYYY-MM-DD.md                可选 legacy/raw mirror
```

## ⏰ 核心自动化节奏

| Schedule | 任务 | 输出 |
|----------|------|------|
| `0 7 * * *` | Late Hour Sync | `memory/YYYY-MM-DD-last-night.md` |
| `0 10,13,16,19,22 * * *` | Micro-Sync | `memory/YYYY-MM-DD.md` |
| `10 22 * * *` | Daily Review | `memory/daily_reviews/YYYY-MM-DD.md` |
| `55 23 * * 0` | Weekly Compound | `memory/weekly_distills/YYYY-Wxx.md` |

健康检查、短期记忆晋升、dreaming 等属于生产叠加层，见 [production-overlay.md](references/production-overlay.md)。

## 🔍 验收

仓库检查：

```bash
python3 scripts/verify_suite.py
python3 scripts/hygiene_scan.py
python3 scripts/sync_drift_check.py
python3 scripts/test_integration.py
```

部署检查：

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "memory pyramid"
```

如果部署仍使用独立 QMD CLI，也可以运行：

```bash
qmd list
```

## 📚 文档

- [CHANGELOG.md](CHANGELOG.md)：版本历史
- [VERSION](VERSION)：当前发布版本
- [SKILL.md](SKILL.md)：使用与接入说明
- [references/architecture-details.md](references/architecture-details.md)：架构详解
- [references/cron-reference.md](references/cron-reference.md)：cron 参考
- [references/production-overlay.md](references/production-overlay.md)：生产叠加层与隐私边界
- [references/troubleshooting.md](references/troubleshooting.md)：故障排除

## 🤝 贡献

欢迎提交改进。公开文档中请避免提交私有部署标识、token、用户 ID、频道 ID、绝对主机路径或其它可回溯个人环境的信息。

## 📄 许可证

MIT License - 查看 [LICENSE](LICENSE)。

---

**维护者**：Satoshi & Duoduo
**语言**：English | 中文
