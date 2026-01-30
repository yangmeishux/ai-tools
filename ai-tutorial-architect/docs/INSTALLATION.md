# Installation Guide

## Claude Code (Recommended)

### Via Plugin Marketplace

```bash
# Add marketplace
/plugin marketplace add yangmeishux/ai-tutorial-architect

# Install plugin
/plugin install ai-tutorial-architect
```

### Manual Installation

```bash
# Clone to skills directory
cd ~/.claude/skills
git clone https://github.com/yangmeishux/ai-tools.git ai-tutorial-architect

# Restart Claude Code
```

## Verification

```bash
# Check commands
/help

# Should see:
# /tutorial:create - Create complete tutorial
# /tutorial:verify - Verify tutorial quality
# /code:validate - Validate code examples

# Test workflow
> [Chief] Test the tutorial team
```

## Update

```bash
/plugin update ai-tutorial-architect
```

## Uninstall

```bash
/plugin uninstall ai-tutorial-architect
```
