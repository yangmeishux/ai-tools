# /code:validate - Validate Code Examples

Execute and verify all code examples in a tutorial.

## Usage

```
/code:validate [tutorial-path] [--env=python|node|go|...]
```

## Examples

```
/code:validate ./tutorial.md --env=python
/code:validate ./tutorial.md --env=node
```

## What It Does

1. Extracts all code blocks
2. Sets up clean environment
3. Executes each example
4. Compares output to documented
5. Reports pass/fail for each

## Output

```
Code Validation Report
======================
✅ Example 1: hello.py - PASS
✅ Example 2: setup.py - PASS
❌ Example 3: api_call.py - FAIL (missing import)
⚠️ Example 4: config.py - PASS with warnings
```
