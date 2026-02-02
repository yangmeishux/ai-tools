# Changelog - AI Tutorial Architect

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**项目**: AI Tutorial Architect
**定位**: 专业的 AI 编程教程架构系统
**原项目**: 基于 ai-agent-team 改造

## [Unreleased]

### Planned
- Agent performance statistics
- Custom agent support
- Interactive quality checklist UI
- Web UI control panel

## [2.2.0] - 2026-01-30

### 🎉 New Feature - AI Content Humanization

Based on research into AI writing patterns and Wikipedia's "Signs of AI writing" guide.

#### Added - New Agent: Humanizer
- **skills/humanizer/SKILL.md** - Complete humanization skill
- **24 AI pattern categories** documented
- **Before/after examples** for each pattern
- **Humanization workflow** integrated into tutorial creation

#### Added - AI Patterns Reference
- **skills/humanizer/ai-patterns-reference.md** - Comprehensive reference
- Detection regex patterns
- Severity classifications
- Quick reference card

#### Changed - Updated Workflows
- **tutorial-workflow/SKILL.md** - Added Humanizer as optional step
- **SKILL.md** - Updated to 11 agents
- **README.md** - Added Humanizer to agent list

#### Added - New Task Classification
- `[task:humanize]` - Quick humanization task
- `[@humanizer]` - Direct agent invocation

### AI Patterns Addressed

1. **Inflated Language** - "pivotal moment", "crucial role"
2. **AI Vocabulary** - "additionally", "landscape", "testament"
3. **Formulaic Structures** - Rule of three, negative parallelisms
4. **Formatting Issues** - Overused em-dashes, title case headings
5. **Chatbot Artifacts** - "I hope this helps", sycophantic tone
6. **Repetition Issues** - Synonym cycling, formulaic challenges

### Usage

```bash
[@humanizer] Remove AI patterns from this tutorial
[task:humanize] Make this content sound more natural
```

## [2.1.0] - 2026-01-30

### 🎉 Major Refactoring - Professional Architecture

