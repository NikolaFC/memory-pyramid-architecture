# Example Memory Files

This directory contains example files showing the expected format for each layer.

## File Structure

```
examples/
├── layer4-raw/                  # Raw conversation logs
│   └── realtime-2026-02-17.md
├── layer3-structured/           # Structured activity logs
│   ├── 2026-02-17.md           # Daytime activities
│   └── 2026-02-16-last-night.md # Night activities
├── layer2-knowledge/            # Distilled insights
│   ├── daily_reviews/
│   │   └── 2026-02-17.md
│   └── weekly_distills/
│       └── 2026-W07.md
└── layer1-navigation/           # Quick index
    └── MEMORY.md.example
```

## Usage

These examples serve as:
1. **Templates** for manual creation
2. **Tests** to verify format compliance
3. **Documentation** of expected structure

## Notes

- Examples use fictional data
- Timestamps are illustrative
- Real files would be longer
