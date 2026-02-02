# AI Tutorial Architect - Test Suite

Test suite based on [superpowers](https://github.com/obra/superpowers) testing methodology.

## Quick Start

```bash
# Run all tests
python3 tests/test_all.py

# Run integration tests only
python3 tests/integration/test_workflow.py

# Run bash test suite
bash tests/run_all_tests.sh
```

## Test Structure

```
tests/
├── test_all.py              # Main unit tests (118 tests)
├── run_all_tests.sh         # Bash test runner
├── TEST_REPORT.md           # Latest test report
├── README.md                # This file
└── integration/
    └── test_workflow.py     # Integration tests (33 tests)
```

## What We Test

### 1. Plugin Configuration
- plugin.json validity
- marketplace.json validity
- Required fields presence

### 2. Skill Structure
- YAML frontmatter format
- Required fields (name, description)
- Content structure (H1, sections)
- Word count limits

### 3. Content Quality
- Core principles stated
- Flowcharts present
- Cross-references valid

### 4. Integration
- Full workflow (11 agents)
- Quick-start workflow
- Quality framework (8 dimensions)
- Task classifications

## Adding New Tests

```python
# In tests/test_all.py
def test_new_feature(self):
    """Description of what you're testing"""
    if condition:
        self.pass_test("Description")
    else:
        self.fail_test("Description")
```

## Test Report

See [TEST_REPORT.md](TEST_REPORT.md) for latest results.

---

**Last Updated:** 2026-01-30  
**Status:** ✅ All tests passing (151/151)
