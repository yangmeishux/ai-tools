#!/usr/bin/env python3
"""
AI Tutorial Architect - Comprehensive Test Suite
Tests all components for correctness and completeness
"""

import json
import os
import re
import sys
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class TestRunner:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        
    def pass_test(self, message):
        self.passed += 1
        print(f"{Colors.GREEN}✓ PASS{Colors.END}: {message}")
        
    def fail_test(self, message):
        self.failed += 1
        print(f"{Colors.RED}✗ FAIL{Colors.END}: {message}")
        
    def warn_test(self, message):
        self.warnings += 1
        print(f"{Colors.YELLOW}⚠ WARN{Colors.END}: {message}")
        
    def section(self, title):
        print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE}  {title}{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}")
        
    def test_plugin_config(self):
        """Test plugin configuration files"""
        self.section("Plugin Configuration")
        
        plugin_json = self.project_root / ".claude-plugin" / "plugin.json"
        marketplace_json = self.project_root / ".claude-plugin" / "marketplace.json"
        
        # Test plugin.json
        if plugin_json.exists():
            self.pass_test("plugin.json exists")
            try:
                with open(plugin_json) as f:
                    data = json.load(f)
                self.pass_test("plugin.json is valid JSON")
                
                required_fields = ['name', 'version', 'description']
                for field in required_fields:
                    if field in data:
                        self.pass_test(f"plugin.json has '{field}' field")
                    else:
                        self.fail_test(f"plugin.json missing '{field}' field")
                        
            except json.JSONDecodeError as e:
                self.fail_test(f"plugin.json is invalid JSON: {e}")
        else:
            self.fail_test("plugin.json not found")
            
        # Test marketplace.json
        if marketplace_json.exists():
            self.pass_test("marketplace.json exists")
            try:
                with open(marketplace_json) as f:
                    json.load(f)
                self.pass_test("marketplace.json is valid JSON")
            except json.JSONDecodeError as e:
                self.fail_test(f"marketplace.json is invalid JSON: {e}")
        else:
            self.fail_test("marketplace.json not found")
    
    def test_main_skill(self):
        """Test main SKILL.md"""
        self.section("Main SKILL.md")
        
        skill_md = self.project_root / "SKILL.md"
        if not skill_md.exists():
            self.fail_test("SKILL.md not found")
            return
            
        self.pass_test("SKILL.md exists")
        
        with open(skill_md) as f:
            content = f.read()
            
        # Check YAML frontmatter
        if content.startswith('---'):
            self.pass_test("SKILL.md has YAML frontmatter start")
        else:
            self.fail_test("SKILL.md missing YAML frontmatter start")
            
        # Check name field
        if re.search(r'^name:\s*\S+', content, re.MULTILINE):
            self.pass_test("SKILL.md has 'name' field")
        else:
            self.fail_test("SKILL.md missing 'name' field")
            
        # Check description field
        if re.search(r'^description:', content, re.MULTILINE):
            self.pass_test("SKILL.md has 'description' field")
        else:
            self.fail_test("SKILL.md missing 'description' field")
            
        # Check H1 heading
        if re.search(r'^# .+', content, re.MULTILINE):
            self.pass_test("SKILL.md has H1 heading")
        else:
            self.fail_test("SKILL.md missing H1 heading")
            
        # Check sections
        if '## ' in content:
            self.pass_test("SKILL.md has section headings")
        else:
            self.fail_test("SKILL.md missing section headings")
            
        # Word count
        word_count = len(content.split())
        if word_count < 3000:
            self.pass_test(f"SKILL.md word count OK ({word_count} words)")
        else:
            self.warn_test(f"SKILL.md word count high ({word_count} words)")
            
        # Check for key sections
        key_sections = ['When to Use', 'Quick Start', 'Agents', 'Workflows']
        for section in key_sections:
            if section in content:
                self.pass_test(f"SKILL.md has '{section}' section")
            else:
                self.warn_test(f"SKILL.md missing '{section}' section")
    
    def test_sub_skills(self):
        """Test all sub-skills"""
        self.section("Sub-skills")
        
        skills_dir = self.project_root / "skills"
        required_skills = [
            "chief", "researcher", "writer", "editor", 
            "fact-checker", "archivist",
            "educator", "practitioner", "learner-advocate", "version-archivist",
            "tutorial-workflow", "quality-assurance", "humanizer"
        ]
        
        for skill_name in required_skills:
            skill_file = skills_dir / skill_name / "SKILL.md"
            
            if not skill_file.exists():
                self.fail_test(f"Skill '{skill_name}' not found")
                continue
                
            self.pass_test(f"Skill '{skill_name}' exists")
            
            with open(skill_file) as f:
                content = f.read()
                
            # Check YAML frontmatter
            if content.startswith('---'):
                self.pass_test(f"Skill '{skill_name}' has YAML frontmatter")
            else:
                self.fail_test(f"Skill '{skill_name}' missing YAML frontmatter")
                
            # Check name matches directory
            name_match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
            if name_match:
                actual_name = name_match.group(1).strip()
                if actual_name == skill_name:
                    self.pass_test(f"Skill '{skill_name}' name matches directory")
                else:
                    self.fail_test(f"Skill '{skill_name}' name mismatch: '{actual_name}'")
            else:
                self.fail_test(f"Skill '{skill_name}' missing name field")
                
            # Check description
            if re.search(r'^description:', content, re.MULTILINE):
                self.pass_test(f"Skill '{skill_name}' has description")
            else:
                self.fail_test(f"Skill '{skill_name}' missing description")
                
            # Check H1 heading
            if re.search(r'^# .+', content, re.MULTILINE):
                self.pass_test(f"Skill '{skill_name}' has H1 heading")
            else:
                self.fail_test(f"Skill '{skill_name}' missing H1 heading")
                
            # Check core principle
            if 'Core principle:' in content or 'core principle' in content.lower():
                self.pass_test(f"Skill '{skill_name}' has core principle")
            else:
                self.warn_test(f"Skill '{skill_name}' missing core principle")
                
            # Word count
            word_count = len(content.split())
            if word_count < 1000:
                self.pass_test(f"Skill '{skill_name}' word count OK ({word_count} words)")
            else:
                self.warn_test(f"Skill '{skill_name}' word count high ({word_count} words)")
    
    def test_commands(self):
        """Test command definitions"""
        self.section("Commands")
        
        commands_dir = self.project_root / "commands"
        required_commands = ["tutorial-create", "tutorial-verify", "code-validate"]
        
        for cmd_name in required_commands:
            cmd_file = commands_dir / f"{cmd_name}.md"
            
            if not cmd_file.exists():
                self.fail_test(f"Command '{cmd_name}' not found")
                continue
                
            self.pass_test(f"Command '{cmd_name}' exists")
            
            with open(cmd_file) as f:
                content = f.read()
                
            # Check has Usage section
            if 'Usage' in content or '## ' in content:
                self.pass_test(f"Command '{cmd_name}' has documentation")
            else:
                self.warn_test(f"Command '{cmd_name}' missing documentation")
    
    def test_agents(self):
        """Test agent definitions"""
        self.section("Agents")
        
        agents_dir = self.project_root / "agents"
        
        if (agents_dir / "code-reviewer.md").exists():
            self.pass_test("code-reviewer agent exists")
        else:
            self.warn_test("code-reviewer agent not found")
    
    def test_documentation(self):
        """Test documentation files"""
        self.section("Documentation")
        
        docs_dir = self.project_root / "docs"
        
        # Test architecture doc
        arch_file = docs_dir / "ARCHITECTURE.md"
        if arch_file.exists():
            self.pass_test("ARCHITECTURE.md exists")
        else:
            self.warn_test("ARCHITECTURE.md not found")
            
        # Test installation doc
        install_file = docs_dir / "INSTALLATION.md"
        if install_file.exists():
            self.pass_test("INSTALLATION.md exists")
        else:
            self.warn_test("INSTALLATION.md not found")
            
        # Test README
        readme_file = self.project_root / "README.md"
        if readme_file.exists():
            self.pass_test("README.md exists")
            with open(readme_file) as f:
                content = f.read()
            if '## ' in content:
                self.pass_test("README.md has sections")
            else:
                self.warn_test("README.md missing sections")
        else:
            self.fail_test("README.md not found")
    
    def test_structure(self):
        """Test overall structure"""
        self.section("Structure")
        
        # Check all skills present
        skills_dir = self.project_root / "skills"
        skill_count = len([d for d in skills_dir.iterdir() if d.is_dir()])
        if skill_count == 13:
            self.pass_test(f"All 13 skills present")
        else:
            self.fail_test(f"Expected 13 skills, found {skill_count}")
            
        # Check directory structure
        required_dirs = ['.claude-plugin', 'skills', 'commands', 'docs']
        for dir_name in required_dirs:
            dir_path = self.project_root / dir_name
            if dir_path.exists() and dir_path.is_dir():
                self.pass_test(f"Directory '{dir_name}' exists")
            else:
                self.fail_test(f"Directory '{dir_name}' missing")
    
    def run_all_tests(self):
        """Run all tests"""
        print(f"{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE}  AI Tutorial Architect - Test Suite v2.1.0{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}")
        
        self.test_plugin_config()
        self.test_main_skill()
        self.test_sub_skills()
        self.test_commands()
        self.test_agents()
        self.test_documentation()
        self.test_structure()
        
        # Summary
        print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BLUE}                      TEST SUMMARY{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}Passed:   {self.passed}{Colors.END}")
        print(f"{Colors.RED}Failed:   {self.failed}{Colors.END}")
        print(f"{Colors.YELLOW}Warnings: {self.warnings}{Colors.END}")
        total = self.passed + self.failed
        print(f"Total:    {total}")
        print("")
        
        if self.failed == 0:
            print(f"{Colors.GREEN}✓ All critical tests passed!{Colors.END}")
            return 0
        else:
            print(f"{Colors.RED}✗ Some tests failed.{Colors.END}")
            return 1

if __name__ == "__main__":
    project_root = Path(__file__).parent.parent
    runner = TestRunner(project_root)
    sys.exit(runner.run_all_tests())
