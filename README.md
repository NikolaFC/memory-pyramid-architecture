# Memory Pyramid Architecture for OpenClaw

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-blue.svg)](https://openclaw.ai)

> 🏗️ A production-ready, four-layer memory architecture for OpenClaw with special optimization for night owls.

## ✨ Features

- 🏗️ **Four-Layer Pyramid**: Raw → Structured → Knowledge → Navigation
- 🌙 **Night-Owl Friendly**: Late night activities (22:00-07:00) belong to "last night"
- 🔄 **Fully Automated**: 6 cron jobs handle everything
- 📊 **QMD Integrated**: All layers indexed for semantic search
- ⚡ **Token Efficient**: 90% reduction vs flat RAG

## 🚀 Quick Start

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/memory-pyramid-architecture.git

# Navigate to skill directory
cd memory-pyramid-architecture

# Run initialization
python3 scripts/init.py
```

Then add the cron jobs via OpenClaw interface.

## 📁 Repository Structure

```
memory-pyramid-architecture/
├── SKILL.md                    # Main skill documentation
├── README.md                   # This file
├── scripts/
│   ├── init.py                # One-command setup
│   └── config.json            # Configuration
├── references/                # Detailed docs
│   ├── architecture-details.md
│   ├── cron-reference.md
│   └── troubleshooting.md
└── examples/                  # Template files
    ├── layer4-raw/
    ├── layer3-structured/
    └── layer2-knowledge/
```

## 🏗️ Architecture Overview

```
Layer 1: Navigation
└── MEMORY.md (quick index)

Layer 2: Knowledge (Processed)
├── topics/ (long-term memory)
├── daily_reviews/ (daily essence)
└── weekly_distills/ (weekly patterns)

Layer 3: Structured (Semi-processed)
├── YYYY-MM-DD.md (daytime 07:00-22:00)
└── YYYY-MM-DD-last-night.md (night 22:00-07:00)

Layer 4: Raw (Original)
└── realtime-YYYY-MM-DD.md (minute-by-minute)
```

## ⏰ Automation Schedule

| Time | Job | Output |
|------|-----|--------|
| 07:00 | Late Hour Sync | `*-last-night.md` |
| 10/13/16/19/22:00 | Hourly Micro-Sync | `YYYY-MM-DD.md` |
| 22:10 | Daily Review | `daily_reviews/*.md` |
| Sun 23:55 | Weekly Compound | `weekly_distills/*.md` |

## 📚 Documentation

- **[SKILL.md](SKILL.md)** - Complete usage guide
- **[references/architecture-details.md](references/architecture-details.md)** - Design deep dive
- **[references/cron-reference.md](references/cron-reference.md)** - All cron jobs explained
- **[references/troubleshooting.md](references/troubleshooting.md)** - Common issues & fixes

## 🌟 Why Night-Owl Optimized?

Traditional systems split activities at midnight, cutting your creative flow in half:

```
22:00 - Start deep work
02:00 - Brilliant insight  ← Belongs to "today" but context is "yesterday"
07:00 - Continue work
```

Memory Pyramid preserves the flow:

```
22:00-07:00 → 2026-02-16-last-night.md  ← Complete session preserved
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🙏 Credits

- **Concept**: Inspired by [OpenViking](https://github.com/volcengine/OpenViking) (ByteDance/Volcano Engine)
- **Design**: [Satoshi](https://github.com/NikolaFC) & Duoduo
- **Community**: OpenClaw users

## 📄 License

[MIT](LICENSE) - Free for personal and commercial use within OpenClaw ecosystem.

## 🔗 Links

- [OpenClaw Documentation](https://docs.openclaw.ai)
- [OpenViking Repository](https://github.com/volcengine/OpenViking)
- [Issues](../../issues)

---

Made with 💕 by Satoshi & Duoduo
