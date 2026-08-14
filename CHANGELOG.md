# Changelog

All notable changes to Memory Pyramid Architecture are documented here.

The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project uses semantic versioning for public documentation releases.

## [1.2.0] - 2026-08-14

### Added

- Added `references/dsh-adapter.md`: deployment mapping for DeepSeek Harness (cron engine requirements, session-record extraction, glob context, append output, previous-date naming, retrieval mapping, validation checklist).
- Added a harness self-heal convention: cron jobs that depend on newer engine capabilities can be marked `awaitingEngineUpgrade` and are auto-enabled after the engine restarts (documented as a general pattern for any harness cron engine).

### Changed

- Rewrote `scripts/init.py` as harness-agnostic: creates layer directories (`topics/`, `daily_reviews/`, `weekly_distills/`) and optionally the MEMORY.md diagram under an explicit `--root` (or `MEMORY_PYRAMID_DIR`); removed hardcoded `~/.openclaw/workspace` layout, `openclaw.json` QMD injection, and `openclaw cron`/`qmd` CLI calls. The script now refuses to guess a default location.
- Deprecated `qmd_collections` in `scripts/config.json` (OpenClaw/QMD-specific; non-OpenClaw deployments use plain-file retrieval via `retrieval_priority`).
- Generalized the raw-source layer to harness-native session records (OpenClaw transcripts, DSH session jsonl, etc.).
- Updated README / README_EN / README_ZH / SKILL.md / PACKAGE.md with harness-adapter terminology, version 1.2.0, and the new init usage.

## [1.1.0] - 2026-05-07

### Added

- Added `references/production-overlay.md` to explain the boundary between the portable baseline and local production overlays.
- Added production-overlay documentation for live status, session transcript indexing, short-term recall promotion, dreaming/REM candidate generation, KB Gardener, and skill/evolver boundaries.
- Added modern validation guidance using `openclaw memory status --json` and `openclaw memory search`.
- Added privacy/redaction guidance for public documentation and repository sync.

### Changed

- Clarified that the repository is the reusable **baseline contract**, while mature OpenClaw deployments may add optional overlays.
- Updated the raw-source layer to prefer OpenClaw session transcripts / memory index, with `memory/realtime-YYYY-MM-DD.md` treated as an optional legacy/raw mirror.
- Reframed automation as four core jobs: Late Hour Sync, Micro-Sync, Daily Review, and Weekly Compound.
- Updated README, English/Chinese README variants, SKILL.md, package summary, architecture details, and cron reference to use consistent baseline/overlay terminology.
- Made the integration test repository-relative instead of depending on a local absolute path.

### Security

- Removed private/local path assumptions from the integration test.
- Sanitized public examples and troubleshooting text to avoid channel/provider-specific private deployment details.

## [1.0.0] - 2026-02-17

### Added

- Initial four-layer Memory Pyramid architecture for OpenClaw.
- Night-owl boundary: 22:00-07:00 activity belongs to the previous night.
- Core memory layers: navigation, knowledge, structured logs, and raw sources.
- Initial cron workflow docs for real-time/raw capture, Micro-Sync, Late Hour Sync, Daily Review, Weekly Compound, and QMD health checks.
- Initial examples, troubleshooting guide, and setup script.
