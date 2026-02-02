---
name: humanizer
description: Use when content sounds too robotic, needs personality, requires natural expression, or before publishing to remove AI-generated patterns
---

# Humanizer - AI Content Humanizer

Remove AI writing patterns and add human touch to content. Transform robotic text into natural, engaging prose.

**Core principle:** AI writes for correctness; humans write for connection. Bridge that gap.

## When to Use

```dot
digraph when_to_use {
    "Content sounds robotic?" [shape=diamond];
    "Need specific personality?" [shape=diamond];
    "Publishing externally?" [shape=diamond];
    "Target audience prefers natural tone?" [shape=diamond];
    "Use Humanizer" [shape=box];
    "Skip for now" [shape=box];

    "Content sounds robotic?" -> "Use Humanizer" [label="yes"];
    "Content sounds robotic?" -> "Need specific personality?" [label="no"];
    "Need specific personality?" -> "Use Humanizer" [label="yes"];
    "Need specific personality?" -> "Publishing externally?" [label="no"];
    "Publishing externally?" -> "Use Humanizer" [label="yes"];
    "Publishing externally?" -> "Target audience prefers natural tone?" [label="no"];
    "Target audience prefers natural tone?" -> "Use Humanizer" [label="yes"];
    "Target audience prefers natural tone?" -> "Skip for now" [label="no"];
}
```

**Trigger phrases:**
- `[@humanizer] Make this sound more natural`
- `[@humanizer] Remove AI patterns from this text`
- `[@humanizer] Add personality to this tutorial`

## The 24 AI Patterns to Remove

### Group 1: Inflated Language

| Pattern | AI Example | Humanized |
|---------|------------|-----------|
| **Significance inflation** | "marks a pivotal moment in..." | "was established in 1989 to..." |
| **Promotional language** | "nestled within the breathtaking" | "is a town in the..." |
| **Vague attributions** | "Experts believe it plays a crucial role" | "according to a 2019 survey by..." |
| **Generic conclusions** | "The future looks bright" | [specific plans or remove] |

### Group 2: AI Vocabulary

| Pattern | AI Example | Humanized |
|---------|------------|-----------|
| **Buzzwords** | additionally, testament, landscape, showcasing | also, remains, common |
| **Copula avoidance** | serves as, features, boasts | is, has |
| **Filler phrases** | "In order to", "Due to the fact that" | To, Because |
| **Excessive hedging** | "could potentially possibly" | may |

### Group 3: Formulaic Structures

| Pattern | AI Example | Humanized |
|---------|------------|-----------|
| **Rule of three** | "innovation, inspiration, and insights" | natural number of items |
| **Negative parallelisms** | "It's not just X, it's Y" | state directly |
| **False ranges** | "from the Big Bang to dark matter" | list topics directly |
| **Superficial -ing** | "symbolizing... reflecting... showcasing" | remove or add sources |

### Group 4: Formatting Issues

| Pattern | AI Example | Humanized |
|---------|------------|-----------|
| **Em dash overuse** | "institutions—not people—yet continues" | use commas or periods |
| **Title Case Headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations" |
| **Inline-header lists** | "Performance: Performance improved" | convert to prose |
| **Emojis in serious content** | "🚀 Launch Phase: 💡 Insight" | remove |

### Group 5: Chatbot Artifacts

| Pattern | AI Example | Humanized |
|---------|------------|-----------|
| **Helpful endings** | "I hope this helps! Let me know..." | remove entirely |
| **Sycophantic tone** | "Great question! You're absolutely right!" | respond directly |
| **Cutoff disclaimers** | "While details are limited..." | find sources or remove |
| **Notability dropping** | "cited in NYT, BBC, FT, Hindu" | cite specific article |

### Group 6: Repetition Issues

| Pattern | AI Example | Humanized |
|---------|------------|-----------|
| **Synonym cycling** | "protagonist... main character... central figure" | pick one, repeat when clear |
| **Formulaic challenges** | "Despite challenges... continues to thrive" | specific facts |
| **Chatbot openings** | "Here is an essay on..." | jump straight in |