Based on [superpowers](https://github.com/obra/superpowers) architecture patterns, completely restructured for professional use.

#### Added - Plugin System
- `.claude-plugin/plugin.json` - Claude Code plugin configuration
- `.claude-plugin/marketplace.json` - Marketplace metadata
- Support for `/plugin install` workflow

#### Added - Modular Skill Structure
Each agent now has its own skill directory following superpowers conventions:
- `skills/chief/SKILL.md` - Project coordination
- `skills/researcher/SKILL.md` - Information gathering  
- `skills/writer/SKILL.md` - Content creation
- `skills/editor/SKILL.md` - Content refinement
- `skills/fact-checker/SKILL.md` - Accuracy validation
- `skills/archivist/SKILL.md` - Knowledge management
- `skills/educator/SKILL.md` - Learning design
- `skills/practitioner/SKILL.md` - Code validation
- `skills/learner-advocate/SKILL.md` - Beginner perspective
- `skills/version-archivist/SKILL.md` - Version tracking
- `skills/tutorial-workflow/SKILL.md` - Workflow definitions
- `skills/quality-assurance/SKILL.md` - Quality framework

#### Added - Command System
- `commands/tutorial-create.md` - Full tutorial creation
- `commands/tutorial-verify.md` - Quality verification
- `commands/code-validate.md` - Code validation

#### Added - Agent Definitions
- `agents/code-reviewer.md` - Code review agent

#### Added - Documentation
- `docs/ARCHITECTURE.md` - System architecture
- `docs/INSTALLATION.md` - Installation guide

#### Changed - Skill Format
- Adopted superpowers YAML frontmatter style
- Name and description only in frontmatter
- Focus on "Use when..." trigger conditions
- Graphviz flowcharts for decision points
- Token-efficient, focused content

#### Changed - Main SKILL.md
- Rewritten following superpowers patterns
- Clearer agent selection guidance
- Workflow visualization
- Quality framework documentation

#### Changed - README.md
- Updated for new architecture
- Installation via plugin marketplace
- Clearer quick start
- Professional presentation

## [2.0.0] - 2026-01-28

### 🎉 Major Release - AI Programming Tutorial Specialization

#### Added - 新增 4 个 AI 编程教程专用 Agent

- 🎓 **Educator（技术教育专家）**
  - 学习路径设计和难度梯度把控
  - 将复杂技术概念转化为可学习的内容
  - 识别认知障碍并提供解决策略
  - 确保内容的实践性和可操作性

- 🧪 **Practitioner（代码实战验证者）**
  - 验证代码示例的可运行性和可复现性
  - 测试环境配置的完整性
  - 检查依赖和版本兼容性
  - 识别和标注常见错误和陷阱

- 👤 **Learner-Advocate（读者代表/初学者视角）**
  - 从初学者角度审查内容
  - 识别可能的困惑点和认知障碍
  - 确保术语有充分解释
  - 检查是否有跳跃式推理或隐含假设

- 📋 **Version-Archivist（版本追踪者）**
  - 记录代码和环境的版本信息
  - 追踪 API 变更和弃用情况
  - 标注不同版本的兼容性和差异
  - 维护更新日志和迁移指南

#### Added - 教程专用任务分类系统

- **tutorial** - 完整教程创作，注重可运行性、易懂性、渐进性
- **concept-guide** - 深入概念讲解，注重准确性、深度、类比
- **quick-start** - 快速上手指南，注重简洁性、成功率、速度
- **best-practice** - 最佳实践总结，注重专业性、规范性、陷阱提示

#### Added - 8 维质量评估体系

1. **可运行性**（Runnability）- 代码经过实际测试验证
2. **环境完整性**（Environment Completeness）- 完整的环境配置说明
3. **渐进性**（Progressiveness）- 合理的难度梯度设计
4. **术语解释**（Term Explanation）- 充分的术语解释和类比
5. **错误处理**（Error Handling）- 常见错误和坑点标注
6. **版本明确**（Version Clarity）- 明确的版本信息标注
7. **实际价值**（Practical Value）- 解决真实世界问题
8. **可复现性**（Reproducibility）- 清晰可重复的步骤

#### Added - AI 编程教程工作流程

- 新增"AI 编程教程创作流程"（推荐流程）
- 建立反馈闭环机制（验证→修正→再验证）
- 集成教学设计前置环节
- 添加代码验证和读者视角审查步骤

#### Added - 示例场景

- 新增场景 4：创建 AI 编程教程（完整示例）
- 展示 4 个新角色的协作方式
- 对比通用内容创作与教程创作的差异
- 提供质量等级标准（金/银/铜牌）

#### Changed - 优化现有功能

- 重构任务分类系统，分为"通用"和"教程专用"两大类
- 优化工作流程说明，突出关键环节
- 更新快速参考文档，添加新角色和使用方式
- 改进 README.md，突出 AI 编程教程特殊支持

#### Documentation Updates

- ✅ SKILL.md - 完整更新所有 Agent 和工作流程
- ✅ QUICK_REFERENCE.md - 添加新角色和教程场景
- ✅ README.md - 更新为核心功能说明
- ✅ 新增"AI 编程教程质量标准"章节
- ✅ 优化所有示例和场景说明

#### Breaking Changes - 重大变更

⚠️ **注意**：从 v1.x 升级到 v2.0 需要注意：

1. Agent 数量从 6 个增加到 10 个
2. 新增 4 个教程专用任务类别
3. 推荐使用新的 AI 编程教程工作流程
4. 质量标准从通用评估升级为 8 维评估体系

**升级建议**：
- 对于 AI 编程教程任务，强烈建议使用新流程
- 对于通用内容创作，旧流程依然完全兼容
- 所有旧的使用方式继续支持，无破坏性变更

---

## [1.0.0] - 2026-01-15

### Added
- 🎭 **6 Core Agents**: Chief, Researcher, Writer, Editor, Fact-Checker, Archivist
- 🔄 **3 Usage Modes**: Chief coordination, direct Agent invocation, task categorization
- 📚 **Complete Workflows**: Standard content creation, research analysis, knowledge management
- ✅ **Quality Assurance**: Multi-layer verification and validation mechanisms
- 📖 **Comprehensive Documentation**:
  - Detailed README with badges and examples
  - Quick reference guide
  - Contributing guidelines
  - Installation instructions
- 🔗 **SKILL Integration**: Native Claude Code SKILL support
- 🎨 **Professional Design**: Well-structured and documented codebase
- 🚀 **CI/CD**: GitHub Actions for continuous integration
- 📝 **Templates**: Issue and PR templates
- 🌟 **MIT License**: Open source licensing

### Changed
- Optimized Agent coordination logic
- Improved documentation structure
- Enhanced error handling

### Fixed
- Initial release - no known issues

---

## [0.1.0] - 2026-01-14 (Initial Development)

### Added
- Basic Agent framework
- Core Agent roles
- Simple workflow system
- Initial documentation

---

## Version Summary

| Version | Date | Description |
|---------|------|-------------|
| 2.0.0 | 2026-01-28 | ⭐ AI 编程教程专业化，新增 4 个专用 Agent |
| 1.0.0 | 2026-01-15 | 🎉 First stable release |
| 0.1.0 | 2026-01-14 | 🚧 Initial development version |

---

## Release Types

- **Major** (X.0.0): Breaking changes, major features
- **Minor** (1.X.0): New features, backward compatible
- **Patch** (1.0.X): Bug fixes, minor improvements

---

## Links

- [GitHub Releases](https://github.com/yangmeishux/ai-tools/releases)
- [GitHub Tags](https://github.com/yangmeishux/ai-tools/tags)
- [Milestones](https://github.com/yangmeishux/ai-tools/milestones)

---

**Note**: This project follows [Semantic Versioning](https://semver.org/).
