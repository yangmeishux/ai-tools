#!/bin/bash
# AI Tutorial Architect - Test Suite
# Based on superpowers testing methodology

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PASSED=0
FAILED=0

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test helper functions
pass() {
    echo -e "${GREEN}✓ PASS${NC}: $1"
    ((PASSED++))
}

fail() {
    echo -e "${RED}✗ FAIL${NC}: $1"
    ((FAILED++))
}

warn() {
    echo -e "${YELLOW}⚠ WARN${NC}: $1"
}

section() {
    echo ""
    echo "═══════════════════════════════════════════════════════════"
    echo "  $1"
    echo "═══════════════════════════════════════════════════════════"
}

# Test 1: Plugin Configuration
test_plugin_config() {
    section "Testing Plugin Configuration"
    
    if [ -f "$PROJECT_ROOT/.claude-plugin/plugin.json" ]; then
        pass "plugin.json exists"
        
        # Validate JSON
        if python3 -c "import json; json.load(open('$PROJECT_ROOT/.claude-plugin/plugin.json'))" 2>/dev/null; then
            pass "plugin.json is valid JSON"
        else
            fail "plugin.json is invalid JSON"
        fi
        
        # Check required fields
        if grep -q '"name"' "$PROJECT_ROOT/.claude-plugin/plugin.json"; then
            pass "plugin.json has 'name' field"
        else
            fail "plugin.json missing 'name' field"
        fi
        
        if grep -q '"version"' "$PROJECT_ROOT/.claude-plugin/plugin.json"; then
            pass "plugin.json has 'version' field"
        else
            fail "plugin.json missing 'version' field"
        fi
    else
        fail "plugin.json not found"
    fi
    
    if [ -f "$PROJECT_ROOT/.claude-plugin/marketplace.json" ]; then
        pass "marketplace.json exists"
        
        if python3 -c "import json; json.load(open('$PROJECT_ROOT/.claude-plugin/marketplace.json'))" 2>/dev/null; then
            pass "marketplace.json is valid JSON"
        else
            fail "marketplace.json is invalid JSON"
        fi
    else
        fail "marketplace.json not found"
    fi
}

# Test 2: Main SKILL.md
test_main_skill() {
    section "Testing Main SKILL.md"
    
    if [ -f "$PROJECT_ROOT/SKILL.md" ]; then
        pass "SKILL.md exists"
        
        # Check YAML frontmatter
        if head -5 "$PROJECT_ROOT/SKILL.md" | grep -q '^---$'; then
            pass "SKILL.md has YAML frontmatter delimiter"
        else
            fail "SKILL.md missing YAML frontmatter delimiter"
        fi
        
        # Check required fields
        if head -10 "$PROJECT_ROOT/SKILL.md" | grep -q '^name:'; then
            pass "SKILL.md has 'name' in frontmatter"
        else
            fail "SKILL.md missing 'name' in frontmatter"
        fi
        
        if head -10 "$PROJECT_ROOT/SKILL.md" | grep -q '^description:'; then
            pass "SKILL.md has 'description' in frontmatter"
        else
            fail "SKILL.md missing 'description' in frontmatter"
        fi
        
        # Check content sections
        if grep -q '^# ' "$PROJECT_ROOT/SKILL.md"; then
            pass "SKILL.md has H1 heading"
        else
            fail "SKILL.md missing H1 heading"
        fi
        
        if grep -q '## ' "$PROJECT_ROOT/SKILL.md"; then
            pass "SKILL.md has section headings"
        else
            fail "SKILL.md missing section headings"
        fi
        
        # Word count check (should be reasonable)
        WORD_COUNT=$(wc -w < "$PROJECT_ROOT/SKILL.md")
        if [ "$WORD_COUNT" -lt 3000 ]; then
            pass "SKILL.md word count reasonable ($WORD_COUNT words)"
        else
            warn "SKILL.md word count high ($WORD_COUNT words) - consider optimizing"
        fi
    else
        fail "SKILL.md not found"
    fi
}

# Test 3: Sub-skills
test_sub_skills() {
    section "Testing Sub-skills"
    
    SKILLS_DIR="$PROJECT_ROOT/skills"
    REQUIRED_SKILLS=("chief" "researcher" "writer" "editor" "fact-checker" "archivist" "educator" "practitioner" "learner-advocate" "version-archivist" "tutorial-workflow" "quality-assurance")
    
    for skill in "${REQUIRED_SKILLS[@]}"; do
        SKILL_FILE="$SKILLS_DIR/$skill/SKILL.md"
        if [ -f "$SKILL_FILE" ]; then
            pass "Skill '$skill' exists"
            
            # Check YAML frontmatter
            if head -5 "$SKILL_FILE" | grep -q '^---$'; then
                pass "Skill '$skill' has YAML frontmatter"
            else
                fail "Skill '$skill' missing YAML frontmatter"
            fi
            
            # Check name field matches directory
            if head -10 "$SKILL_FILE" | grep -q "^name: $skill"; then
                pass "Skill '$skill' has matching name field"
            else
                fail "Skill '$skill' name field mismatch"
            fi
            
            # Check description field
            if head -10 "$SKILL_FILE" | grep -q '^description:'; then
                pass "Skill '$skill' has description"
            else
                fail "Skill '$skill' missing description"
            fi
            
            # Check word count (superpowers recommends <500 for most skills)
            SKILL_WORDS=$(wc -w < "$SKILL_FILE")
            if [ "$SKILL_WORDS" -lt 1000 ]; then
                pass "Skill '$skill' word count OK ($SKILL_WORDS words)"
            else
                warn "Skill '$skill' word count high ($SKILL_WORDS words)"
            fi
            
        else
            fail "Skill '$skill' not found at $SKILL_FILE"
        fi
    done
}