## Humanization Process

```dot
digraph humanize {
    rankdir=TB;

    "Read content completely" [shape=box];
    "Scan for AI patterns" [shape=box];
    "Categorize issues found" [shape=box];
    "Rewrite section by section" [shape=box];
    "Add specific examples" [shape=box];
    "Adjust tone for audience" [shape=box];
    "Verify accuracy maintained" [shape=box];
    "Final polish" [shape=box];

    "Read content completely" -> "Scan for AI patterns";
    "Scan for AI patterns" -> "Categorize issues found";
    "Categorize issues found" -> "Rewrite section by section";
    "Rewrite section by section" -> "Add specific examples";
    "Add specific examples" -> "Adjust tone for audience";
    "Adjust tone for audience" -> "Verify accuracy maintained";
    "Verify accuracy maintained" -> "Final polish";
}
```

## Humanization Techniques

### 1. Add Specific Details
Replace vague statements with concrete examples.

**Before:** "AI tools have improved developer productivity significantly."  
**After:** "In a 2024 Google study, developers using Copilot completed simple functions 55% faster, though debugging speed didn't change."

### 2. Use Conversational Tone
Write like you're explaining to a colleague.

**Before:** "It is important to note that..."  
**After:** "Here's the thing..." or just remove and state directly.

### 3. Vary Sentence Structure
Mix short and long sentences. Break patterns.

**Before:** "The system processes data. The system outputs results. The system handles errors."  
**After:** "It processes your data. Results come out clean. And when something breaks? There's a fallback."

### 4. Include Imperfections
Humans don't write perfectly. Add:
- Occasional fragments
- Rhetorical questions
- Direct address ("you'll notice...")
- Personal asides

### 5. Choose Clarity Over Variety
Don't force synonyms. Repeat words when they're clearest.

**Before:** "The protagonist... main character... central figure... hero"  
**After:** "The protagonist... the protagonist... they..."

## Tone Adjustments by Context

| Context | Approach |
|---------|----------|
| **Technical tutorial** | Clear, direct, occasional humor |
| **Blog post** | Conversational, personal, engaging |
| **Documentation** | Friendly but efficient |
| **Academic** | Precise but not pompous |
| **Marketing** | Enthusiastic but not hype-y |

## Output Format

```markdown
## Humanization Report

### Patterns Found
- [X] Significance inflation (3 instances)
- [X] AI vocabulary (7 instances)
- [X] Rule of three (2 instances)
- [ ] Chatbot artifacts (none found)

### Changes Made
| Location | Before | After |
|----------|--------|-------|
| Para 2 | "pivotal moment" | "started in 2020" |
| Para 4 | "Additionally, the system" | "It also" |
| Code comment | "serves as a utility" | "this utility" |

### Tone Adjustments
- Shifted from formal to conversational
- Added specific example (line 23)
- Removed promotional language

### Accuracy Check
- All technical details preserved ✓
- No facts altered ✓
- Code unchanged ✓
```

## Red Flags

**Never:**
- Sacrifice clarity for "sounding human"
- Add factual errors in pursuit of casual tone
- Remove all structure (humans use structure too)
- Overcorrect to the point of unprofessionalism

**If content is already good:**
- Don't force changes
- Minor polish only
- Flag as "minimal humanization needed"

**Maintain accuracy:**
- Technical terms stay technical
- Numbers and facts unchanged
- Code examples untouched
- Only the wrapper changes

## Integration

**Typical workflow position:**
```
Writer → Editor → [Humanizer] → Version-Archivist → Fact-Checker
```

**Works with:**
- **Writer** - Establish base tone, then humanize
- **Editor** - Structural fixes first, then tone
- **Fact-Checker** - Verify humanization didn't alter facts
- **Learner-Advocate** - Ensure humanization improves clarity

**Use sparingly for:**
- API documentation (keep it dry)
- Code comments (clarity over style)
- Legal/compliance text (precision required)
