# Cron Jobs Reference

Complete reference for all cron jobs in the Memory Pyramid Architecture.

## Active Jobs

### 1. Real-time Chat Sync

```json
{
  "name": "Real-time Chat Sync (每分钟)",
  "schedule": "* * * * *",
  "model": "none (Python script)",
  "delivery": "none"
}
```

**Purpose**: Capture every conversation minute-by-minute
**Output**: `realtime-YYYY-MM-DD.md`
**Token Cost**: 0 (Python script, no LLM)

**Logic**:
```python
- Read session JSONL files
- Filter out system messages, heartbeats
- Keep only user queries + assistant responses
- Append to realtime file
- Run qmd update + embed
```

---

### 2. Late Hour Sync 🌙

```json
{
  "name": "Late Hour Sync",
  "schedule": "0 7 * * *",
  "model": "moonshot/kimi-k2.5",
  "delivery": "none"
}
```

**Purpose**: Archive night activities (22:00-07:00)
**Output**: `YYYY-MM-DD-last-night.md`
**Token Cost**: ~500-1000

**Logic**:
```python
- sessions_list(activeMinutes=540)  # 9 hours
- Filter messages between 22:00-07:00
- Extract: activities, insights, decisions, tasks
- Generate markdown with sections
- Save with yesterday's date
```

**Sections**:
- ## Late Night Activities (22:00-07:00)
- ## Key Insights
- ## Decisions Made
- ## Tasks Completed

---

### 3. Hourly Micro-Sync

```json
{
  "name": "Hourly Micro-Sync (safety net)",
  "schedule": "0 10,13,16,19,22 * * *",
  "model": "moonshot/kimi-k2.5",
  "delivery": "none"
}
```

**Purpose**: Extract important daytime activities every 3 hours
**Output**: Appends to `YYYY-MM-DD.md`
**Token Cost**: ~200-500 per run

**Logic**:
```python
- sessions_list(activeMinutes=180)  # 3 hours
- Classify activities:
  - SKIP: heartbeat, chitchat, system messages
  - KEEP: decisions, code, config changes, tasks
- If meaningful activities found:
  - Append ## Micro-Sync Update (HH:MM)
  - Bullet point summary
  - qmd update + embed
- Else: NO_REPLY (silent)
```

**Update Format**:
```markdown
## Micro-Sync Update (14:00)

- Fixed cron model errors (5 jobs updated)
- Created skill directory structure
- Discussed QMD Health Check delivery config
```

---

### 4. Daily Review

```json
{
  "name": "Daily Review",
  "schedule": "10 22 * * *",
  "model": "moonshot/kimi-k2.5",
  "delivery": "announce (Telegram)"
}
```

**Purpose**: Deep distillation of full day
**Input**: 
- `YYYY-MM-DD.md` (daytime activities)
- `YYYY-MM-DD-last-night.md` (last night activities)
**Output**: `daily_reviews/YYYY-MM-DD.md`
**Token Cost**: ~2000-4000

**Logic**:
```python
- Read daytime log (5 micro-sync updates)
- Read night log (late hour sync)
- LLM analysis with prompt:
  "Extract achievements, lessons, decisions, 
   automation candidates, open questions"
- Generate structured report
- Save to daily_reviews/
- Announce completion to user
```

**Output Format**:
```markdown
# Daily Review: 2026-02-17

## Achievements
- Fixed 5 cron job model errors
- Implemented Late Hour Sync for night owls
- Created memory-pyramid-architecture skill

## Lessons Learned
- QMD retrieval is more token-efficient than file reading
- Night-owl boundary at 22:00 preserves creative flow

## Decisions Made
- Daily Review at 22:10 (after last micro-sync)
- Separate night logs with *-last-night.md naming

## Automation Candidates
- Cron model validation (prevent future errors)
- Automatic QMD collection registration

## Open Questions
- How to visualize memory pyramid flow?
```

---

### 5. Weekly Memory Compound

```json
{
  "name": "Weekly Memory Compound (Sunday 23:55)",
  "schedule": "55 23 * * 0",
  "model": "moonshot/kimi-k2.5",
  "delivery": "announce"
}
```

**Purpose**: Cross-day pattern analysis
**Input**: 7 days of `daily_reviews/*.md`
**Output**: `weekly_distills/YYYY-WXX.md`
**Token Cost**: ~4000-6000

