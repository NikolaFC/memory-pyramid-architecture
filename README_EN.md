# Memory Pyramid Architecture for OpenClaw

**Version: 1.1.0**
**Last updated: 2026-05-07**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](VERSION)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-blue.svg)](https://openclaw.ai)

> 🏗️ A production-ready, four-layer memory baseline for OpenClaw with night-owl-aware session boundaries.

This repository is the portable baseline. A local production deployment may add live status, session transcript indexing, short-term memory promotion, dreaming, KB gardening, or skill/evolver governance as **overlays**.

## ✨ Features

- 🏗️ **Four-layer pyramid**: Raw → Structured → Knowledge → Navigation
- 🌙 **Night-owl friendly**: 22:00-07:00 activity belongs to the previous night
- 🔄 **Automated core workflow**: Late Hour Sync → Micro-Sync → Daily Review → Weekly Compound
- 📊 **Search integrated**: memory files and session transcripts can be indexed for retrieval
- ⚡ **Token efficient**: retrieve distilled layers first; expand to raw sources only when necessary
- 🧩 **Production-overlay friendly**: extend safely without changing the baseline contract

## 🚀 Quick Start

```bash
git clone https://github.com/<owner>/memory-pyramid-architecture.git
cd memory-pyramid-architecture
python3 scripts/init.py
python3 scripts/test_integration.py   # optional
```

Then verify the cron jobs and memory index in your OpenClaw environment.

## 🏗️ Architecture Overview

```text
Layer 1: Navigation
└── MEMORY.md

Layer 2: Knowledge
├── memory/topics/
├── memory/daily_reviews/
└── memory/weekly_distills/

Layer 3: Structured Logs
├── memory/YYYY-MM-DD.md
└── memory/YYYY-MM-DD-last-night.md

Layer 4: Raw Sources
├── OpenClaw session transcripts / memory index  preferred in current OpenClaw
└── memory/realtime-YYYY-MM-DD.md                optional legacy/raw mirror
```

## ⏰ Core Schedule

| Schedule | Job | Output |
|----------|-----|--------|
| `0 7 * * *` | Late Hour Sync | `memory/YYYY-MM-DD-last-night.md` |
| `0 10,13,16,19,22 * * *` | Micro-Sync | `memory/YYYY-MM-DD.md` |
| `10 22 * * *` | Daily Review | `memory/daily_reviews/YYYY-MM-DD.md` |
| `55 23 * * 0` | Weekly Compound | `memory/weekly_distills/YYYY-Wxx.md` |

Optional health, promotion, and dreaming jobs belong in a production overlay. See [references/production-overlay.md](references/production-overlay.md).

## 🔍 Validation

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "memory pyramid"
```

If your deployment still uses a standalone QMD CLI, `qmd list` is also useful.

## 📚 Documentation

- [CHANGELOG.md](CHANGELOG.md) - version history
- [VERSION](VERSION) - current release version
- [SKILL.md](SKILL.md) - setup and usage
- [references/architecture-details.md](references/architecture-details.md) - design deep dive
- [references/cron-reference.md](references/cron-reference.md) - cron guidance
- [references/production-overlay.md](references/production-overlay.md) - production extensions and privacy boundaries
- [references/troubleshooting.md](references/troubleshooting.md) - common fixes

## 🤝 Contributing

Please avoid committing private deployment identifiers, tokens, user IDs, channel IDs, or host-specific absolute paths. Keep reusable docs generic.

## 📄 License

[MIT](LICENSE)

---

Made with 💕 by Satoshi & Duoduo
