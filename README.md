# Memory Pyramid Architecture

> 🏗️ Production-ready four-layer memory architecture for OpenClaw
> 🌙 Optimized for night owls - preserve your creative flow!

## What is This?

A battle-tested memory system that organizes your OpenClaw conversations into a progressive refinement pipeline:

```
Raw Conversations → Structured Logs → Daily Insights → Weekly Patterns
     (Auto)            (Auto)         (Auto)          (Auto)
```

## Why Use It?

| Problem | Solution |
|---------|----------|
| Memory scattered across days | Unified timeline with night-owl boundaries |
| Can't find past insights | Four-layer progressive refinement |
| Context bloat | Automatic summarization at each layer |
| Late-night work split across days | 22:00-07:00 belongs to "last night" |

## Installation

```bash
# One-command setup
python3 ~/.openclaw/workspace/skills/memory-pyramid-architecture/scripts/init.py
```

## Quick Example

After running for a week, your memory structure looks like:

```
memory/
├── 2026-02-10.md                    # Daytime activities
├── 2026-02-10-last-night.md         # Night activities (22:00-07:00)
├── daily_reviews/
│   ├── 2026-02-10.md               # Daily distilled insights
│   └── 2026-02-11.md
├── weekly_distills/
│   └── 2026-W06.md                 # Weekly pattern analysis
└── topics/
    └── project_alfa.md              # Long-term knowledge
```

## How It Works

1. **Every minute**: Conversations sync to `realtime-*.md`
2. **Every 3 hours** (daytime): Important activities extracted to `YYYY-MM-DD.md`
3. **07:00 daily**: Last night's activities archived to `*-last-night.md`
4. **22:10 daily**: Full day summarized to `daily_reviews/*.md`
5. **Sunday 23:55**: Week analyzed for patterns in `weekly_distills/*.md`

## Documentation

- Full guide: [SKILL.md](SKILL.md)
- Architecture deep dive: [references/architecture-details.md](references/architecture-details.md)
- Troubleshooting: [references/troubleshooting.md](references/troubleshooting.md)

## Community

This skill is part of the OpenClaw ecosystem. Share improvements, report issues, and collaborate!

---

Made with 💕 by Satoshi & Duoduo
