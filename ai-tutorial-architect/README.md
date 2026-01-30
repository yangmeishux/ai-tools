# 🎓 AI Tutorial Architect

[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple?style=flat-square&logo=anthropic)](https://claude.com/claude-code)
[![Version](https://img.shields.io/badge/Version-2.2.0-blue?style=flat-square)]()
[![Quality](https://img.shields.io/badge/Quality-Gold%20Standard-yellow?style=flat-square)]()

**Professional AI programming tutorial creation system with 11 specialized agents and 8-dimensional quality assessment. Now with AI content humanization for natural, engaging prose.**

Based on [superpowers](https://github.com/obra/superpowers) architecture and [newtype-profile](https://github.com/newtype-01/newtype-profile) agent coordination patterns.

---

## ✨ What Makes It Different?

Traditional tutorial creation vs AI Tutorial Architect:

| Aspect | Traditional | AI Tutorial Architect |
|--------|-------------|----------------------|
| Code examples | "Should work" | ✅ Verified executable |
| Beginner-friendly | Assumes knowledge | ✅ Cognitive barriers identified |
| Version info | Often missing | ✅ Compatibility documented |
| Quality | Subjective | ✅ 8-dimensional assessment |
| Creation process | Single author | ✅ 11 expert perspectives |

---

## 🚀 Quick Start

### Installation

```bash
# Via Claude Code marketplace
/plugin marketplace add yangmeishux/ai-tutorial-architect
/plugin install ai-tutorial-architect

# Or manual
cd ~/.claude/skills
git clone https://github.com/yangmeishux/ai-tools.git ai-tutorial-architect
```

### Create Your First Tutorial

```bash
# Let Chief coordinate the team
> [Chief] Create a Python asyncio tutorial for intermediate developers

# Or use task classification
> [task:tutorial] Create a React Hooks complete guide
```

---

## 🎭 The 11 Agents

### Core Team

| Agent | Role | When to Invoke |
|-------|------|----------------|
| **Chief** | Project coordinator | `[Chief] Plan this project` |
| **Researcher** | Information gatherer | `[@researcher] Research topic` |
| **Writer** | Content creator | `[@writer] Draft content` |
| **Editor** | Content refiner | `[@editor] Polish this` |
| **Fact-Checker** | Accuracy validator | `[@fact-checker] Verify claims` |
| **Archivist** | Knowledge manager | `[@archivist] Find related docs` |

### Tutorial Specialists

| Agent | Specialty | When to Invoke |
|-------|-----------|----------------|
| **Educator** | Learning design | `[@educator] Design learning path` |
| **Practitioner** | Code validation | `[@practitioner] Verify code runs` |
| **Learner-Advocate** | Beginner voice | `[@learner-advocate] Check clarity` |
| **Version-Archivist** | Compatibility | `[@version-archivist] Document versions` |

### Content Enhancement ✨ (NEW)

| Agent | Specialty | When to Invoke |
|-------|-----------|----------------|
| **Humanizer** | AI content humanizer | `[@humanizer] Remove AI patterns` |

---

## 🔄 Workflows

### Full Tutorial (Gold Standard)

```
Chief → Researcher/Archivist → Educator → Writer → 
Practitioner → Learner-Advocate → Editor → [Humanizer] →
Version-Archivist → Fact-Checker → Chief
```

**Time:** 6-9 hours (with humanization)  
**Output:** Production-ready tutorial with natural tone

### Quick Start

```
Chief → Writer → Practitioner → Editor → Chief
```

**Time:** 2-3 hours  
**Output:** Working tutorial

### Available Commands

| Command | Purpose |
|---------|---------|
| `/tutorial:create` | Full creation workflow |
| `/tutorial:verify` | 8-dimension quality check |
| `/code:validate` | Execute code examples |

---

## 📊 8-Dimensional Quality

| Dimension | Checked By | Description |
|-----------|------------|-------------|
| **Runnability** | Practitioner | Every example executes |
| **Environment** | Practitioner | Setup fully documented |
| **Progressiveness** | Educator | Appropriate difficulty curve |
| **Term Explanation** | Learner-Advocate | Terms defined on first use |
| **Error Handling** | Practitioner + Learner-Advocate | Common errors covered |
| **Version Clarity** | Version-Archivist | Versions specified |
| **Practical Value** | Educator + Practitioner | Solves real problems |
| **Reproducibility** | Practitioner + Learner-Advocate | Steps clearly defined |

**Quality Levels:**
- 🥇 Gold: 8/8 dimensions
- 🥈 Silver: 6-7/8 dimensions  
- 🥉 Bronze: 4-5/8 dimensions

---

## 💡 Usage Examples

### Example 1: Complete Tutorial

```bash
> [Chief] Create a "Python Type Hints" tutorial for developers
>     transitioning from JavaScript
```

**Process:**
1. Researcher explores Type Hints ecosystem
2. Archivist finds related typing tutorials
3. Educator designs JS → Python mental model
4. Writer creates content with examples
5. Practitioner verifies all code runs
6. Learner-Advocate checks JS dev perspective
7. Editor polishes structure
8. Version-Archivist documents Python versions
9. Fact-Checker verifies type system claims
10. Chief integrates and delivers

### Example 2: Quick Guide

```bash
> [@writer] Write a Docker setup guide
> [@practitioner] Verify the steps work
> [@editor] Polish and format
```

**Time:** 1 hour

### Example 3: Quality Check

```bash
> /tutorial:verify ./my-tutorial.md
```

**Output:** Quality report with improvement suggestions

---

## 📁 Project Structure

```
ai-tutorial-architect/
├── .claude-plugin/      # Plugin configuration
├── skills/              # Agent skill definitions
│   ├── chief/
│   ├── researcher/
│   ├── writer/
│   ├── editor/
│   ├── fact-checker/
│   ├── archivist/
│   ├── educator/        # Tutorial specialist
│   ├── practitioner/    # Tutorial specialist
│   ├── learner-advocate/# Tutorial specialist
│   ├── version-archivist/# Tutorial specialist
│   ├── tutorial-workflow/
│   └── quality-assurance/
├── commands/            # CLI commands
├── agents/              # Agent definitions
├── docs/                # Documentation
├── SKILL.md             # Entry point
└── README.md            # This file
```

---

## 🔗 Inspired By

- **[superpowers](https://github.com/obra/superpowers)** - Multi-agent workflow architecture
- **[newtype-profile](https://github.com/newtype-01/newtype-profile)** - Agent team coordination model

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file.

---

<div align="center">

**Made with ❤️ for better technical education**

[⬆ Back to Top](#-ai-tutorial-architect)

</div>
