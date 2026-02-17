---
name: memory-pyramid-architecture
description: Four-layer pyramid memory architecture for OpenClaw with night-owl optimization (22:00-07:00归属前一天). Implements real-time → micro-sync → daily-review → weekly-compound workflow.
triggers:
  - "setup memory architecture"
  - "initialize pyramid memory"
  - "configure night-owl memory"
  - "memory workflow setup"
author: "Satoshi & Duoduo"
version: "1.0.0"
date: "2026-02-17"
---

# Memory Pyramid Architecture Skill

A production-ready, four-layer memory architecture designed for OpenClaw with special optimization for night-owl users.

## ✨ Key Features

- 🏗️ **Four-Layer Pyramid**: Raw → Structured → Knowledge → Navigation
- 🌙 **Night-Owl Friendly**: Late night activities (22:00-07:00) belong to "last night", not split across days
- 🔄 **Automated Workflow**: Real-time → Micro-Sync → Daily Review → Weekly Compound
- 📊 **QMD Integration**: All layers indexed for semantic search
- ⚡ **Token Efficient**: Progressive refinement reduces context bloat

## 🎯 Architecture Overview

```
Layer 1: Navigation
└── MEMORY.md (quick index, ~150 lines)

Layer 2: Knowledge (Processed)
├── topics/ (long-term thematic memory)
├── daily_reviews/ (daily distilled essence)
└── weekly_distills/ (weekly pattern analysis)

Layer 3: Structured Logs (Semi-processed)
├── YYYY-MM-DD.md (daytime 07:00-22:00)
└── YYYY-MM-DD-last-night.md (night 22:00-07:00)

Layer 4: Raw (Original)
└── realtime-YYYY-MM-DD.md (minute-by-minute sync)
```

## 🚀 Quick Start

### 1. Initialize the Architecture

```bash
# Run initialization script
python3 ~/.openclaw/workspace/skills/memory-pyramid-architecture/scripts/init.py
```

This will:
- Create required directories (`daily_reviews/`, `weekly_distills/`)
- Update `MEMORY.md` with architecture diagram
- Add QMD collection paths to `openclaw.json`
- Install cron jobs with correct scheduling

### 2. Verify Setup

```bash
# Check directory structure
ls -la ~/.openclaw/workspace/memory/

# Verify QMD collections
qmd list | grep memory-

# Check cron jobs
openclaw cron list
```

## 📅 Cron Schedule

| Time | Job | Output |
|------|-----|--------|
| 07:00 | Late Hour Sync | `*-last-night.md` (night activities) |
| 10/13/16/19/22:00 | Hourly Micro-Sync | `YYYY-MM-DD.md` updates |
| 22:10 | Daily Review | `daily_reviews/*.md` |
| Sun 23:55 | Weekly Compound | `weekly_distills/*.md` |

## 📖 Usage Guide

### For Night Owls

Your late-night work (22:00-07:00) is automatically captured and associated with "last night", preserving creative flow across calendar boundaries.

### Daily Workflow

1. **Morning (07:00)**: Review `*-last-night.md` for yesterday's late insights
2. **Evening (22:10)**: Check `daily_reviews/*.md` for today's summary
3. **Sunday**: Review `weekly_distills/*.md` for pattern insights

### Memory Retrieval Priority

When searching memories, follow this priority:

1. `daily_reviews/` - Most distilled daily insights
2. `weekly_distills/` - Cross-day patterns
3. `topics/` - Long-term thematic knowledge
4. `YYYY-MM-DD.md` - Specific day activities
5. `*-last-night.md` - Specific night activities
6. `realtime-*.md` - Raw logs (last resort)

## 🔧 Customization

### Adjust Time Windows

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

### Add New Collections

To add a new memory layer:

1. Create directory: `mkdir ~/.openclaw/workspace/memory/new_layer`
2. Add to QMD config in `openclaw.json`
3. Update retrieval priority in `references/retrieval-guide.md`

## 📚 Documentation

- [Architecture Details](references/architecture-details.md) - Deep dive into design decisions
- [Cron Reference](references/cron-reference.md) - All cron jobs explained
- [Troubleshooting](references/troubleshooting.md) - Common issues and fixes
- [Examples](examples/) - Sample memory files

## 🤝 Contributing

This skill is designed for the OpenClaw community. Contributions welcome!

### To Contribute:

1. Fork the skill directory
2. Make your improvements
3. Test thoroughly
4. Submit via OpenClaw community channels

### Areas for Contribution:

- Additional time zone support
- Integration with external memory stores
- Visualization tools for memory flow
- Custom refinement prompts
- Migration tools from other architectures

## 🙏 Credits

- **Concept**: Inspired by OpenViking (ByteDance/Volcano Engine)
- **Design**: Satoshi & Duoduo
- **Community**: OpenClaw users

## 📄 License

MIT - Free for personal and commercial use within OpenClaw ecosystem.

---

**Questions?** Open an issue in the OpenClaw community or ask your AI assistant!
