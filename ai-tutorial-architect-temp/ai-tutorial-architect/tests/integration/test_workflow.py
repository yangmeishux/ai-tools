#!/usr/bin/env python3
"""
Integration Tests for AI Tutorial Architect
Tests complete workflows and agent coordination
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

class WorkflowTest:
    """Test complete tutorial creation workflows"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        
    def test_full_tutorial_workflow(self):
        """Test the complete 10-agent workflow"""
        print("\n[Integration Test] Full Tutorial Workflow")
        print("-" * 50)
        
        workflow_steps = [
            ("chief", "Define goals, audience, outcomes"),
            ("researcher", "Research topic, gather examples"),
            ("archivist", "Find related tutorials"),
            ("educator", "Design learning path"),
            ("writer", "Create content + code"),
            ("practitioner", "Verify ALL code runs"),
            ("learner-advocate", "Check clarity"),
            ("editor", "Polish structure"),
            ("humanizer", "Add natural tone (optional)"),
            ("version-archivist", "Document versions"),
            ("fact-checker", "Verify accuracy"),
            ("chief", "Final review")
        ]
        
        # Verify all skills exist
        skills_dir = project_root / "skills"
        for agent, task in workflow_steps:
            skill_file = skills_dir / agent / "SKILL.md"
            if skill_file.exists():
                self.passed += 1
                print(f"  ✓ {agent}: {task}")
            else:
                self.failed += 1
                print(f"  ✗ {agent}: MISSING")
                
        # Check workflow skill has this flow
        workflow_skill = skills_dir / "tutorial-workflow" / "SKILL.md"
        if workflow_skill.exists():
            with open(workflow_skill) as f:
                content = f.read()
            if "Chief" in content and "Practitioner" in content:
                self.passed += 1
                print("  ✓ Workflow skill documents full process")
            else:
                self.failed += 1
                print("  ✗ Workflow skill incomplete")
                
    def test_quick_start_workflow(self):
        """Test the quick-start workflow"""
        print("\n[Integration Test] Quick-Start Workflow")
        print("-" * 50)
        
        workflow = [
            ("chief", "Define scope"),
            ("writer", "Draft content"),
            ("practitioner", "Verify code"),
            ("editor", "Quick polish")
        ]
        
        skills_dir = project_root / "skills"
        for agent, task in workflow:
            skill_file = skills_dir / agent / "SKILL.md"
            if skill_file.exists():
                self.passed += 1
                print(f"  ✓ {agent}: {task}")
            else:
                self.failed += 1
                print(f"  ✗ {agent}: MISSING")
                
    def test_quality_framework(self):
        """Test the 8-dimensional quality framework"""
        print("\n[Integration Test] Quality Framework")
        print("-" * 50)
        
        dimensions = [
            ("runnability", "practitioner"),
            ("environment", "practitioner"),
            ("progressiveness", "educator"),
            ("term-explanation", "learner-advocate"),
            ("error-handling", ["practitioner", "learner-advocate"]),
            ("version-clarity", "version-archivist"),
            ("practical-value", ["educator", "practitioner"]),
            ("reproducibility", ["practitioner", "learner-advocate"])
        ]
        
        qa_skill = project_root / "skills" / "quality-assurance" / "SKILL.md"
        with open(qa_skill) as f:
            qa_content = f.read()
            
        for dimension, validators in dimensions:
            if dimension.replace('-', ' ') in qa_content.lower():
                self.passed += 1
                if isinstance(validators, list):
                    print(f"  ✓ {dimension}: checked by {', '.join(validators)}")
                else:
                    print(f"  ✓ {dimension}: checked by {validators}")
            else:
                self.failed += 1
                print(f"  ✗ {dimension}: NOT FOUND")
                
    def test_task_classifications(self):
        """Test task classification system"""
        print("\n[Integration Test] Task Classifications")
        print("-" * 50)
        
        classifications = [
            ("[task:tutorial]", "Complete tutorial"),
            ("[task:concept-guide]", "Deep concept"),
            ("[task:quick-start]", "Quick guide"),
            ("[task:best-practice]", "Best practices")
        ]
        
        skill_file = project_root / "SKILL.md"
        with open(skill_file) as f:
            content = f.read()
            
        for classification, description in classifications:
            if classification in content:
                self.passed += 1
                print(f"  ✓ {classification}: {description}")
            else:
                self.failed += 1
                print(f"  ✗ {classification}: MISSING")
                
    def test_humanizer_workflow(self):
        """Test Humanizer workflow integration"""
        print("\n[Integration Test] Humanizer Workflow")
        print("-" * 50)
        
        workflow_skill = project_root / "skills" / "tutorial-workflow" / "SKILL.md"
        with open(workflow_skill) as f:
            content = f.read()
            
        if "Humanizer" in content:
            self.passed += 1
            print("  ✓ Tutorial workflow includes Humanizer")
        else:
            self.failed += 1
            print("  ✗ Tutorial workflow missing Humanizer")
            
        if "humanize" in content.lower():
            self.passed += 1
            print("  ✓ Humanization task documented")
        else:
            self.warn("  ⚠ Humanization task not clearly documented")
            
        # Check humanizer skill exists
        humanizer_skill = project_root / "skills" / "humanizer" / "SKILL.md"
        if humanizer_skill.exists():
            self.passed += 1
            print("  ✓ Humanizer skill exists")
        else:
            self.failed += 1
            print("  ✗ Humanizer skill not found")
            
    def test_agent_references(self):
        """Test that agents reference each other correctly"""
        print("\n[Integration Test] Agent References")
        print("-" * 50)
        
        # Check chief references all agents
        chief_skill = project_root / "skills" / "chief" / "SKILL.md"
        with open(chief_skill) as f:
            chief_content = f.read()
            
        agents = ["researcher", "writer", "editor", "practitioner", "educator", "humanizer"]
        for agent in agents:
            if agent in chief_content.lower():
                self.passed += 1
                print(f"  ✓ Chief references {agent}")
            else:
                self.warn(f"  ⚠ Chief may not reference {agent}")
                
    def warn(self, message):
        print(message)
        
    def run_all(self):
        """Run all integration tests"""
        print("=" * 60)
        print("  AI Tutorial Architect - Integration Tests")
        print("=" * 60)
        
        self.test_full_tutorial_workflow()
        self.test_quick_start_workflow()
        self.test_quality_framework()
        self.test_task_classifications()
        self.test_agent_references()
        
        print("\n" + "=" * 60)
        print(f"  Results: {self.passed} passed, {self.failed} failed")
        print("=" * 60)
        
        return self.failed == 0

if __name__ == "__main__":
    test = WorkflowTest()
    success = test.run_all()
    sys.exit(0 if success else 1)
