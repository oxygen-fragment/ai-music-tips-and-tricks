# Prompt Guide

## Priority

Left-to-right, top-to-bottom. Think of the priority of prompt terms (say, separated by commas), like a tree structure - some will have more or less equal priority. For example, when you have multiple instruments playing in concert with one another.

**Key principle:** Place your most important instructions at the beginning. Front-load critical information like genre, mood, and primary instruments. Early tokens carry more weight in conditioning.

## Prompt Interpretability

Not all prompts are created equal. Some instructions are crystal clear to AI models ("120 BPM", "Distorted guitar") while others are ambiguous or impossible to execute ("Building intensity", "10 seconds of piano").

**Understanding interpretability helps you:**
- Write prompts that produce consistent results
- Know when to use technical terms vs descriptive language
- Recognize architectural limitations (what's possible vs impossible)
- Transform vague prompts into effective ones

### Quick Interpretability Guide

- **🟢 High Interpretability** — Use these for consistent results
  - Quantified: `120 BPM`, `Dm key`
  - Technical: `Crescendo`, `Staccato`, `Syncopation`
  - Specific: `Distorted guitar`, `808 bass`, `Rolling hi-hats`

- **🟡 Medium Interpretability** — Understood but variable
  - General: `Upbeat`, `Dark`, `Energetic`
  - Relative: `Building intensity`, `Gradual build`

- **🔴 Low Interpretability** — Vague, use sparingly
  - Abstract: `Emotional`, `Epic`, `Interesting`
  - Exclusions: `No drums`, `Without bass` (50-70% failure rate)

- **⚫ Architecturally Impossible** — Cannot be done with text alone
  - Absolute timing: `10 seconds of X`, `[0:00-0:10]`
  - Guaranteed exclusions
  - Use hybrid workflows instead (multi-step generation + DAW editing)

**📖 Read the full guide:** [Prompt Interpretability: What AI Music Models Actually Understand](/docs/prompting/prompt-interpretability.md)

Learn about the four dimensions of interpretability, transformation examples, platform-specific considerations, and common pitfalls with solutions.
