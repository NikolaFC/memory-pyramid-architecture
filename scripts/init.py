#!/usr/bin/env python3
"""
Memory Pyramid Architecture - Initialization Script

Sets up the complete four-layer memory architecture:
1. Creates required directories
2. Updates MEMORY.md with architecture diagram
3. Configures QMD collections in openclaw.json
4. Installs cron jobs with proper scheduling

Author: OpenClaw Community
Version: 1.0.0
"""

import os
import json
import subprocess
from datetime import datetime

WORKSPACE = os.path.expanduser("~/.openclaw/workspace")
MEMORY_DIR = f"{WORKSPACE}/memory"
CONFIG_FILE = f"{WORKSPACE}/skills/memory-pyramid-architecture/scripts/config.json"

def log(message):
    print(f"[INIT] {message}")

def create_directories():
    """Create required memory directories"""
    dirs = [
        f"{MEMORY_DIR}/daily_reviews",
        f"{MEMORY_DIR}/weekly_distills",
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        log(f"Created directory: {d}")

def update_memory_md():
    """Add architecture diagram to MEMORY.md if not present"""
    memory_md = f"{WORKSPACE}/MEMORY.md"
    
    # Check if already has pyramid architecture
    with open(memory_md, 'r', encoding='utf-8') as f:
        content = f.read()
        if "记忆架构图（金字塔模型·夜猫子版）" in content:
            log("MEMORY.md already has pyramid architecture diagram")
            return
    
    # Append architecture section
    architecture_section = """

---

## 📊 记忆架构图（金字塔模型·夜猫子版）

> 自动生成于: {datetime.now().strftime('%Y-%m-%d')}
> 详见: `docs/guides/memory-architecture-workflow.md`

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
└── memory/realtime-YYYY-MM-DD.md (每分钟实时同步)
```

**Cron时间表**: 07:00 Late Hour Sync → 10/13/16/19/22:00 Micro-Sync → 22:10 Daily Review
""".format(datetime=datetime)
    
    with open(memory_md, 'a', encoding='utf-8') as f:
        f.write(architecture_section)
    
    log("Updated MEMORY.md with architecture diagram")

def configure_qmd():
    """Add QMD collections to openclaw.json"""
    openclaw_json = os.path.expanduser("~/.openclaw/openclaw.json")
    
    with open(openclaw_json, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # Check if already configured
    existing_names = [p.get('name') for p in config.get('memory', {}).get('qmd', {}).get('paths', [])]
    
    new_paths = [
        {
            "path": "./memory/daily_reviews",
            "name": "memory-daily-reviews",
            "pattern": "*.md"
        },
        {
            "path": "./memory/weekly_distills",
            "name": "memory-weekly-distills",
            "pattern": "*.md"
        },
        {
            "path": "./memory",
            "name": "memory-late-night",
            "pattern": "*-last-night.md"
        }
    ]
    
    added = []
    for path_config in new_paths:
        if path_config['name'] not in existing_names:
            config['memory']['qmd']['paths'].insert(4, path_config)  # Insert after topics
            added.append(path_config['name'])
    
    if added:
        with open(openclaw_json, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        log(f"Added QMD collections: {', '.join(added)}")
    else:
        log("QMD collections already configured")

def install_crons():
    """Install required cron jobs (manual step - show instructions)"""
    log("Cron installation instructions:")
    print("""
The following cron jobs need to be added via 'openclaw cron add':

1. Late Hour Sync (07:00 daily)
   Schedule: 0 7 * * *
   Purpose: Archive night activities (22:00-07:00)
   Output: memory/YYYY-MM-DD-last-night.md

2. Hourly Micro-Sync (10,13,16,19,22:00 daily)
   Schedule: 0 10,13,16,19,22 * * *
   Purpose: Extract important activities every 3 hours
   Output: memory/YYYY-MM-DD.md

3. Daily Review (22:10 daily)
   Schedule: 10 22 * * *
   Purpose: Distill daily insights
   Output: memory/daily_reviews/YYYY-MM-DD.md

4. Weekly Memory Compound (Sun 23:55)
   Schedule: 55 23 * * 0
   Purpose: Cross-day pattern analysis
   Output: memory/weekly_distills/YYYY-WXX.md

Run 'openclaw cron list' to check existing jobs.
""")

def main():
    log("Initializing Memory Pyramid Architecture...")
    
    create_directories()
    update_memory_md()
    configure_qmd()
    install_crons()
    
    log("Initialization complete!")
    log("Next steps:")
    log("1. Run 'qmd update && qmd embed' to index new collections")
    log("2. Add cron jobs manually via 'openclaw cron add'")
    log("3. Read SKILL.md for detailed usage instructions")

if __name__ == "__main__":
    main()
