# AI Writing Patterns Reference

Complete reference of AI writing patterns to detect and correct.

Based on Wikipedia's "Signs of AI writing" guide and community research.

## Quick Reference Card

### Top 10 Most Common Patterns

1. **"Additionally"** → Use "also", "plus", "and"
2. **"It's important to note"** → Delete or replace with "Note:"
3. **"In order to"** → "To"
4. **"Due to the fact that"** → "Because"
5. **"Not just X, it's Y"** → State directly
6. **"Marks a pivotal moment"** → Be specific about dates/events
7. **Three-item lists** → Vary the count
8. **"I hope this helps"** → Delete
9. **"Experts believe"** → Cite specific expert
10. **"The future looks bright"** → Specific predictions or delete

## Pattern Categories

### 1. Inflated Importance

AI often overstates significance to sound authoritative.

**Phrases to flag:**
- pivotal moment
- crucial role
- significant impact
- transformative potential
- groundbreaking
- vital importance
- key player

**Fix:** Replace with specific facts or remove.

---

### 2. Empty Transitions

**Instead of:**
- "Furthermore,"
- "Moreover,"
- "Additionally,"
- "Consequently,"
- "Therefore,"
- "In conclusion,"

**Use:**
- "Also,"
- "So,"
- "That means,"
- Just start the sentence
- [Delete entirely]
- "In short," or just end

---

### 3. Hedging Overload

**Instead of:**
- "could potentially possibly"
- "might arguably be considered"
- "it could be suggested that"
- "one might perhaps think"

**Use:**
- "may"
- "might"
- "arguably"
- "suggests that"
- "I think"

Or state directly if you have evidence.

---

### 4. Buzzword Bingo

**Common AI vocabulary to vary:**

| AI Word | Alternatives |
|---------|--------------|
| additionally | also, plus, and, besides |
| testament to | shows, proves, reflects |
| landscape | field, area, world, scene |
| showcasing | showing, displaying, with |
| underscores | shows, highlights, emphasizes |
| serves as | is, acts as, works as |
| functions as | is, works as |
| plays a role | helps, contributes, is part of |
| crucial | key, critical, vital, important |
| significant | big, major, notable, real |

---

### 5. Formulaic Openings

**Avoid:**
- "In today's rapidly evolving world..."
- "In the ever-changing landscape of..."
- "As we navigate the complexities of..."
- "In an era defined by..."

**Instead:** Jump straight to the point.

---

### 6. Formulaic Closings

**Avoid:**
- "In conclusion,..."
- "To sum up,..."
- "The future looks bright..."
- "Exciting times lie ahead..."
- "Only time will tell..."

**Instead:**
- End on your strongest point
- Or just stop
- Or add a specific forward-looking statement

---

### 7. Unnecessary Intensifiers

**Flag:**
- very, extremely, incredibly
- truly, really, actually
- quite, rather, fairly

**Fix:** Remove most of them. Keep only when they add meaning.

---

### 8. Passive Voice Overuse

**AI:** "The code was written by the developer."  
**Human:** "The developer wrote the code."

Not all passive is bad, but AI overuses it.

---

### 9. Abstract Nouns

**AI:** "The utilization of tools"  
**Human:** "Using tools"

**Flag:** -tion, -ness, -ity, -ment, -ance, -ence endings

---

### 10. Chatbot Telltales

**Remove:**
- "I hope this helps!"
- "Let me know if you have questions!"
- "Happy to assist!"
- "Great question!"
- "You're absolutely right!"
- "I'm glad you asked!"

**Exception:** Actual conversational contexts.

---

## Before/After Examples

### Example 1: Tutorial Introduction

**AI Version:**
> In today's rapidly evolving technological landscape, AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. Furthermore, these groundbreaking tools are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.

**Humanized:**
> AI coding assistants can speed up some tasks. In a 2024 Google study, developers using Copilot completed simple functions 55% faster. But the benefits aren't universal—they showed no improvement on debugging or architectural decisions.

### Example 2: Technical Explanation

**AI Version:**
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users.

**Humanized:**
> These tools shine at boilerplate: config files, test scaffolding, repetitive refactors. They struggle when judgment is needed. I've accepted suggestions that compiled and passed tests but did the wrong thing because I wasn't paying attention.

### Example 3: Documentation

**AI Version:**
> In order to configure the system, it is necessary to first ensure that all prerequisites have been satisfied. Additionally, one must verify that the environment variables are properly set, due to the fact that the application depends on them for crucial functionality.

**Humanized:**
> Before starting, check that:
> - Node.js 18+ is installed
> - DATABASE_URL is set in your .env file
> - The app won't start without these

---

## Detection Regex Patterns

For automated scanning:

```regex
\b(additionally|furthermore|moreover|consequently|therefore|thus|hence)\b
\b(it is important to note|it should be noted)\b
\b(in order to|so as to)\b
\b(due to the fact that|owing to the fact that)\b
\b(marks? a pivotal|represents a crucial|signifies a transformative)\b
\b(not just \w+, (it's|it is)|not only \w+, (but also|but))\b
\b(the future looks bright|exciting times lie ahead)\b
\b(experts believe|critics argue|observers note) (that )?(it|this)\b
\b(serves? as|functions? as|acts? as) (a|an)\b
```

---

## Severity Levels

| Level | Examples | Action |
|-------|----------|--------|
| **Critical** | Chatbot artifacts, factual errors | Must fix |
| **High** | Buzzwords, inflated language | Should fix |
| **Medium** | Passive voice, empty transitions | Fix if easy |
| **Low** | Minor intensifiers | Optional |

---

## References

- Wikipedia: "Signs of AI writing" (WikiProject AI Cleanup)
- blader/humanizer GitHub project
- Community pattern research
