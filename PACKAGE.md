# Memory Pyramid Architecture Skill - Summary

**Current version: 1.1.0**

See [CHANGELOG.md](CHANGELOG.md) for release history.

## 📦 Package Contents

```text
memory-pyramid-architecture/
├── SKILL.md                           # Main skill documentation
├── README.md                          # Quick start guide
├── VERSION                            # Current release version
├── CHANGELOG.md                       # Release history
├── package.json                       # npm-style script entrypoints
├── .github/workflows/ci.yml           # GitHub Actions verification
├── README_EN.md / README_ZH.md        # Language variants
├── README_LOCAL.md                    # Local deployment notes
├── scripts/
│   ├── init.py                        # Setup / verification helper
│   ├── config.json                    # Baseline layer and cron config
│   ├── verify_suite.py                # Python compile + integration checks
│   ├── hygiene_scan.py                # Hygiene and secret-pattern scan
│   ├── sync_drift_check.py            # Version/docs/CI drift check
│   ├── test_integration.py            # Smoke test
│   └── visualize.py                   # Flow diagram helper
├── references/
│   ├── architecture-details.md        # Deep dive into design
│   ├── cron-reference.md              # Core and optional cron guidance
│   ├── production-overlay.md          # Production overlay and privacy boundary
│   ├── kb-gardener-workflow-v0.1.md   # Optional knowledge-base overlay
│   ├── topic-routing-policy-v0.1.md   # Topic routing policy
│   ├── topic-scope-template.md        # Topic contract template
│   └── troubleshooting.md             # Common issues and fixes
└── examples/
    ├── README.md                      # Examples overview
    ├── layer4-raw/                    # Raw-source example
    ├── layer3-structured/             # Day and night log examples
    └── layer2-knowledge/              # Daily and weekly review examples
```

## 🚀 Quick Installation

```bash
python3 scripts/init.py
python3 scripts/verify_suite.py
python3 scripts/hygiene_scan.py
python3 scripts/sync_drift_check.py
```

Then verify cron jobs and memory indexing in the target OpenClaw environment.

## ✨ Key Features

1. **Four-layer baseline** - Raw → structured → knowledge → navigation
2. **Night-owl optimization** - 22:00-07:00 activity belongs to the previous night
3. **Core automation** - Late Hour Sync, Micro-Sync, Daily Review, Weekly Compound
4. **Token efficient** - distilled-first retrieval, raw expansion only when needed
5. **Production-overlay friendly** - live status, session indexing, promotion, dreaming, KB gardening, and skill/evolver governance stay optional
6. **Privacy-aware public docs** - avoid private deployment identifiers in reusable documentation

## 🎯 Use Cases

1. **Personal OpenClaw memory** - keep long-running work searchable and distilled
2. **Team deployment** - standardize memory layers and cron schedules
3. **Community sharing** - contribute reusable docs and examples
4. **Fork and customize** - add local production overlays safely

## 🤝 Contributing

Ways to contribute:

1. Report bugs via the OpenClaw community
2. Suggest enhancements
3. Share sanitized customizations
4. Improve documentation
5. Add new generic features such as multi-timezone support or visualization

Before publishing, confirm the diff does not contain tokens, user IDs, channel IDs, private hostnames, private absolute paths, or raw private logs.

## 📚 Documentation Index

- **Start here**: README.md
- **How to use**: SKILL.md
- **Deep dive**: references/architecture-details.md
- **Cron jobs**: references/cron-reference.md
- **Production overlays**: references/production-overlay.md
- **Fix problems**: references/troubleshooting.md
- **See examples**: examples/

## 🔗 Related Resources

- OpenViking: https://github.com/volcengine/OpenViking
- OpenClaw docs: https://docs.openclaw.ai

---

**Ready to use.** Install with `scripts/init.py` and keep production overlays documented separately.
