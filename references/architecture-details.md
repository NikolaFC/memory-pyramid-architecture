# Architecture Deep Dive

This document explains the design decisions behind Memory Pyramid Architecture for OpenClaw.

## Baseline vs Production Overlay

The repository defines a **portable baseline**. A real production deployment can add extra jobs and indexes, but those additions should be documented as overlays instead of changing the baseline contract.

- **Baseline**: `MEMORY.md`, structured logs, daily reviews, weekly distills, topics, core cron schedules.
- **Production overlay**: live status files, indexed session transcripts, short-term recall promotion, dreaming/REM summaries, KB Gardener, skill/evolver signal surfaces, and health/watchdog jobs.

This separation keeps the public repo reusable while still allowing local deployments to evolve.

## The Problem with Traditional Memory Systems

### 1. Calendar Boundary Issue

Traditional systems split activities at midnight:

```text
22:00 - Start deep work
02:00 - Important insight
07:00 - Continue work

Problem: the 02:00 insight is stored under a different calendar day even though it belongs to the same work session.
```

**Solution**: 22:00-07:00 activity belongs to the previous night.

```text
YYYY-MM-DD-last-night.md captures 22:00-07:00 and preserves session continuity.
```

### 2. Flat Storage Problem

Traditional RAG puts every memory in one bucket:

```text
Query → vector search → mixed raw and distilled results
```

**Solution**: progressive refinement.

```text
Layer 4 Raw Sources → Layer 3 Structured Logs → Layer 2 Knowledge → Layer 1 Navigation
        preserve              extract signal            distill          orient quickly
```

### 3. Context Bloat

Loading entire conversation history is expensive and noisy.

**Solution**: hierarchical retrieval.

- Most queries should start from Layer 2 or Layer 1.
- Exact proof or audit requests can expand to Layer 3 or Layer 4.
- Raw session transcripts are valuable, but should not be the default context payload.

## Four-Layer Design Philosophy

### Layer 4: Raw Sources

**Purpose**: Preserve or index the complete source record.

**Preferred current source**: OpenClaw session transcripts and the OpenClaw memory index.

**Optional legacy/raw mirror**: `memory/realtime-YYYY-MM-DD.md`.

**Update pattern**:

- Current OpenClaw deployments can index session transcripts directly.
- Older deployments may mirror selected raw messages into `realtime-*.md`.
- Raw sources are high-token and should be used mainly for exact recall, audit, or conflict resolution.

### Layer 3: Structured Logs

**Purpose**: Capture important activities in a human-readable timeline.

**Format**:

- `memory/YYYY-MM-DD.md` for daytime activity
- `memory/YYYY-MM-DD-last-night.md` for 22:00-07:00 activity

**Update**:

- Micro-Sync at 10/13/16/19/22:00
- Late Hour Sync at 07:00

**Content**:

- Decisions
- Code/config changes
- Task progress
- Risks and blockers
- Pointers to evidence paths

**Filter out**:

- Routine heartbeats
- Low-value chatter
- Duplicate status noise
- Private raw identifiers that are not needed for future recall

### Layer 2: Knowledge

**Purpose**: Distill actionable patterns and stable truth.

**Format**:

- `memory/daily_reviews/YYYY-MM-DD.md`
- `memory/weekly_distills/YYYY-Wxx.md`
- `memory/topics/*.md`

**Update**:

- Daily Review at 22:10
- Weekly Compound on Sunday 23:55
- Manual or guarded promotion for topics

**Content**:

- Durable decisions
- Repeated lessons
- Reusable patterns
- Automation opportunities
- Long-term project knowledge

### Layer 1: Navigation

**Purpose**: Fast orientation.

**Format**: `MEMORY.md`

**Content**:

- Pointers to current memory layers
- High-value durable facts
- Topic index
- Retrieval guidance

Keep `MEMORY.md` concise. Put large operational details in topic pages, docs, or references.

## The Night-Owl Boundary

### Why 22:00-07:00?

