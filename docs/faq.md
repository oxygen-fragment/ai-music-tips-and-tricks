# Frequently Asked Questions (FAQ)

> ⚠️ **Status**: In Progress - Being actively developed

---

## Table of Contents

- [Getting Started](#getting-started)
- [Platform Choice](#platform-choice)
- [Prompting](#prompting)
- [Music Theory](#music-theory)
- [Technical Questions](#technical-questions)
- [Legal & Copyright](#legal--copyright)
- [Cost & Credits](#cost--credits)

---

## Getting Started

### Do I need music theory knowledge to use this guide?

**Answer:** No! This guide is specifically designed for people without formal music training. All music terms are explained in plain English in the [Fundamentals](fundamentals/) section.

---

### Which platform should I start with?

**Answer:** TODO - Add recommendation with reasoning
- Suno: Best for... (TODO)
- Udio: Best for... (TODO)
- Producer.ai: Best for... (TODO)

**See Also:** [Platform Comparison](platform-comparison.md)

---

### How long does it take to generate a song?

**Answer:** TODO - Add timing information per platform

---

## Platform Choice

### Suno vs Udio vs Producer.ai - Which is better?

**Answer:** TODO - Add nuanced comparison

**See detailed comparison:** [Platform Comparison](platform-comparison.md)

---

### Can I use multiple platforms for one project?

**Answer:** TODO

---

### Which platform has the best vocals?

**Answer:** TODO - Add comparison data

---

### Which platform gives the most control?

**Answer:** TODO - Add comparison data

---

## Prompting

### Why does the same prompt give different results?

**Answer:** TODO - Explain AI randomness, seed values, platform variations

---

### How detailed should my prompts be?

**Answer:** TODO - Add guidance on prompt complexity

**See Also:** [Prompt Guide](prompting/prompt-guide.md)

---

### Should I specify BPM in prompts?

**Answer:** Generally yes, but with caveats:
- Most genres have standard BPM ranges
- Some genres have paradoxes (see [Trap Tempo Paradox](../samples/beats/trap.md#the-trap-tempo-paradox))
- TODO: Add more guidance

---

### Do commas matter in prompts?

**Answer:** TODO - Add research on prompt parsing

---

### What's the difference between Style field and Lyrics field?

**Answer:** TODO - Platform-specific answers

---

## Music Theory

### What's the difference between tempo and rhythm?

**Answer:**
- **Tempo**: How fast the song is (BPM)
- **Rhythm**: The pattern of beats and accents

**See:** [Tempo](fundamentals/music-terms/sound-elements/tempo.md) | [Rhythm](fundamentals/music-terms/sound-elements/rhythm.md)

---

### What does "cadence" mean?

**Answer:** The way a musical phrase ends - either resolved (feels complete) or unresolved (feels like it needs to continue).

**See:** [Cadence Guide](fundamentals/music-terms/musical-techniques/cadence.md)

---

### What's a "bar" or "measure"?

**Answer:** TODO - Add clear explanation with examples

**Note:** Bar timing tags don't work reliably in Suno. See [Bar Timing Research](../research/suno_bar_timing_research_report.md)

---

### Can I specify key signature (like C major)?

**Answer:** TODO - Test and document per platform

---

## Technical Questions

### Can I download the generated audio?

**Answer:** TODO - Per platform permissions

---

### What audio format do I get?

**Answer:** TODO - Per platform specifications

---

### Can I edit the generated music?

**Answer:** TODO - Platform capabilities

---

### How do I extend a song?

**Answer:**
- **Suno:** TODO
- **Udio:** TODO

---

### Can I remix or vary a generation?

**Answer:** TODO - Per platform

---

## Legal & Copyright

### Do I own the music I generate?

**Answer:** TODO - Per platform license terms (requires legal review)

**Important:** Always check the current terms of service for each platform.

---

### Can I use AI-generated music commercially?

**Answer:** TODO - Per platform license terms (requires legal review)

---

### Do I need to credit the AI platform?

**Answer:** TODO - Per platform requirements

---

### Can I copyright AI-generated music?

**Answer:** TODO - Complex legal question, provide links to resources

---

## Cost & Credits

### How much does each platform cost?

**Answer:** TODO - Current pricing per platform (note: prices change)

| Platform | Free Tier | Paid Tiers | Credits System |
|----------|-----------|------------|----------------|
| Suno | TODO | TODO | Yes (see [Suno Guide](platforms/suno.md#credits)) |
| Udio | TODO | TODO | TODO |
| Producer.ai | TODO | TODO | TODO |

---

### What uses credits in Suno?

**Answer:** See [Suno Credits Guide](platforms/suno.md#credits) for detailed breakdown.

---

### Can I get free credits?

**Answer:**
- **Suno:** 50 bonus credits once per day when you go below 10 credits
- **Udio:** TODO
- **Producer.ai:** TODO

---

### What's the most credit-efficient way to iterate?

**Answer:** TODO - Strategies for efficient iteration

---

## Advanced Questions

### Can I control specific instruments?

**Answer:** Yes, using instrumentation tags:
- **Suno v5:** `[Instrumentation: piano only]`
- See [Comprehensive Instrument Reference](platforms/suno-tags.md#comprehensive-instrument-reference)

---

### How reliable are experimental tags?

**Answer:** Varies significantly. Check [Suno Tags Reference](platforms/suno-tags.md) for testing status of specific tags.

---

### Can I make solo instrument tracks?

**Answer:** Yes. See [Instruments That Work Well Solo](platforms/suno-tags.md#instruments-that-work-well-solo) for tested instruments.

---

### Why don't bar timing tags work in Suno?

**Answer:** Research shows bar count specifications (like "8 bars of intro") actually increase timing variance rather than control it. See [Bar Timing Research Report](../research/suno_bar_timing_research_report.md) for detailed methodology and findings.

---

## Still Have Questions?

- Check the [Troubleshooting Guide](troubleshooting.md)
- Review platform-specific guides: [Suno](platforms/suno.md) | [Udio](platforms/udio.md)
- Search [GitHub Issues](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues)
- [Open a new issue](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new) with your question
