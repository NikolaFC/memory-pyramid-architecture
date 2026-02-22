# Architecture Deep Dive

This document explains the design decisions behind the Memory Pyramid Architecture.

## The Problem with Traditional Memory Systems

### 1. Calendar Boundary Issue

Traditional systems split activities at midnight:
```
22:00 - Start deep work
02:00 - Brilliant insight
07:00 - Continue work

Problem: Insight at 02:00 belongs to "today" but context started "yesterday"
```

**Our Solution**: Night activities (22:00-07:00) belong to "last night"
```
2026-02-16-last-night.md captures 22:00-07:00
Preserving creative flow across calendar boundaries
```

### 2. Flat Storage Problem

Traditional RAG: All memories in one bucket
```
Query → Vector search → Mixed results (old/new, raw/processed)
```

**Our Solution**: Progressive refinement pyramid
```
Layer 4 (Raw) → Layer 3 (Structured) → Layer 2 (Knowledge) → Layer 1 (Navigation)
     Filter          Extract              Distill              Index
```

### 3. Context Bloat

Loading entire conversation history → Token explosion

**Our Solution**: Hierarchical retrieval
- 90% of queries answered by Layer 2 (daily_reviews/weekly_distills)
- Only deep dives reach Layer 3 or 4
- Typical retrieval: <1k tokens vs 30k+ for full history

## Four-Layer Design Philosophy

### Layer 4: Raw (Capture Everything)

**Purpose**: Preserve complete record
**Format**: `realtime-YYYY-MM-DD.md`
**Update**: Every minute
**Content**: User queries + Assistant responses (filtered)
**Token Cost**: High (don't retrieve directly)

### Layer 3: Structured (Extract Signal from Noise)

**Purpose**: Capture important activities
**Format**: 
- `YYYY-MM-DD.md` (daytime 07:00-22:00)
- `YYYY-MM-DD-last-night.md` (night 22:00-07:00)

**Update**: 
- Hourly Micro-Sync (10/13/16/19/22:00) for daytime
- Late Hour Sync (07:00) for night

**Content**: Important decisions, code changes, configurations
**Filter**: Exclude heartbeats, chitchat, system messages

### Layer 2: Knowledge (Distill Insights)

**Purpose**: Extract actionable patterns
**Format**:
- `daily_reviews/YYYY-MM-DD.md`
- `weekly_distills/YYYY-WXX.md`
- `topics/*.md`

**Update**:
- Daily Review (22:10)
- Weekly Compound (Sun 23:55)
- Manual (topics)

**Content**:
- Achievements, lessons, decisions
- Automation candidates
- Cross-day patterns
- Long-term knowledge

### Layer 1: Navigation (Quick Orientation)

**Purpose**: Fast startup indexing
**Format**: `MEMORY.md`
**Max Size**: ~150 lines
**Content**:
- Quick links to all layers
- This week's highlights
- Active projects
- Critical decisions

## The Night-Owl Boundary (22:00-07:00)

### Why This Window?

1. **Natural Rhythm**: Many developers peak 22:00-02:00
2. **Sleep Integration**: 07:00 natural wake time for night owls
3. **Context Preservation**: Late insights stay with originating session
4. **Morning Review**: 07:00 sync provides yesterday's night summary

### Implementation

```python
# Late Hour Sync logic
def late_hour_sync():
    # Capture 22:00 yesterday → 07:00 today
    night_activities = capture_window(
        start="yesterday 22:00",
        end="today 07:00"
    )
    
    # File named with yesterday's date
    filename = f"{yesterday}-last-night.md"
    
    # Content sections
    write(filename, {
        "Late Night Activities": night_activities,
        "Key Insights": extract_insights(night_activities),
        "Decisions Made": extract_decisions(night_activities),
    })
```

## Automation Pipeline

```
Minute 0-59: Real-time Sync
    ↓ Save to realtime-*.md

Hour 10,13,16,19,22: Micro-Sync
    ↓ Read recent 3h from realtime-*.md
    ↓ Extract important activities
    ↓ Append to YYYY-MM-DD.md

07:00: Late Hour Sync
    ↓ Read 22:00-07:00 from realtime-*.md
    ↓ Extract night activities
    ↓ Save to YYYY-MM-DD-last-night.md

22:10: Daily Review
    ↓ Read YYYY-MM-DD.md (daytime)
    ↓ Read YYYY-MM-DD-last-night.md (last night)
    ↓ LLM distillation
    ↓ Save to daily_reviews/*.md

Sun 23:55: Weekly Compound
    ↓ Read 7 daily_reviews/*.md
    ↓ Cross-day pattern analysis
    ↓ LLM synthesis
    ↓ Save to weekly_distills/*.md
```

## QMD Collection Strategy

Each layer has dedicated collection for efficient retrieval:

| Collection | Pattern | Use Case |
|------------|---------|----------|
| memory-realtime | `realtime-*.md` | Deep historical search |
| memory-daily | `2026-*.md` | Specific day lookup |
| memory-late-night | `*-last-night.md` | Night activity search |
| memory-daily-reviews | `daily_reviews/*.md` | Daily insight retrieval |
| memory-weekly-distills | `weekly_distills/*.md` | Pattern analysis |
| memory-topics | `topics/*.md` | Thematic knowledge |
| memory-root | `MEMORY.md` | Quick orientation |

## Comparison with Other Architectures

| Feature | Flat RAG | OpenViking | Memory Pyramid |
|---------|----------|------------|----------------|
| Structure | Single layer | L0/L1/L2 | 4 layers |
| Night handling | Midnight split | Not specified | 22:00-07:00 window |
| Automation | Manual | Partial | Full pipeline |
| Token efficiency | Low | Medium | High |
| OpenClaw native | N/A | No | Yes |

## Future Enhancements

Potential improvements for community contribution:

1. **Multi-timezone support**: Configurable day/night boundaries
2. **Activity type detection**: Auto-tag (coding, research, chat)
3. **Sentiment tracking**: Mood patterns in daily reviews
4. **Skill suggestions**: ML-based automation candidate detection
5. **Visualization**: Memory flow dashboard
6. **Export tools**: Migrate to external knowledge bases

## References

- OpenViking paper: https://github.com/volcengine/OpenViking
- OpenClaw MemOS docs
- Vector database best practices
