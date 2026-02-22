# OpenClaw 记忆金字塔架构

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-blue.svg)](https://openclaw.ai)

> 🏗️ 为 OpenClaw 打造的生产级四层记忆架构，专为夜猫子用户优化（22:00-07:00 活动归属于前一天）。

## ✨ 特性

- 🏗️ **四层金字塔**: 原始数据 → 结构化 → 知识 → 导航
- 🌙 **夜猫子友好**: 深夜活动（22:00-07:00）归属于"昨晚"
- 🔄 **全自动运行**: 6 个 cron 任务零干预
- 📊 **QMD 集成**: 所有层级支持语义搜索
- ⚡ **Token 高效**: 比扁平 RAG 节省 90% tokens

## 🚀 快速开始

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/memory-pyramid-architecture.git

# 进入 skill 目录
cd memory-pyramid-architecture

# 运行初始化
python3 scripts/init.py
```

然后通过 OpenClaw 界面添加 cron 任务。

## 📁 仓库结构

```
memory-pyramid-architecture/
├── SKILL.md                    # Skill 主文档
├── README.md                   # 英文版说明
├── README_ZH.md               # 中文版说明
├── scripts/
│   ├── init.py                # 一键初始化
│   └── config.json            # 配置文件
├── references/                # 详细文档
│   ├── architecture-details.md
│   ├── cron-reference.md
│   └── troubleshooting.md
└── examples/                  # 模板文件
    ├── layer4-raw/
    ├── layer3-structured/
    └── layer2-knowledge/
```

## 🏗️ 架构概览

### 四层金字塔

1. **Layer 4 - Raw (原始层)**
   - 未经处理的原始输入
   - 包含时间戳和来源标记

2. **Layer 3 - Structured (结构化层)**
   - 清洗和格式化
   - 提取关键实体和关系

3. **Layer 2 - Knowledge (知识层)**
   - 语义索引和标签
   - 跨会话关联

4. **Layer 1 - Navigation (导航层)**
   - 高层索引和摘要
   - 快速检索入口

### 夜猫子模式

- 22:00-07:00 (Europe/London) 的活动归属于"昨晚"
- 确保时间线连续性
- 避免日历切割

## 📚 文档

- [架构详解](references/architecture-details.md)
- [Cron 参考](references/cron-reference.md)
- [故障排除](references/troubleshooting.md)

## 🤝 贡献

欢迎贡献！请查看 [贡献指南](CONTRIBUTING.md)。

## �许可证

MIT License - 查看 [LICENSE](LICENSE) 文件。

---

**维护者**: Satoshi & Duoduo  
**语言**: English | 中文
