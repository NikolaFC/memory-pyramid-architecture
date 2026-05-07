---
name: memory-pyramid-architecture
description: Four-layer memory baseline for OpenClaw with night-owl optimization (22:00-07:00 belongs to the previous night). Implements Late Hour Sync, Micro-Sync, Daily Review, and Weekly Compound, with optional production overlays.
triggers:
  - "setup memory architecture"
  - "initialize pyramid memory"
  - "configure night-owl memory"
  - "memory workflow setup"
author: "Satoshi & Duoduo"
version: "1.1.0"
date: "2026-05-07"
---

# Memory Pyramid Architecture Skill

**Current version: 1.1.0**

A production-ready, four-layer memory baseline for OpenClaw with night-owl-friendly time boundaries.

This skill describes the **portable baseline**. Production deployments may add live status, indexed session transcripts, short-term promotion/dreaming, KB gardening, or skill/evolver governance as overlays. Keep public documentation generic and avoid private deployment identifiers.

## ✨ Key Features

- 🏗️ **Four-layer pyramid**: Raw → Structured → Knowledge → Navigation
- 🌙 **Night-owl friendly**: 22:00-07:00 activity belongs to the previous night
- 🔄 **Core workflow**: Late Hour Sync → Micro-Sync → Daily Review → Weekly Compound
- 📊 **Search integrated**: memory files and session transcripts can be indexed for retrieval
- ⚡ **Token efficient**: retrieve distilled layers first, raw sources last
- 🧩 **Overlay friendly**: optional production jobs do not change the baseline contract

## 🎯 Architecture Overview

```text
Layer 1: Navigation
└── MEMORY.md

Layer 2: Knowledge
├── memory/topics/            long-term thematic truth
├── memory/daily_reviews/     daily distilled insights
└── memory/weekly_distills/   weekly pattern analysis

Layer 3: Structured Logs
├── memory/YYYY-MM-DD.md
└── memory/YYYY-MM-DD-last-night.md

Layer 4: Raw Sources
├── OpenClaw session transcripts / memory index  preferred in current OpenClaw
└── memory/realtime-YYYY-MM-DD.md                optional legacy/raw mirror
```

## 🚀 Quick Start

### 1. Initialize or verify the baseline

```bash
python3 scripts/init.py
```

This should:

- Create required directories (`memory/topics/`, `memory/daily_reviews/`, `memory/weekly_distills/`)
- Ensure `MEMORY.md` points to the memory layers
- Register or document memory search/index paths for the local OpenClaw deployment
- Prepare the core cron schedule from `scripts/config.json`

### 2. Verify setup

Repository checks:

```bash
python3 scripts/verify_suite.py
python3 scripts/hygiene_scan.py
python3 scripts/sync_drift_check.py
python3 scripts/test_integration.py
```

Deployment checks:

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "memory pyramid"
```

If your environment still uses a standalone QMD CLI, `qmd list` is also useful.

## 📅 Core Cron Schedule

| Schedule | Job | Output |
|----------|-----|--------|
| `0 7 * * *` | Late Hour Sync | `memory/YYYY-MM-DD-last-night.md` |
| `0 10,13,16,19,22 * * *` | Micro-Sync | `memory/YYYY-MM-DD.md` |
| `10 22 * * *` | Daily Review | `memory/daily_reviews/YYYY-MM-DD.md` |
| `55 23 * * 0` | Weekly Compound | `memory/weekly_distills/YYYY-Wxx.md` |

Optional health checks, short-term promotion, dreaming, or KB gardening jobs are production overlays. See `references/production-overlay.md`.

## 📖 Usage Guide

### For night owls

Late-night work from 22:00 to 07:00 is associated with the previous night, preserving continuity across midnight.

### Daily workflow

1. **07:00**: Late Hour Sync captures the previous night.
2. **10/13/16/19/22:00**: Micro-Sync appends meaningful daytime activity.
3. **22:10**: Daily Review distills the day.
4. **Sunday 23:55**: Weekly Compound extracts patterns and repeated work.

### Retrieval priority

1. `memory/daily_reviews/` - distilled daily insights
2. `memory/weekly_distills/` - cross-day patterns
3. `memory/topics/` - long-term thematic truth
4. `memory/YYYY-MM-DD.md` - structured day log
5. `memory/YYYY-MM-DD-last-night.md` - structured night log
6. Session transcripts / raw mirror - exact recall and deep audit

## 🔧 Customization

### Adjust time windows

Edit `scripts/config.json`:

```json
{
  "night_owl": {
    "day_end": "22:00",
    "day_start": "07:00",
    "timezone": "Europe/London"
  }
}
```

### Add a production overlay

Document the overlay separately before enabling it:

- Owner / entrypoint
- Schedule and timezone
- Explicit model, if it uses an LLM
- Output files
- Delivery behavior
- Rollback / disable procedure
- Privacy boundaries

## 📚 Documentation

- [Changelog](CHANGELOG.md) - release history
- [Architecture Details](references/architecture-details.md) - design deep dive
- [Cron Reference](references/cron-reference.md) - core and optional cron guidance
- [Production Overlay](references/production-overlay.md) - safe production extensions
- [Troubleshooting](references/troubleshooting.md) - common issues and fixes
- [Examples](examples/) - sample memory files

## 🤝 Contributing

This skill is designed for the OpenClaw community. Contributions welcome.

Before opening a PR, confirm that docs do not include tokens, user IDs, channel IDs, private hostnames, host-specific absolute paths, or private deployment topology.

## 🙏 Credits

- **Concept**: Inspired by OpenViking
- **Design**: Satoshi & Duoduo
- **Community**: OpenClaw users

## 📄 License

MIT - Free for personal and commercial use within the OpenClaw ecosystem.
