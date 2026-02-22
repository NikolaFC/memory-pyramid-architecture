#!/usr/bin/env python3
"""
Memory Pyramid Visualization Tool
Generates Mermaid diagram for memory flow visualization
"""

DIAGRAM = """# Memory Pyramid Architecture - Flow Diagram

```mermaid
graph TD
    subgraph "Layer 4: Raw"
        R1[User Input]
        R2[Session Transcripts]
        R3[System Logs]
    end

    subgraph "Layer 3: Structured"
        S1[Entity Extraction]
        S2[Time Ordering]
        S3[Relation Mapping]
    end

    subgraph "Layer 2: Knowledge"
        K1[Semantic Indexing]
        K2[Tagging]
        K3[Cross-Session Links]
    end

    subgraph "Layer 1: Navigation"
        N1[High-Level Index]
        N2[Summaries]
        N3[Quick Access]
    end

    R1 --> S1
    R2 --> S2
    R3 --> S3
    S1 --> K1
    S2 --> K2
    S3 --> K3
    K1 --> N1
    K2 --> N2
    K3 --> N3

    style R1 fill:#f9f,stroke:#333
    style N1 fill:#bbf,stroke:#333
```

## Layer Descriptions

| Layer | Function | Key Operations |
|-------|----------|----------------|
| Raw | Original input capture | Timestamp, source tagging |
| Structured | Data cleaning | Entity extraction, deduplication |
| Knowledge | Semantic organization | Indexing, tagging, linking |
| Navigation | Quick access | Summaries, indices, search |

## Night-Owl Mode

- Activities between 22:00-07:00 (Europe/London) belong to "last night"
- Ensures timeline continuity
- Prevents calendar-based fragmentation
"""

if __name__ == '__main__':
    print(DIAGRAM)
