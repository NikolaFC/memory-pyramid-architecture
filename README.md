# Memory Pyramid Architecture for OpenClaw

**Version: 1.1.0**
**Last updated: 2026-05-07**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-blue.svg)](https://openclaw.ai)

> 🏗️ A production-ready, four-layer memory baseline for OpenClaw with night-owl-aware session boundaries.

This repository documents the **portable baseline**. Real OpenClaw production environments may add a small production overlay: live status files, indexed session transcripts, short-term promotion/dreaming pipelines, KB gardening, and skill/evolver boundaries. Those extensions should be documented as overlays, not as an incompatible “v2 rewrite”.

## ✨ Features

- 🏗️ **Four-layer design**: Raw → Structured → Knowledge → Navigation
- 🌙 **Night-owl friendly**: 22:00-07:00 activity belongs to the previous night
- 🔄 **Cron-driven pipeline**: 4 core schedules, with optional maintenance jobs
- 📊 **Search integrated**: memory files and session transcripts can be indexed for retrieval
- ⚡ **Token efficient**: prefer distilled layers before falling back to raw transcripts
- 🧩 **Overlay friendly**: add production-only memory jobs without changing the baseline contract

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/<owner>/memory-pyramid-architecture.git
cd memory-pyramid-architecture

# Initialize or verify the baseline files
python3 scripts/init.py

# Optional smoke test
python3 scripts/test_integration.py
```

Then add or verify the OpenClaw cron jobs described in `scripts/config.json` and `references/cron-reference.md`.

## 📁 Repository Structure

```text
memory-pyramid-architecture/
├── README.md / README_EN.md / README_ZH.md / README_LOCAL.md
├── VERSION
├── CHANGELOG.md
├── SKILL.md
├── PACKAGE.md
├── scripts/
│   ├── init.py                # setup / verification helper
│   ├── config.json            # baseline layers and cron schedules
│   ├── test_integration.py    # smoke test
│   └── visualize.py           # flow diagram helper
├── references/
│   ├── architecture-details.md
│   ├── cron-reference.md
│   ├── production-overlay.md
│   ├── kb-gardener-workflow-v0.1.md
│   ├── topic-routing-policy-v0.1.md
│   ├── topic-scope-template.md
│   └── troubleshooting.md
└── examples/
    ├── README.md
    ├── layer4-raw/
    ├── layer3-structured/
    └── layer2-knowledge/
```

## 🏗️ Architecture Overview

```text
Layer 1: Navigation
└── MEMORY.md

Layer 2: Knowledge
├── memory/topics/            long-term thematic truth
├── memory/daily_reviews/     daily distilled insights
└── memory/weekly_distills/   weekly pattern distillation

Layer 3: Structured logs
├── memory/YYYY-MM-DD.md
└── memory/YYYY-MM-DD-last-night.md

Layer 4: Raw sources
├── OpenClaw session transcripts / session index  preferred in current OpenClaw
└── memory/realtime-YYYY-MM-DD.md                 optional legacy/raw mirror
```

## ⏰ Core Automation Schedule

| Schedule | Job | Output |
|----------|-----|--------|
| `0 7 * * *` | Late Hour Sync | `memory/YYYY-MM-DD-last-night.md` |
| `0 10,13,16,19,22 * * *` | Micro-Sync | `memory/YYYY-MM-DD.md` |
| `10 22 * * *` | Daily Review | `memory/daily_reviews/YYYY-MM-DD.md` |
| `55 23 * * 0` | Weekly Compound | `memory/weekly_distills/YYYY-Wxx.md` |

Optional production jobs, such as search-index health checks or short-term promotion/dreaming jobs, are overlays. See [production-overlay.md](references/production-overlay.md).

## 🔍 Validation

Generic checks:

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "memory pyramid"
```

If your environment still uses a standalone QMD CLI, you can also run:

```bash
qmd list
```

## 📚 Documentation

- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[VERSION](VERSION)** - Current release version
- **[SKILL.md](SKILL.md)** - Skill usage and setup guide
- **[references/architecture-details.md](references/architecture-details.md)** - Design deep dive
- **[references/cron-reference.md](references/cron-reference.md)** - Core and optional cron guidance
- **[references/production-overlay.md](references/production-overlay.md)** - Safe production extensions and privacy boundaries
- **[references/troubleshooting.md](references/troubleshooting.md)** - Common issues and fixes

## 🌟 Why Night-Owl Optimized?

Traditional systems split activities at midnight, cutting a work session in half:

```text
22:00 - Start deep work
02:00 - Important insight
07:00 - Continue the same context
```

Memory Pyramid preserves the flow:

```text
22:00-07:00 → YYYY-MM-DD-last-night.md
```

## 🤝 Contributing

Contributions welcome:

1. Fork the repository
2. Create a feature branch
3. Update docs and examples together
4. Avoid committing private deployment identifiers, tokens, user IDs, channel IDs, or host-specific paths
5. Submit a pull request

## 🙏 Credits

- **Concept**: Inspired by [OpenViking](https://github.com/volcengine/OpenViking)
- **Design**: Satoshi & Duoduo
- **Community**: OpenClaw users

## 📄 License

[MIT](LICENSE) - Free for personal and commercial use within the OpenClaw ecosystem.

## 🔗 Links

- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenViking Repository](https://github.com/volcengine/OpenViking)
- [Issues](../../issues)

---

Made with 💕 by Satoshi & Duoduo
