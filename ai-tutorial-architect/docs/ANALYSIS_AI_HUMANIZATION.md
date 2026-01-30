# AI味去除功能分析报告

## 来源分析

### 1. 微信公众号文章要点
**"AI味"的核心特征：**
- 句式太规矩、模板化
- 表达空泛、通用（"正确的废话"）
- 逻辑通顺但生硬，缺少口语化
- 冗余信息，重点不突出

**去除AI味的心法：**
- 给它人设
- 喂它干货
- 让它说人话

### 2. GitHub Humanizer项目 (blader/humanizer)
基于维基百科 "Signs of AI writing" 指南，识别24种AI写作模式：

#### 语言和词汇问题
1. **Significance inflation** - 重要性夸大（"pivotal moment"）
2. **Notability name-dropping** - 名人/权威堆砌
3. **AI vocabulary** - AI特征词汇（additionally, testament, landscape）
4. **Copula avoidance** - 回避系动词（serves as → is）
5. **Synonym cycling** - 同义词循环（避免重复但造成不一致）
6. **Filler phrases** - 填充短语（"in order to", "due to the fact that"）
7. **Excessive hedging** - 过度限定（"could potentially possibly"）

#### 句式和结构问题
8. **Superficial -ing analyses** - 表面化的现在分词分析
9. **Negative parallelisms** - 否定平行结构（"not just X, it's Y"）
10. **Rule of three** - 三规则（过度使用三项并列）
11. **False ranges** - 虚假范围（"from Big Bang to dark matter"）

#### 格式和排版问题
12. **Em dash overuse** - 破折号滥用
13. **Boldface overuse** - 粗体滥用
14. **Inline-header lists** - 行内标题列表
15. **Title Case Headings** - 标题式大写
16. **Emojis** - 表情符号
17. **Curly quotes** - 弯引号

#### 内容和语气问题
18. **Chatbot artifacts** - 聊天机器人痕迹（"I hope this helps!"）
19. **Cutoff disclaimers** - 截断免责声明
20. **Sycophantic tone** - 谄媚语气（"Great question!"）
21. **Generic conclusions** - 通用结论（"The future looks bright"）

## 功能设计建议

### 新增Agent：Humanizer（人性化润色师）

**角色定位**：内容润色专家，专门去除AI写作痕迹

**核心职责**：
- 识别AI写作模式
- 转换为自然人类表达
- 保持内容准确性
- 增加个性化和情感色彩

**使用场景**：
- 教程内容需要更自然的表达
- 博客文章需要个性化风格
- 文档需要降低机器感
- 内容需要特定人设/语气

**工作流程**：
1. 扫描内容识别AI模式
2. 逐类修正问题
3. 增加具体细节和例子
4. 调整语气使其更自然
5. 保持技术准确性

**与其他Agent的关系**：
- 在 Editor 之后使用
- 与 Writer 协作确定语气
- 与 Fact-Checker 协作确保准确性
- 与 Learner-Advocate 协作确保易懂性

## 集成方案

### 1. 作为新技能添加到 skills/
路径：`skills/humanizer/SKILL.md`

### 2. 更新工作流
在 tutorial-workflow 中添加 Humanizer 作为可选步骤：
```
Editor → [Humanizer] → Version-Archivist
```

### 3. 新增任务分类
`[task:humanize]` - 人性化润色任务

### 4. 更新相关文档
- SKILL.md - 添加 Humanizer 到Agent列表
- README.md - 更新功能说明
- tutorial-workflow/SKILL.md - 添加新工作流