**Logic**:
```python
- Read 7 daily review files
- Extract: achievements, lessons, decisions, automation candidates
- Cross-reference patterns:
  - Repeated unautomated work (>2 times)
  - Repeated errors (>2 times)
- LLM synthesis:
  - Pattern analysis
  - Automation opportunities
  - Error patterns
  - Knowledge gaps
- Systematic upgrade suggestions:
  - Skill Upgrade
  - Memory Upgrade
  - Convention Upgrade
  - Soul Upgrade
- Update MEMORY.md with key highlights
- Generate weekly report
```

**Output Format**:
```markdown
# Weekly Compound: 2026-W07

## Pattern Analysis
### Repeated Unautomated Work
1. Manual cron model fixing (3 times)
   → Suggest: Automated model validation skill

### Repeated Errors
1. Forgot to use QMD before file read (2 times)
   → Suggest: AGENTS.md rule reminder

## Automation Opportunities
1. **P0**: Auto-fix cron model aliases
2. **P1**: QMD retrieval prompt injection
3. **P2**: Daily memory summary notification

## Error Patterns
- Model alias drift (using deprecated aliases)
- Direct file reading without QMD check

## Knowledge Gaps
- OpenViking architecture details
- Advanced QMD query syntax

## Systematic Upgrade Suggestions

### Skill Upgrade
- Create cron-model-validator skill
- Create qmd-reminder skill

### Memory Upgrade
- Add OpenViking research to topics/
- Create QMD best practices guide

### Convention Upgrade
- Update AGENTS.md with model alias rules
- Add QMD-first search reminder

### Soul Upgrade
- More proactive pattern recognition
- Better token cost awareness

## Key Insights
This week focused on memory architecture optimization.
Major achievement: Night-owl friendly four-layer pyramid.
```

---

### 6. QMD Health Check

```json
{
  "name": "QMD Health Check (Monday 03:30)",
  "schedule": "30 3 * * 1",
  "model": "moonshot/kimi-k2.5",
  "delivery": "none"
}
```

**Purpose**: Weekly database maintenance check
**Output**: `reports/qmd-health-YYYY-MM-DD.md`
**Token Cost**: ~500

**Checks**:
- Database size (>300MB warning, >500MB critical)
- Orphaned chunks count
- Collection health status
- Index fragmentation

**Actions**:
- 🔴 Critical: Send WhatsApp notification
- ⚠️ Warning: Log to report
- ✅ Normal: NO_REPLY

---

## Disabled/Backup Jobs

### Session Health Monitor (Disabled)

```json
{
  "name": "Session Health Monitor",
  "enabled": false,
  "schedule": "every 2 hours"
}
```

**Purpose**: Monitor token usage, suggest session refresh
**Status**: Disabled (using manual /status instead)

---

### Daily Memory Sync (Disabled)

```json
{
  "name": "Daily Memory Sync (23:45)",
  "enabled": false
}
```

**Purpose**: Original daily log generator
**Status**: Disabled (replaced by Micro-Sync + Late Hour Sync)

---

## Troubleshooting

### Job Not Running

```bash
# Check job status
openclaw cron list

# Check runs history
openclaw cron runs --job-id <id>
```

### Model Errors

Common errors:
- `model not allowed: moonshot/kimi` → Use `moonshot/kimi-k2.5`
- `model not allowed: moonshot/trinity` → Use `moonshot/kimi-k2.5`

### Delivery Errors

- `Delivering to WhatsApp requires target` → Set delivery.mode to "none"
- `channel not configured` → Check channel configuration

### High Token Usage

- Daily Review: 2000-4000 tokens (normal)
- Weekly Compound: 4000-6000 tokens (normal)
- If higher: Check input file sizes

---

## Customization

### Change Night Boundary

Edit `scripts/config.json`:
```json
{
  "night_owl": {
    "day_end": "23:00",
    "day_start": "08:00"
  }
}
```

Then update:
- Late Hour Sync schedule
- Hourly Micro-Sync schedule
- File naming in scripts

### Add New Collection

1. Create directory: `mkdir ~/.openclaw/workspace/memory/new_layer`
2. Add to QMD config in `openclaw.json`
3. Create sync cron job
4. Add retrieval priority in `references/retrieval-guide.md`