1. **Context preservation**: late-night work often continues the previous evening.
2. **Review rhythm**: 07:00 creates a natural close for the night block.
3. **Searchability**: related decisions stay together instead of splitting at midnight.

### Late Hour Sync Logic

```python
def late_hour_sync():
    night_activities = capture_window(
        start="yesterday 22:00",
        end="today 07:00",
    )

    filename = f"{yesterday}-last-night.md"

    write(filename, {
        "Late Night Activities": night_activities,
        "Key Insights": extract_insights(night_activities),
        "Decisions Made": extract_decisions(night_activities),
        "Next Actions": extract_next_actions(night_activities),
    })
```

## Automation Pipeline

```text
Raw session transcripts / optional realtime mirror
    ↓
10/13/16/19/22: Micro-Sync
    ↓ append meaningful daytime changes
memory/YYYY-MM-DD.md
    ↓
07:00: Late Hour Sync
    ↓ capture 22:00-07:00 as previous night
memory/YYYY-MM-DD-last-night.md
    ↓
22:10: Daily Review
    ↓ distill decisions, lessons, risks, next actions
memory/daily_reviews/YYYY-MM-DD.md
    ↓
Sun 23:55: Weekly Compound
    ↓ extract patterns, automation opportunities, durable truth
memory/weekly_distills/YYYY-Wxx.md
    ↓
MEMORY.md and memory/topics/*.md receive only durable, high-signal updates.
```

## Search / Index Strategy

Current OpenClaw deployments can validate memory indexing with:

```bash
openclaw memory status --json
openclaw memory search "memory pyramid"
```

A deployment may expose separate collections such as:

| Source | Pattern | Use case |
|--------|---------|----------|
| root | `MEMORY.md` | quick orientation |
| topics | `memory/topics/*.md` | durable thematic truth |
| daily reviews | `memory/daily_reviews/*.md` | daily distilled insight |
| weekly distills | `memory/weekly_distills/*.md` | cross-day patterns |
| structured logs | `memory/YYYY-MM-DD*.md` | timeline lookup |
| sessions | OpenClaw session transcripts | exact recall / audit |
| raw mirror | `memory/realtime-*.md` | optional legacy deep search |

If your environment still uses a standalone QMD CLI, `qmd list` remains a useful diagnostic.

## Production Overlay Examples

Optional overlays should not be hard-coded into the baseline docs unless they are generic and reusable.

Common overlays:

- `memory/status/live.md` for short current-state tracking
- Short-term recall promotion into durable memory
- Dreaming / REM summaries for candidate long-term truths
- KB Gardener for turning sources into `docs/kb/*` pages
- Skill/evolver boundaries for promoting repeated workflows into skills or rules
- Memory index health checks

See [production-overlay.md](production-overlay.md).

## Comparison with Other Architectures

| Feature | Flat RAG | OpenViking-inspired hierarchy | Memory Pyramid |
|---------|----------|-------------------------------|----------------|
| Structure | Single layer | Multi-stage memory | 4-layer OpenClaw baseline |
| Night handling | Midnight split | Not usually explicit | 22:00-07:00 window |
| Raw source | Mixed with summaries | Depends on implementation | Session transcripts or raw mirror |
| Retrieval | Direct vector search | Progressive | Distilled-first with raw expansion |
| OpenClaw native | No | No | Yes |

## Privacy Boundary

Public docs and PRs should not include:

- Tokens, credentials, or secret references
- User IDs, chat IDs, channel IDs, guild/server IDs, message IDs
- Private hostnames, private absolute paths, or deployment topology
- Account balances, trading data, private logs, or screenshots
- Raw conversation excerpts unless explicitly sanitized and necessary

Prefer generic examples and reproducible commands.

## Future Enhancements

1. Multi-timezone support
2. Activity-type tagging
3. Memory-quality linting
4. Search result evaluation harness
5. Visualization dashboard
6. Export tools for external knowledge bases

## References

- OpenViking: https://github.com/volcengine/OpenViking
- OpenClaw docs: https://docs.openclaw.ai