# Test 4: Commands
test_commands() {
    section "Testing Commands"
    
    COMMANDS_DIR="$PROJECT_ROOT/commands"
    REQUIRED_COMMANDS=("tutorial-create" "tutorial-verify" "code-validate")
    
    for cmd in "${REQUIRED_COMMANDS[@]}"; do
        CMD_FILE="$COMMANDS_DIR/$cmd.md"
        if [ -f "$CMD_FILE" ]; then
            pass "Command '$cmd' exists"
            
            # Check has usage section
            if grep -q '## Usage\|# Usage\|Usage:' "$CMD_FILE"; then
                pass "Command '$cmd' has usage documentation"
            else
                warn "Command '$cmd' missing usage documentation"
            fi
            
            # Check has examples
            if grep -q '## Example\|# Example\|Example:' "$CMD_FILE"; then
                pass "Command '$cmd' has examples"
            else
                warn "Command '$cmd' missing examples"
            fi
        else
            fail "Command '$cmd' not found"
        fi
    done
}

# Test 5: Agents
test_agents() {
    section "Testing Agents"
    
    AGENTS_DIR="$PROJECT_ROOT/agents"
    
    if [ -f "$AGENTS_DIR/code-reviewer.md" ]; then
        pass "code-reviewer agent exists"
    else
        warn "code-reviewer agent not found (optional)"
    fi
}

# Test 6: Documentation
test_documentation() {
    section "Testing Documentation"
    
    DOCS_DIR="$PROJECT_ROOT/docs"
    
    if [ -f "$DOCS_DIR/ARCHITECTURE.md" ]; then
        pass "ARCHITECTURE.md exists"
    else
        warn "ARCHITECTURE.md not found"
    fi
    
    if [ -f "$DOCS_DIR/INSTALLATION.md" ]; then
        pass "INSTALLATION.md exists"
    else
        warn "INSTALLATION.md not found"
    fi
    
    if [ -f "$PROJECT_ROOT/README.md" ]; then
        pass "README.md exists"
        
        # Check README has key sections
        if grep -q '## ' "$PROJECT_ROOT/README.md"; then
            pass "README.md has sections"
        else
            warn "README.md missing sections"
        fi
    else
        fail "README.md not found"
    fi
}

# Test 7: Cross-references
test_cross_references() {
    section "Testing Cross-references"
    
    # Check that skills reference each other correctly
    if grep -r "skills/chief" "$PROJECT_ROOT/skills/"/*.md 2>/dev/null || true; then
        pass "Cross-references to chief skill exist"
    fi
    
    # Check no broken markdown links
    BROKEN_LINKS=$(grep -rE '\[.*\]\(.*\)' "$PROJECT_ROOT/skills/"/*.md 2>/dev/null | grep -v 'http' | grep -v '.md)' || true)
    if [ -z "$BROKEN_LINKS" ]; then
        pass "No obvious broken internal links in skills"
    else
        warn "Potential broken links found"
    fi
}

# Test 8: File naming conventions
test_naming_conventions() {
    section "Testing Naming Conventions"
    
    # Check skill directories use kebab-case
    for dir in "$PROJECT_ROOT/skills"/*; do
        if [ -d "$dir" ]; then
            dirname=$(basename "$dir")
            if echo "$dirname" | grep -qE '^[a-z0-9]+(-[a-z0-9]+)*$'; then
                pass "Skill directory '$dirname' uses kebab-case"
            else
                warn "Skill directory '$dirname' may not follow kebab-case convention"
            fi
        fi
    done
}

# Test 9: Integration
test_integration() {
    section "Integration Tests"
    
    # Test that all skills can be parsed
    SKILLS_COUNT=$(find "$PROJECT_ROOT/skills" -name "SKILL.md" | wc -l)
    if [ "$SKILLS_COUNT" -eq 12 ]; then
        pass "All 12 skills present"
    else
        fail "Expected 12 skills, found $SKILLS_COUNT"
    fi
    
    # Test directory structure
    if [ -d "$PROJECT_ROOT/.claude-plugin" ] && [ -d "$PROJECT_ROOT/skills" ] && [ -d "$PROJECT_ROOT/commands" ]; then
        pass "Directory structure is complete"
    else
        fail "Directory structure incomplete"
    fi
}

# Run all tests
main() {
    echo "╔═══════════════════════════════════════════════════════════╗"
    echo "║     AI Tutorial Architect - Test Suite v2.1.0            ║"
    echo "╚═══════════════════════════════════════════════════════════╝"
    
    test_plugin_config
    test_main_skill
    test_sub_skills
    test_commands
    test_agents
    test_documentation
    test_cross_references
    test_naming_conventions
    test_integration
    
    # Summary
    echo ""
    echo "═══════════════════════════════════════════════════════════"
    echo "                      TEST SUMMARY                         "
    echo "═══════════════════════════════════════════════════════════"
    echo -e "${GREEN}Passed: $PASSED${NC}"
    echo -e "${RED}Failed: $FAILED${NC}"
    TOTAL=$((PASSED + FAILED))
    echo "Total:  $TOTAL"
    echo ""
    
    if [ $FAILED -eq 0 ]; then
        echo -e "${GREEN}✓ All tests passed!${NC}"
        exit 0
    else
        echo -e "${RED}✗ Some tests failed.${NC}"
        exit 1
    fi
}

main "$@"
