# DSH Adapter — Memory Pyramid on DeepSeek Harness

This document maps the portable Memory Pyramid baseline onto **DeepSeek
Harness (DSH)** deployments. It contains no deployment-specific paths or
identifiers; substitute your own `<memory-root>`.

## Mapping overview

| Baseline concept | OpenClaw deployment | DSH deployment |
|---|---|---|
| Four layer directories | under the OpenClaw workspace | under your `<memory-root>` (e.g. a shared memory dir) |
| Layer 4 raw sources | OpenClaw session transcripts / memory index | DSH session records (`session.jsonl` / `.zstd` per session) |
| Retrieval index (QMD collections) | `qmd` CLI + `openclaw.json` | DSH retrieval skill/tools over plain files (read/glob/grep) |
| Cron engine | `openclaw cron add` | DSH cron engine (5-field cron, local time) |
| Model selection | explicit model in cron payload | explicit `model` per job (mandatory) |

## Initializing the baseline

```bash
python3 scripts/init.py --root <memory-root>
```

`init.py` is harness-agnostic since v1.1.0: it only creates layer directories,
optionally appends the diagram to `<memory-root>/MEMORY.md`, and prints the
cron contract. It refuses to guess a location — pass `--root` explicitly.

## Cron jobs on DSH

Create the four core jobs in the DSH cron engine. **Every job must specify an
explicit model** (a lightweight model is the usual choice for distillation
jobs; use a stronger model only if weekly compounding quality is insufficient).

| Job | Schedule | Output (relative to `<memory-root>`) |
|---|---|---|
| Late Hour Sync | `0 7 * * *` | `YYYY-MM-DD-last-night.md` (previous night's date) |
| Micro-Sync | `0 10,13,16,19,22 * * *` | append to `YYYY-MM-DD.md` |
| Daily Review | `10 22 * * *` | `daily_reviews/YYYY-MM-DD.md` |
| Weekly Compound | `55 23 * * 0` | `weekly_distills/YYYY-Wxx.md` (or dated file) |

### Inputs per job

- **Late Hour Sync / Micro-Sync** need *recent session activity* as input.
  Point their context at DSH session records covering the window since the
  previous successful run, plus the current structured log. Late Hour Sync
  should additionally receive the previous day's log; it attributes 22:00-07:00
  activity to the previous night (see night-owl rules in
  `references/architecture-details.md`).
- **Daily Review** needs the current day log, the previous-night log (may be
  missing — treat honestly), and the navigation-layer files (index / todos /
  active tasks).
- **Weekly Compound** needs the most recent 7 `daily_reviews/*.md`.

Outputs: Late Hour Sync, Daily Review, and Weekly Compound write full files;
Micro-Sync **appends** a timestamped section to the day log.

### Engine capabilities your DSH cron engine needs

If your DSH cron engine is a plain LLM caller with file context injection,
the following capabilities are required to run the pyramid faithfully:

1. **Session extraction** — read compressed DSH session records and extract
   user/assistant text messages since a given timestamp (skip system-injected
   context snapshots; they are noise for memory distillation).
2. **Glob context** — inject the N most recently modified files matching a
   pattern (for Weekly Compound's review inputs).
3. **Append output mode** — Micro-Sync must append, never overwrite.
4. **Previous-date placeholder** — Late Hour Sync output files are named with
   the *previous* night's date (a `{date-1d}`-style expansion handles
   month/year boundaries correctly).

If the engine cannot extract session activity, the baseline degrades: sync
jobs get no raw input and must honestly report "no source data" instead of
fabricating activity.

## Retrieval on DSH

QMD collections have no DSH equivalent; use the harness's plain-file tools
and follow the baseline retrieval priority
(see `scripts/config.json` → `retrieval_priority`):

1. `daily_reviews/` — distilled daily insights
2. `weekly_distills/` — cross-day patterns
3. `topics/` — long-term thematic truth
4. `YYYY-MM-DD.md` — structured day log
5. `YYYY-MM-DD-last-night.md` — structured night log
6. raw session records — exact recall only

## Validation checklist

After installation, verify:

- [ ] All four jobs exist with the expected schedules and timezone.
- [ ] Every LLM-backed job explicitly specifies a model.
- [ ] Micro-Sync appends (run it twice and confirm the file grew).
- [ ] Late Hour Sync names its output with the previous night's date.
- [ ] Jobs with no source data report that honestly instead of fabricating.
- [ ] Retrieval reads the distilled layers before the raw layer.

## Night-owl boundary

22:00-07:00 activity belongs to the previous night (configurable in
`scripts/config.json` → `night_owl`). Keep job schedules, file naming, and
prompt instructions consistent with this boundary when you customize it.
