#!/usr/bin/env python3
"""
Memory Pyramid Architecture - Initialization Script (harness-agnostic)

Sets up the four-layer memory directory baseline under an explicit root:
  1. Creates layer directories (topics / daily_reviews / weekly_distills)
  2. Optionally appends the architecture diagram to <root>/MEMORY.md
  3. Prints the cron-job contract (harness-specific installation is documented
     separately; see references/dsh-adapter.md for the DSH recipe)

The memory root must be provided explicitly (--root or MEMORY_PYRAMID_DIR).
We intentionally refuse to guess a default location: silently creating the
baseline in the wrong place is worse than failing loudly.

Usage:
  python3 scripts/init.py --root <memory-root>

Version: 1.1.0
"""

import argparse
import os
from datetime import datetime

VERSION = "1.1.0"

def log(message):
    print(f"[INIT] {message}")

def create_directories(root):
    dirs = [
        os.path.join(root, "topics"),
        os.path.join(root, "daily_reviews"),
        os.path.join(root, "weekly_distills"),
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        log(f"Directory ready: {d}")

ARCHITECTURE_MARKER = "记忆架构图（金字塔模型·夜猫子版）"

def update_memory_md(root):
    """Append the architecture diagram to <root>/MEMORY.md if not present."""
    memory_md = os.path.join(root, "MEMORY.md")
    if not os.path.exists(memory_md):
        log(f"No MEMORY.md at {memory_md} — skipping diagram (create it first if this is the navigation layer).")
        return

    with open(memory_md, "r", encoding="utf-8") as f:
        content = f.read()
    if ARCHITECTURE_MARKER in content:
        log("MEMORY.md already has the pyramid architecture diagram")
        return

    architecture_section = """

---

## 📊 记忆架构图（金字塔模型·夜猫子版）

> 自动生成于: {now}
> 基线定义见仓库 SKILL.md / references/architecture-details.md

```
第一层：导航层
└── MEMORY.md (核心索引)

第二层：知识层（已加工）
├── memory/topics/ (专题记忆)
├── memory/daily_reviews/ (每日精华)
└── memory/weekly_distills/ (每周知识蒸馏)

第三层：结构化日志（半加工）
├── memory/YYYY-MM-DD.md (白天活动 07:00-22:00)
└── memory/YYYY-MM-DD-last-night.md (夜间活动 22:00-07:00)

第四层：原始层（原始记录）
└── 会话原始记录（harness 自有 session 数据；legacy 可选 mirror: memory/realtime-YYYY-MM-DD.md）
```

**Cron时间表**: 07:00 Late Hour Sync → 10/13/16/19/22:00 Micro-Sync → 22:10 Daily Review → 周日 23:55 Weekly Compound
""".format(now=datetime.now().strftime("%Y-%m-%d"))

    with open(memory_md, "a", encoding="utf-8") as f:
        f.write(architecture_section)
    log("Updated MEMORY.md with architecture diagram")

CORE_JOBS = [
    ("Late Hour Sync", "0 7 * * *", "memory/YYYY-MM-DD-last-night.md",
     "把 22:00-07:00 活动按前一晚日期归档"),
    ("Micro-Sync", "0 10,13,16,19,22 * * *", "memory/YYYY-MM-DD.md（追加）",
     "每 3 小时追加有意义的白天活动"),
    ("Daily Review", "10 22 * * *", "memory/daily_reviews/YYYY-MM-DD.md",
     "蒸馏当日洞察"),
    ("Weekly Compound", "55 23 * * 0", "memory/weekly_distills/YYYY-Wxx.md",
     "跨日模式分析"),
]

def print_cron_contract():
    """Print the portable cron contract; harness-specific installation is separate."""
    print("""
Core cron contract (portable baseline — see references/cron-reference.md):

  {jobs}

Installation is harness-specific:
  - OpenClaw: create the jobs with `openclaw cron add` (see references/cron-reference.md).
  - DSH: create the jobs in the DSH cron engine with an explicit model per job
    (see references/dsh-adapter.md).

Every LLM-backed job MUST explicitly specify a model allowed by the local
deployment; never rely on a harness default.
""".format(jobs="\n  ".join(
        f"{name}: {schedule} -> {output} ({purpose})"
        for name, schedule, output, purpose in CORE_JOBS
    )))

def main():
    parser = argparse.ArgumentParser(description="Memory Pyramid baseline initializer (harness-agnostic)")
    parser.add_argument("--root", default=os.environ.get("MEMORY_PYRAMID_DIR"),
                        help="Memory root directory (defaults to $MEMORY_PYRAMID_DIR). "
                             "Required: we refuse to guess a location.")
    args = parser.parse_args()

    if not args.root:
        parser.error("no memory root given. Pass --root <dir> or set MEMORY_PYRAMID_DIR. "
                     "Refusing to guess a default location (creating the baseline in the "
                     "wrong place is worse than failing loudly).")

    root = os.path.abspath(os.path.expanduser(args.root))
    log(f"Initializing Memory Pyramid baseline v{VERSION} at {root}")

    create_directories(root)
    update_memory_md(root)
    print_cron_contract()

    log("Initialization complete.")
    log("Next steps: install the four cron jobs in your harness, then verify with")
    log("  python3 scripts/verify_suite.py && python3 scripts/test_integration.py")

if __name__ == "__main__":
    main()
