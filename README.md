![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-知乎%20%7C%20公众号%20%7C%20小红书%20%7C%20微博-orange.svg)

<div align="center">

# 🎯 零AI痕迹写作系统

**面向中文自媒体的"去AI味"写作方法论与工具集**

覆盖知乎、微信公众号、小红书、微博四大主流平台

</div>

---

## 📖 项目简介

一套完整的零AI痕迹写作方法论与实战工具，帮助创作者写出有人味、能过审、有真实感的文章。核心是**4层改写法**——不是简单换词，而是从根本上换掉AI的写作思维。

### ✨ 核心价值

- 🧠 **思维换道**：打破AI的"总-分-总"，用人类的"踩坑→发现→验证"叙事
- 🚫 **词库过滤**：300+ AI高频词黑名单，自动扫描标记
- 📝 **模板赋能**：四大平台文章骨架模板，直接套用
- 🔍 **实战案例**：Before/After对照展示，直观感受差异
- 🛠️ **工具加持**：Python自动扫描脚本，一键检测AI痕迹
- 💡 **持续迭代**：不断更新的创作规范与方法论

---

## 🌟 功能特性

### 核心方法论
- 🎯 **4层改写法**：结构层 → 例子层 → 语气层 → 删减层
- 📊 **AI痕迹检测**：300+高频词黑名单自动扫描
- 💬 **口语化转换**：100+正式表达→口语化替换
- 🧩 **平台模板**：知乎/公众号/小红书/微博四大平台专属模板

### 平台覆盖
| 平台 | 创作规范 | 模板支持 | 要点指南 |
|------|----------|----------|----------|
| 知乎 | ✅ | ✅ | ✅ |
| 微信公众号 | ✅ | ✅ | ✅ |
| 小红书 | ✅ | ✅ | ✅ |
| 微博 | ✅ | ✅ | ✅ |

---

## 🚀 快速开始

### 方法一：直接阅读方法论
从 `skill.md` 开始，了解完整的零AI痕迹写作方法论。

### 方法二：使用扫描工具
```bash
# 克隆项目
git clone https://github.com/ymstar/zero-ai-trace-writing.git
cd zero-ai-trace-writing

# 扫描你的文章
python3 scripts/blacklist-scanner.py your-article.md
```

### 方法三：套用平台模板
直接使用 `references/templates.md` 中的平台模板，快速构建文章骨架。

---

## 📂 文档目录

| 文件 | 说明 |
|------|------|
| `skill.md` | 技能完整说明（总览） |
| `references/methodology-upgrade.md` | 4层改写方法论详解 |
| `references/zhihu-creation-guide.md` | 知乎创作规范手册 |
| `references/wechat-creation-guide.md` | 公众号创作规范手册 |
| `references/xiaohongshu-creation-guide.md` | 小红书创作规范手册 |
| `references/weibo-creation-guide.md` | 微博创作规范手册 |
| `references/templates.md` | 四平台文章骨架模板 |
| `references/before-after-examples.md` | 实战案例对照（Before/After） |
| `references/word-blacklist.md` | AI高频词黑名单（300+词） |
| `references/colloquial-replacements.md` | 口语化替换词库（100+组） |
| `scripts/blacklist-scanner.py` | 黑名单自动扫描脚本 |

---

## 🧩 核心方法论：4层改写法

不是换词，是换思维：

| 层级 | 目标 | 具体方法 |
|------|------|----------|
| **结构层** | 打破AI的"总-分-总"僵化结构 | 改用"踩坑→发现→验证"的人类叙事逻辑 |
| **例子层** | 删除AI的假大空举例 | 换成真实经历、可验证事实、具体数据 |
| **语气层** | 去除官腔、套话、空话 | 第一人称、明确立场、口语化表达 |
| **删减层** | 砍掉所有不增加信息量的句子 | "至关重要""总而言之"等通通删掉 |

> 💡 **核心理念**：AI写作的本质问题不是词，是思维模式。人类写作是"探索式"的——我有一个问题，我解决了，我告诉你；AI写作是"演示式"的——我有一个结论，我证明给你看。

---

## 🛠️ 工具使用

### AI高频词扫描器

```bash
# 基础扫描
python3 scripts/blacklist-scanner.py your-article.md

# 带详细定位
python3 scripts/blacklist-scanner.py your-article.md -v

# 指定自定义黑名单
python3 scripts/blacklist-scanner.py your-article.md -b my-blacklist.txt
```

### 扫描示例输出
```
📊 扫描结果
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
总计检测：1284 词
AI 高频词：3 个
风险等级：🟡 中等

⚠️ 标记词汇：
   L10  至关重要  → 建议改为"关键在于""核心是"
   L25  总而言之  → 建议改为"说白了""一句话总结"
   L42  深入探讨  → 建议改为"深挖一下""仔细聊聊"

💡 提示：AI痕迹 ≠ 不能用，关键是"自然度"和"真实性"
```

---

## 🌐 虾评Skill

本技能已发布在虾评Skill平台，可以直接在扣子(Coze)中导入使用：

👉 [零AI痕迹写作 - 虾评Skill](https://xiaping.coze.site/skill/2b1b3774-4032-437b-bcfd-606e4d53e548)

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE)

---

## 💬 交流与反馈

- 提交 Issue：欢迎提出问题和改进建议
- Star 支持：如果对你有帮助，点个 Star 支持一下
- 贡献代码：欢迎提交 PR 共同完善

---

<div align="center">

**用人类的方式写，写给人类看** ✨

</div>
