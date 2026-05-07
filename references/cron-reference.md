# Cron Jobs Reference

This page documents the Memory Pyramid **core cron schedules** and the safe way to add optional production overlay jobs.

## Rules for Cron Jobs

- Every LLM-backed cron payload should explicitly specify a model allowed by the local OpenClaw config.
- Use the deployment timezone intentionally; do not silently convert local wall-clock requirements to UTC.
- Prefer `delivery.mode: none` for purely internal memory maintenance.
- Announce only when a job produces user-value, a blocker, or an actionable failure.
- Document owner, entrypoint, output files, delivery, validation, and rollback for every production overlay job.

## Core Jobs

### 1. Late Hour Sync

```json
{
  "name": "Late Hour Sync",
  "schedule": "0 7 * * *",
  "delivery": "none"
}
```

**Purpose**: Capture 22:00-07:00 activity as the previous night.

**Output**: `memory/YYYY-MM-DD-last-night.md`

**Logic**:

```text
- Inspect recent session activity or raw mirror for 22:00-07:00.
- Extract only meaningful activity: decisions, tasks, blockers, code/config changes.
- Write with the previous date.
- Avoid private raw identifiers unless they are needed for local-only audit.
```

**Suggested sections**:

```markdown
## Late Night Activities (22:00-07:00)
## Key Decisions
## Risks / Blockers
## Next Actions
```

---

### 2. Micro-Sync

```json
{
  "name": "Micro-Sync",
  "schedule": "0 10,13,16,19,22 * * *",
  "delivery": "none"
}
```

**Purpose**: Keep the structured daily log fresh without storing every raw message.

**Output**: append to `memory/YYYY-MM-DD.md`

**Logic**:

```text
- Inspect recent activity since the previous sync.
- Skip heartbeats, duplicate status, and low-value chatter.
- Keep decisions, implementation milestones, config changes, validation results, and user-visible blockers.
- Append a short timestamped section.
```

**Update format**:

```markdown
## Micro-Sync Update (14:00)

- Decision: ...
- Changed: ...
- Validation: ...
- Next: ...
```

---

### 3. Daily Review

```json
{
  "name": "Daily Review",
  "schedule": "10 22 * * *",
  "delivery": "optional announce"
}
```

**Purpose**: Distill the day into reusable knowledge.

**Input**:

- `memory/YYYY-MM-DD.md`
- `memory/YYYY-MM-DD-last-night.md`
- Relevant topic/status files, only when needed

**Output**: `memory/daily_reviews/YYYY-MM-DD.md`

**Suggested output**:

```markdown
# Daily Review: YYYY-MM-DD

## Completed
## Decisions
## Lessons
## Risks / Watchouts
## Automation Candidates
## Next Actions
```

---

### 4. Weekly Compound

```json
{
  "name": "Weekly Compound",
  "schedule": "55 23 * * 0",
  "delivery": "optional announce"
}
```

**Purpose**: Extract cross-day patterns and durable improvements.

**Input**: recent `memory/daily_reviews/*.md`

**Output**: `memory/weekly_distills/YYYY-Wxx.md`

**Suggested output**:

```markdown
# Weekly Compound: YYYY-Wxx

## Pattern Analysis
## Repeated Errors
## Repeated Successful Workflows
## Automation Opportunities
## Durable Decisions
## Knowledge Gaps
## Suggested Updates
```

## Optional Production Overlay Jobs

These jobs are useful in mature deployments, but they are **not part of the portable baseline**.

### Search / Memory Index Health Check

**Purpose**: confirm memory search indexes are healthy and current.

**Typical validation**:

```bash
openclaw memory status --json
openclaw memory search "memory pyramid"
```

If a standalone QMD CLI is present:

```bash
qmd list
```

### Short-Term Promotion

**Purpose**: rank frequently recalled short-term items and promote high-confidence durable truths into long-term memory.

**Guardrails**:

- Require evidence paths.
- Do not promote noisy one-off facts.
- Do not promote private identifiers into public docs.
- Keep manual review or safe thresholds for high-impact memory changes.

### Dreaming / REM Backfill

**Purpose**: generate grounded reflection candidates from historical sessions or short-term memory.

**Guardrails**:

- Treat outputs as candidates until reviewed.
- Prefer citations or evidence paths.
- Do not silently rewrite durable truth without newer evidence.

### Live Status Cleanup

**Purpose**: keep `memory/status/live.md` short and current.

**Guardrails**:

- Store only in-progress, blocked, or pending-decision items.
- Remove completed items after a short retention window.
- Keep background logs and long causal chains elsewhere.

## Validation Checklist

After adding or changing cron jobs:

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "recent decision"
```

Check:

- [ ] Core jobs exist with expected schedules and timezone.
- [ ] LLM-backed jobs explicitly specify a model accepted by the local config.
- [ ] Outputs are written to the intended memory paths.
- [ ] Delivery behavior is intentional.
- [ ] Failures have a visible alert path or documented inspection path.
- [ ] Public docs do not include private deployment identifiers.

## Troubleshooting

### Job Not Running

```bash
openclaw cron list
openclaw cron runs --job-id <id>
```

Common causes:

- Job disabled
- Timezone mismatch
- Model not allowed by local config
- Tool allowlist too narrow
- Output path missing

### Cron Runs but No File Changes

Check:

- Prompt tells the agent to write a file, not only summarize.
- Recent activity contained meaningful changes.
- The job is not instructed to always reply `NO_REPLY` before writing.
- File permissions allow writes.

### Search Index Looks Stale

Check:

```bash
openclaw memory status --json
openclaw memory index --force
```

If using standalone QMD:

```bash
qmd update
qmd list
```

### High Token Usage

Reduce inputs:

- Read Layer 2 before Layer 3.
- Use recent windows instead of full history.
- Store evidence paths instead of full pasted logs.
- Expand raw session transcripts only when exact recall is needed.

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
- Micro-Sync schedule
- File naming / date attribution logic
- Documentation for the deployment timezone

### Add a New Overlay Job

Before enabling it, document:

1. Owner
2. Schedule and timezone
3. Entrypoint / prompt / script
4. Model and thinking level, if LLM-backed
5. Tool allowlist
6. Output files
7. Delivery behavior
8. Failure alert behavior
9. Rollback / disable procedure
10. Privacy boundary
