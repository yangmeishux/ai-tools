# /tutorial:verify - Verify Tutorial Quality

Run the 8-dimensional quality assessment on a tutorial.

## Usage

```
/tutorial:verify [tutorial-path] [--level=gold|silver|bronze]
```

## Examples

```
/tutorial:verify ./my-tutorial.md
/tutorial:verify ./my-tutorial.md --level=gold
```

## What It Checks

1. Runnability - All code executes
2. Environment Completeness - Setup documented
3. Progressiveness - Appropriate difficulty
4. Term Explanation - Terms defined
5. Error Handling - Common errors covered
6. Version Clarity - Versions specified
7. Practical Value - Real-world relevance
8. Reproducibility - Steps clearly defined

## Output

Quality report with:
- Overall rating (Gold/Silver/Bronze)
- Per-dimension scores
- Required improvements list
