# Memory Pyramid Architecture

> 🏗️ Production-ready four-layer memory baseline for OpenClaw
> 🌙 Optimized for night owls: 22:00-07:00 belongs to the previous night.

## What is This?

A memory system that organizes OpenClaw conversations into a progressive refinement pipeline:

```text
Raw Sources → Structured Logs → Daily Insights → Weekly Patterns → Navigation
```

The portable baseline is intentionally small. Local production deployments can add overlays such as live status, session indexing, short-term promotion, dreaming, KB gardening, and skill/evolver governance.

## Why Use It?

| Problem | Solution |
|---------|----------|
| Memory scattered across days | Unified timeline with night-owl boundaries |
| Hard to find past insights | Progressive refinement and search index |
| Context bloat | Read distilled layers first |
| Late-night work split across dates | 22:00-07:00 belongs to the previous night |
| Production needs differ | Keep local overlays separate from the public baseline |

## Installation

```bash
python3 scripts/init.py
```

If this repository is installed as an OpenClaw skill, run the same command from the skill directory.

## Quick Example

After running for a week, the memory structure may look like:

```text
memory/
├── 2026-02-10.md                    # Daytime activities
├── 2026-02-10-last-night.md         # Night activities (22:00-07:00)
├── daily_reviews/
│   ├── 2026-02-10.md                # Daily distilled insights
│   └── 2026-02-11.md
├── weekly_distills/
│   └── 2026-W06.md                  # Weekly pattern analysis
└── topics/
    └── project_example.md           # Long-term knowledge
```

## How It Works

1. **Raw sources**: OpenClaw session transcripts / memory index, or optional `realtime-*.md` mirror.
2. **Micro-Sync**: meaningful daytime activity goes to `YYYY-MM-DD.md`.
3. **Late Hour Sync**: 22:00-07:00 activity goes to `YYYY-MM-DD-last-night.md`.
4. **Daily Review**: daily logs become `daily_reviews/*.md`.
5. **Weekly Compound**: daily reviews become `weekly_distills/*.md`.
6. **Navigation**: durable, high-signal pointers go to `MEMORY.md`.

## Validation

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "memory pyramid"
```

## Documentation

- Full guide: [SKILL.md](SKILL.md)
- Architecture deep dive: [references/architecture-details.md](references/architecture-details.md)
- Production overlays: [references/production-overlay.md](references/production-overlay.md)
- Troubleshooting: [references/troubleshooting.md](references/troubleshooting.md)

## Community

This skill is part of the OpenClaw ecosystem. Share improvements, report issues, and collaborate.

---

Made with 💕 by Satoshi & Duoduo
