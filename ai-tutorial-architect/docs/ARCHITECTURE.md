# AI Tutorial Architect - Architecture

System architecture and design principles.

## Overview

AI Tutorial Architect is a multi-agent system for creating high-quality programming tutorials. It applies proven software development practices to content creation.

## Design Principles

### 1. Separation of Concerns
Each agent has a focused responsibility:
- **Researcher** finds information
- **Writer** creates content
- **Practitioner** validates execution
- **Editor** refines quality

### 2. Quality Gates
Quality checks at natural boundaries prevent errors from propagating:
- Research → Outline approval
- Writing → Code verification
- Editing → Final review

### 3. Composability
Agents can be combined for different workflows:
- Full tutorial: All 11 agents (Core 6 + Tutorial 4 + Humanizer)
- Quick guide: Writer + Practitioner + Version-Archivist
- Research only: Researcher + Archivist
- Humanization: Humanizer + Editor

### 4. Test-Driven Content
Every code example must:
- Execute successfully
- Produce documented output
- Run in clean environment

## Directory Structure

```
ai-tutorial-architect/
├── .claude-plugin/         # Claude Code plugin config
│   ├── plugin.json         # Plugin metadata
│   └── marketplace.json    # Marketplace listing
├── skills/                 # Agent skill definitions
│   ├── chief/              # Coordination
│   ├── researcher/         # Information gathering
│   ├── writer/             # Content creation
│   ├── editor/             # Content refinement
│   ├── fact-checker/       # Accuracy validation
│   ├── archivist/          # Knowledge management
│   ├── educator/           # Learning design
│   ├── practitioner/       # Code validation
│   ├── learner-advocate/   # Beginner perspective
│   ├── version-archivist/  # Version tracking
│   ├── humanizer/          # AI content humanization
│   ├── tutorial-workflow/  # Workflow definitions (supporting)
│   └── quality-assurance/  # Quality framework (supporting)
├── commands/               # CLI commands
│   ├── tutorial-create.md
│   ├── tutorial-verify.md
│   └── code-validate.md
├── agents/                 # Agent definitions
│   └── code-reviewer.md
├── docs/                   # Documentation
│   └── ARCHITECTURE.md
├── README.md               # Main documentation
└── SKILL.md                # Entry point
```

## Agent Communication

Agents communicate through structured handoffs:

1. Chief creates task specification
2. Agent receives context + requirements
3. Agent produces output
4. Output passes to next agent or Chief

No direct agent-to-agent communication - all coordination through Chief.

## Quality Framework

The 8-dimensional quality model:

```
┌─────────────────────────────────────┐
│         Quality Dimensions          │
├─────────────────────────────────────┤
│  Technical        │  Pedagogical    │
│  ─────────────    │  ───────────    │
│  • Runnability    │  • Progression  │
│  • Environment    │  • Terminology  │
│  • Versions       │  • Practical    │
│                   │  • Reproducible │
├─────────────────────────────────────┤
│  Cross-cutting: Error Handling      │
└─────────────────────────────────────┘
```

## Workflow Patterns

### Sequential
```
A → B → C → D
```
For dependent tasks (writing before editing).

### Parallel
```
    ┌→ B ─┐
A → ├→ C ─┼→ E
    └→ D ─┘
```
For independent tasks (research + archivist).

### Iterative
```
A → B → C → (check) → B → C → (check) → D
```
For refinement loops (code verification).

## Extensibility

Add new capabilities by:
1. Creating skill in `skills/[name]/SKILL.md`
2. Adding command in `commands/` if needed
3. Updating workflow documentation
4. Registering with Chief

## Inspiration

This architecture draws from:
- [superpowers](https://github.com/obra/superpowers) - Multi-agent workflow patterns
- [newtype-profile](https://github.com/newtype-01/newtype-profile) - Agent team coordination
- Test-Driven Development - Quality-first approach
