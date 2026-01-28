# AI Tutorial Architect - 快速参考

专业的 AI 编程教程架构系统，快速上手指南

## 🎯 三种使用方式

### 1. 让主编协调（推荐用于复杂任务）
```
[Chief] 我需要写一篇深度分析文章
```

### 2. 指定 Agent（推荐用于单一任务）
```
[@researcher] 研究 AI 趋势
[@writer] 撰写文章
[@editor] 优化内容
[@fact-checker] 验证数据
[@archivist] 查找文档
[@educator] 设计学习路径
[@practitioner] 验证代码可运行性
[@learner-advocate] 从初学者角度审查
[@version-archivist] 标注版本信息
```

### 3. 任务分类（快速模式）
```
[task:research] 调研主题
[task:writing] 撰写内容
[task:editing] 优化结构
[task:fact-check] 验证事实
[task:tutorial] 创建完整教程
[task:concept-guide] 深入讲解概念
[task:quick-start] 快速上手指南
[task:best-practice] 最佳实践总结
```

---

## 👥 Agent 速查表

### 基础角色
| Agent | 角色 | 一句话描述 |
|-------|------|-----------|
| **Chief** | 主编 | 协调团队，分解任务，整合输出 |
| **Researcher** | 研究员 | 收集信息，调研趋势，提供资料 |
| **Writer** | 作者 | 创作内容，撰写文章，生成文案 |
| **Editor** | 编辑 | 优化结构，精炼语言，提升质量 |
| **Fact-Checker** | 核查员 | 验证事实，检查数据，确保准确 |
| **Archivist** | 档案员 | 检索知识，查找文档，建立关联 |

### AI 编程教程专用角色 ⭐
| Agent | 角色 | 一句话描述 |
|-------|------|-----------|
| **Educator** | 技术教育专家 | 设计学习路径，将技术转化为可学习内容 |
| **Practitioner** | 代码实战验证者 | 验证代码可运行性，测试环境配置 |
| **Learner-Advocate** | 读者代表 | 从初学者角度审查，识别困惑点 |
| **Version-Archivist** | 版本追踪者 | 标注版本信息，追踪 API 变更 |

---

## 🔄 标准工作流程

### 内容创作（通用）
```
Chief 规划 → Researcher 研究 → Writer 创作 → Editor 优化 → Fact-Checker 验证 → Chief 审核
```

### AI 编程教程（推荐）⭐
```
Chief 规划 → Researcher 调研 → Educator 设计 → Writer 创作
→ Practitioner 验证 → Learner-Advocate 审查 → Editor 优化
→ Version-Archivist 标注版本 → Fact-Checker 验证 → Chief 审核
```

### 研究分析
```
Chief 定义 → Researcher 调研 → Archivist 补充 → Fact-Checker 验证 → Writer 撰写 → Editor 整理
```

### 快速模式
```
Chief → Researcher (15分钟) → Writer (30分钟) → Editor (15分钟) → Chief 输出
```

---

## 💬 常用命令示例

### 内容创作类
```
[Chief] 写一篇关于 AI 的技术博客
[@writer] 基于研究结果写文章
[@editor] 审查并优化这篇文章
```

### 研究分析类
```
[@researcher] 调研区块链应用场景
[Chief] 分析市场前景并给出建议
[@fact-checker] 验证这些数据的准确性
```

### 知识管理类
```
[@archivist] 查找相关历史文档
[Chief] 建立知识库并整理分类
```

### 质量控制类
```
[@fact-checker] 检查所有引用和数据
[Chief] 启动三轮质量审查
```

---

## 🚀 高级功能

### 并行处理
```
[Chief] 并行执行：
      - Researcher 研究市场
      - Archivist 分析历史数据
      - Fact-Checker 验证来源
```

### 迭代优化
```
[Chief] 三轮迭代：
      Round 1: Writer 起草
      Round 2: Editor 深度优化
      Round 3: Fact-Checker 全面验证
```

### 质量检查点
```
[Chief] 设置检查点：
      ✓ 研究阶段
      ✓ 创作阶段
      ✓ 编辑阶段
      ✓ 最终阶段
```

---

## ⚡ 快速决策树

```
你的任务是什么？
│
├─ 简单单一任务？
│  └─ 直接指定对应 Agent [@agent-name]
│
├─ 复杂多步骤任务？
│  └─ 使用 [Chief] 协调团队
│
└─ 不确定？
   └─ 使用 [task:category] 自动分类
```

---

## 🎨 场景速查

### 通用场景
| 场景 | 使用方式 |
|------|---------|
| 写技术博客 | `[Chief] 写一篇关于 X 的技术博客` |
| 市场分析 | `[Chief] 分析 X 市场的发展前景` |
| 产品文案 | `[@writer] 为产品 X 撰写营销文案` |
| 文档优化 | `[@editor] 优化这份技术文档` |
| 信息验证 | `[@fact-checker] 验证这些事实` |
| 知识检索 | `[@archivist] 查找关于 X 的文档` |

### AI 编程教程场景 ⭐
| 场景 | 使用方式 |
|------|---------|
| 完整教程 | `[task:tutorial] 创建"用 X 做 Y"的完整教程` |
| 概念讲解 | `[task:concept-guide] 深入讲解 X 技术概念` |
| 快速上手 | `[task:quick-start] 写一个 X 技术的快速上手指南` |
| 最佳实践 | `[task:best-practice] 总结 X 技术的最佳实践` |
| 代码验证 | `[@practitioner] 验证这段代码能否运行` |
| 学习路径 | `[@educator] 为初中级开发者设计 X 技术的学习路径` |
| 初学者审查 | `[@learner-advocate] 从初学者角度审查这个教程` |
| 版本检查 | `[@version-archivist] 标注教程涉及的所有技术栈版本` |

---

## 🔗 SKILL 组合

### 完整内容生产
```
/brainstorming (构思)
→ /ai-agent-team (创作)
→ /docx (Word)
→ /pdf (导出)
```

### 研究项目
```
/ai-agent-team (团队研究)
→ /obsidian-markdown (笔记)
→ /xlsx (数据表)
→ /pptx (演示)
```

### 知识管理
```
/ai-agent-team (整理)
→ /obsidian-bases (数据库)
→ /obsidian-canvas-creator (可视化)
```

---

## ✅ 最佳实践

### DO ✅
- 明确任务目标
- 提供充分上下文
- 遵循工作流程
- 给出具体反馈

### DON'T ❌
- 简单任务不用全部 Agent
- 不要跳过验证环节
- 不要忽略编辑步骤
- 避免重复信息

---

## 📊 效率对比

| 方式 | 适用场景 | 时间 | 质量 |
|------|---------|------|------|
| 单 Agent | 简单任务 | 快 | 中 |
| 指定 Agent | 单一明确任务 | 中 | 高 |
| Chief 协调 | 复杂项目 | 长 | 最高 |

---

## 🆘 故障排除

### 问题：Agent 响应不符合预期
**解决**：
1. 提供更具体的任务描述
2. 增加上下文信息
3. 使用迭代优化

### 问题：流程太慢
**解决**：
1. 使用快速模式
2. 减少不必要的 Agent
3. 并行处理独立任务

### 问题：质量不够高
**解决**：
1. 启用多轮迭代
2. 设置质量检查点
3. 明确质量标准

---

**记住**：当不确定如何开始时，直接使用 `[Chief]` 让主编协调团队！

---

**项目**: AI Tutorial Architect
**基于**: [newtype-profile](https://github.com/newtype-01/newtype-profile) 架构
**版本**: 2.0.0
**维护者**: yangmeishux
