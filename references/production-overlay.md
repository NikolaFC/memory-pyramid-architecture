# Production Overlay Guide

Memory Pyramid has a small, reusable baseline. Production deployments often add extra capabilities. This page explains how to document those additions safely without leaking private deployment details or turning local experiments into the public baseline.

## Principle

Treat the repository as the **baseline contract** and production additions as **overlays**.

```text
Baseline Memory Pyramid
  ├─ MEMORY.md
  ├─ memory/YYYY-MM-DD.md
  ├─ memory/YYYY-MM-DD-last-night.md
  ├─ memory/daily_reviews/
  ├─ memory/weekly_distills/
  └─ memory/topics/

Production Overlay
  ├─ live status dashboard files
  ├─ session transcript indexing
  ├─ short-term recall promotion
  ├─ dreaming / REM candidate generation
  ├─ KB Gardener workflow
  ├─ skill/evolver signal boundaries
  └─ memory/search health checks
```

An overlay can be powerful, but it should remain optional and separately documented.

## Common Overlay Components

### 1. Live Status

**Typical path**: `memory/status/live.md`

**Purpose**: show only current in-progress, blocked, or pending-decision tasks.

**Rules**:

- Keep it short.
- Remove completed items after a short retention window.
- Do not store raw logs, private IDs, or long causal histories.

### 2. Session Transcript Indexing

**Purpose**: use OpenClaw session transcripts as the preferred raw source for exact recall.

**Validation**:

```bash
openclaw memory status --json
openclaw memory search "example query"
```

**Notes**:

- Session transcripts are local/private by default.
- Public docs should describe the concept, not private session keys or channel IDs.
- `memory/realtime-YYYY-MM-DD.md` can remain an optional legacy/raw mirror for older deployments.

### 3. Short-Term Recall Promotion

**Purpose**: promote repeated, evidence-backed short-term recalls into durable memory.

**Guardrails**:

- Require evidence paths or citations.
- Prefer candidate review before durable promotion.
- Avoid promoting noisy one-off facts.
- Never promote secrets or private identifiers into public docs.

### 4. Dreaming / REM Candidate Generation

**Purpose**: generate reflection candidates or historical summaries from sessions and short-term memory.

**Guardrails**:

- Treat generated reflections as candidates until reviewed.
- Prefer grounded outputs with source references.
- Newer evidence overrides older summaries.

### 5. KB Gardener

**Purpose**: turn raw sources and repeated context into stable knowledge pages.

**Suggested flow**:

```text
ingest → route → compile → enrich → lint → promote
```

**Suggested paths**:

```text
memory/kb_workbench/<topic>/     draft/workbench area
docs/kb/<topic>/                 canonical reusable knowledge
```

**Boundary**:

- Memory Pyramid remembers what happened.
- KB Gardener maintains reusable knowledge.
- Do not call this a Memory Pyramid rewrite; it is an overlay.

### 6. Skill / Evolver Boundary

**Purpose**: decide where repeated lessons go.

| Signal | Best destination |
|--------|------------------|
| One-off fact or decision | Memory Pyramid |
| Stable reusable context | Reference / docs |
| Repeated executable workflow | Skill |
| Structural pressure across workflows | Evolver / governance ledger |

This avoids stuffing executable SOPs into memory or creating noisy skills from one-off facts.

## Overlay Documentation Template

When adding an overlay job or subsystem, document:

```markdown
## <Overlay Name>

- Purpose:
- Owner:
- Entrypoint:
- Schedule / trigger:
- Model, if LLM-backed:
- Tool allowlist:
- Input paths:
- Output paths:
- Delivery behavior:
- Failure alert behavior:
- Validation command:
- Rollback / disable procedure:
- Privacy boundary:
```

## Public Documentation Redaction Gate

Before publishing docs or PR text, check that it does **not** include:

- Tokens, credentials, API keys, secret names that reveal deployment structure
- User IDs, chat IDs, channel IDs, guild/server IDs, message IDs, phone numbers
- Private hostnames, private absolute paths, local usernames, or deployment topology
- Account balances, private trading data, screenshots, raw private logs
- Exact private timeline details that can fingerprint a deployment

Use generic placeholders instead:

```text
<workspace>
<owner>
<channel-id>
<job-id>
<deployment-specific-model>
```

## Recommended Validation Flow

```bash
openclaw cron list
openclaw memory status --json
openclaw memory search "memory pyramid"
```

For standalone QMD deployments:

```bash
qmd list
```

Then inspect the changed docs:

```bash
git diff --stat
git diff -- README.md references/
```

For public pushes, run a local grep for obvious private identifiers before committing.
