# Needs Testing Tracker

> **Purpose**: Track claims, hypotheses, and questions that need systematic verification.
>
> **Status**: Living document - updated as tests are completed and new questions arise.
>
> **Want to help?** Pick a test from the High Priority section and follow the [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md)!

---

## Table of Contents

- [How to Use This Document](#how-to-use-this-document)
- [High Priority Tests](#high-priority-tests)
- [Medium Priority Tests](#medium-priority-tests)
- [Low Priority Tests](#low-priority-tests)
- [Completed Tests](#completed-tests)
- [How to Contribute](#how-to-contribute)

---

## How to Use This Document

### Priority Levels

**🔴 High Priority** — Fundamental claims affecting main guidance
- Used frequently in documentation
- High impact on user outcomes
- Multiple documents reference this claim

**🟡 Medium Priority** — Valuable but less critical
- Used in specific contexts
- Moderate impact on outcomes
- Helpful but not essential

**🟢 Low Priority** — Nice to know, low urgency
- Edge cases or advanced topics
- Limited impact on typical users
- Theoretical interest

### Test Status

- **❓ UNTESTED** — No systematic testing yet
- **🧪 IN PROGRESS** — Someone is currently testing (note who)
- **✅ COMPLETED** — Test finished, results documented (link to findings)

---

## High Priority Tests

### 1. Technical vs Descriptive Term Consistency

**Priority**: 🔴 High
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md)

**Claim**: Technical terms like "120 BPM" produce more consistent results than descriptive terms like "fast tempo"

**Current Evidence**: 💭 HYPOTHESIS — Logical inference, no testing

**Why It Matters**: Central to interpretability framework, affects all user guidance

**Test Needed**:
- Compare variance: "120 BPM" vs "fast tempo" (n=10 each)
- Measure actual BPM with detect_bpm.py
- Calculate standard deviation for each
- Test across multiple genres

**Estimated Time**: 2-3 hours (20 generations + analysis)

**Related Tests**: Also test with other parameters (key, time signature)

---

### 2. "Building Intensity" vs "Crescendo" Effectiveness

**Priority**: 🔴 High
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md)

**Claim**: "Crescendo" (technical) produces clearer dynamic changes than "building intensity" (descriptive)

**Current Evidence**: 💭 HYPOTHESIS — Based on training data assumptions

**Why It Matters**: Example used throughout interpretability guide

**Test Needed**:
- Generate 10 samples per prompt
- Measure dB range between start and end of section
- Compare clarity/consistency of dynamic change
- Rate subjective quality (1-5 scale)

**Estimated Time**: 3-4 hours (20 generations + analysis + audio measurement)

---

### 3. Instrument Exclusion Success Rates

**Priority**: 🔴 High
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md), [suno-tags.md](platforms/suno-tags.md)

**Claim**: Negative instructions ("no drums") fail 50-70% of the time

**Current Evidence**: ❓ UNKNOWN — Specific percentage claimed but not sourced

**Why It Matters**: Users waste credits if this advice is wrong

**Test Needed**:
- Test "no drums" alone (n=20)
- Test "piano only" positive framing (n=20)
- Test combination "piano only, no drums" (n=20)
- Define clear pass/fail criteria upfront
- Calculate actual success rates

**Estimated Time**: 5-6 hours (60 generations + analysis)

**Note**: High N needed for reliable percentage claims

---

### 4. Front-Loading Effectiveness

**Priority**: 🔴 High
**Status**: ❓ UNTESTED
**Source**: [prompt-guide.md](prompting/prompt-guide.md)

**Claim**: "Place your most important instructions at the beginning. Front-load critical information like genre, mood, and primary instruments. Early tokens carry more weight in conditioning."

**Current Evidence**: 💭 HYPOTHESIS — Common NLP principle, but not verified for music models

**Why It Matters**: Affects fundamental prompting advice

**Test Needed**:
- Create matched pairs: "Piano, jazz, slow" vs "Slow, jazz, piano"
- Test 10+ arrangements
- Measure which element dominates in output
- Control for all other variables

**Estimated Time**: 4-5 hours (50+ generations + analysis)

**Challenge**: Defining "dominance" objectively

---

### 5. Suno Meta Tag Reliability

**Priority**: 🔴 High
**Status**: ❓ UNTESTED
**Source**: [suno-tags.md](platforms/suno-tags.md)

**Claim**: Meta tags ([Energy: X], [Mood: X]) have 60-70% reliability

**Current Evidence**: 👥 ANECDOTAL — Based on ~30-40 community reports, sample size unclear

**Why It Matters**: v5 feature, many users asking about reliability

**Test Needed**:
- Test each meta tag type separately:
  - [Energy: Low] vs [Energy: High] (n=10 each)
  - [Mood: Dark] vs [Mood: Bright] (n=10 each)
  - [Instrumentation: Piano only] (n=20)
- Define success criteria per tag type
- Calculate actual reliability per tag
- Document failure modes

**Estimated Time**: 8-10 hours (80+ generations + analysis)

**Note**: Large test, could be divided among multiple testers

---

## Medium Priority Tests

### 6. Poetic/Metaphorical Prompt Effectiveness

**Priority**: 🟡 Medium
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md)

**Claim**: Phrases like "Like a summer breeze" produce sensible results despite seeming abstract

**Current Evidence**: 👥 ANECDOTAL — One user report, worked consistently for them

**Why It Matters**: Expands understanding of what prompts work, but not high-impact on typical usage

**Test Needed**:
- Test "Like a summer breeze" (n=10)
- Test equivalent literal prompt "Light, airy, gentle" (n=10)
- Compare audio characteristics
- Test other metaphors: "Sounds of thunder", "Morning light", etc.
- Establish pattern: which metaphors work?

**Estimated Time**: 4-5 hours (40+ generations + analysis)

---

### 7. "Soft Heavy Metal" Genre Modifier Consistency

**Priority**: 🟡 Medium
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md)

**Claim**: "Soft heavy metal" produces gentler metal tones while maintaining structure

**Current Evidence**: 👥 ANECDOTAL — One user report

**Why It Matters**: Challenges assumption about "contradictory" prompts, but specific use case

**Test Needed**:
- "Soft heavy metal" vs "Heavy metal" vs "Hard heavy metal" (n=5 each)
- Measure:
  - Distortion levels (spectral analysis)
  - Tempo consistency
  - Genre characteristics maintained
- Test with other genres: "Soft punk", "Hard folk", etc.

**Estimated Time**: 3-4 hours (15 generations + audio analysis)

---

### 8. Transformation Examples Actual Effectiveness

**Priority**: 🟡 Medium
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md) — Transformation Examples section

**Claim**: "Improved" prompts produce better results than original prompts

**Current Evidence**: 💭 HYPOTHESIS — Labeled as UNTESTED in document

**Why It Matters**: If transformations don't help, guidance is misleading

**Test Needed**:
- Test each transformation pair (7 examples in doc)
- Example: "Building intensity" vs "Crescendo, layered guitars..."
- Measure consistency and quality for each
- Determine if "improved" version is actually better

**Estimated Time**: 8-10 hours (70+ generations + analysis)

**Note**: Large test, can be divided by example

---

### 9. BPM Drift Quantification

**Priority**: 🟡 Medium
**Status**: ❓ UNTESTED
**Source**: Multiple documents claim "±5-10 BPM drift"

**Claim**: BPM specifications drift by ±5-10 BPM from target

**Current Evidence**: 👥 ANECDOTAL — Commonly reported, but not measured systematically

**Why It Matters**: Sets user expectations for BPM accuracy

**Test Needed**:
- Test multiple BPM targets: 80, 100, 120, 140, 160 BPM (n=10 each)
- Measure actual BPM with detect_bpm.py
- Calculate drift range per target BPM
- Determine if drift is consistent across tempos

**Estimated Time**: 4-5 hours (50 generations + analysis)

---

### 10. Parenthetical Instructions in Suno

**Priority**: 🟡 Medium
**Status**: ❓ UNTESTED
**Source**: [suno.md](platforms/suno.md), [suno-tags.md](platforms/suno-tags.md)

**Claim**: Suno adheres to ONE instruction in parentheses; multiple instructions confuse the model

**Current Evidence**: 👥 ANECDOTAL — Community observation

**Why It Matters**: Affects how users write parenthetical instructions

**Test Needed**:
- Test single instruction: "(30 seconds maximum)" (n=10)
- Test multiple: "(30 seconds, piano only, quiet)" (n=10)
- Measure which instructions are followed
- Determine if order matters

**Estimated Time**: 3-4 hours (20 generations + duration measurement)

---

## Low Priority Tests

### 11. Cultural Reference Effectiveness

**Priority**: 🟢 Low
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md)

**Claim**: Cultural references like "90s grunge" have moderate (⭐⭐⭐) training data grounding

**Current Evidence**: 💭 HYPOTHESIS

**Why It Matters**: Interesting but not essential for typical users

**Test Needed**:
- Test "90s grunge" vs literal breakdown
- Test various cultural references
- Compare to literal equivalent descriptions

**Estimated Time**: 3-4 hours

---

### 12. Novel Genre Combinations

**Priority**: 🟢 Low
**Status**: ❓ UNTESTED
**Source**: [prompt-interpretability.md](prompting/prompt-interpretability.md)

**Claim**: "Trap meets classical" type prompts have weak/inconsistent associations

**Current Evidence**: 💭 HYPOTHESIS

**Why It Matters**: Edge case, experimental usage

**Test Needed**:
- Test various novel combinations
- Measure consistency
- Determine patterns in what works

**Estimated Time**: 4-5 hours

---

### 13. [Long Intro] Duration Consistency

**Priority**: 🟢 Low
**Status**: ❓ UNTESTED
**Source**: [suno-tags.md](platforms/suno-tags.md)

**Claim**: [Long Intro] may extend intro to 20-30 seconds but is inconsistent

**Current Evidence**: 👥 ANECDOTAL

**Why It Matters**: Useful feature but not critical

**Test Needed**:
- Test [Long Intro] vs [Intro] (n=10 each)
- Measure actual intro durations
- Calculate variance and mean length

**Estimated Time**: 2-3 hours

---

## Completed Tests

### ✅ Bar Count Specifications (Duration Tags)

**Status**: ✅ COMPLETED
**Date**: 2025-11-15
**Tester**: @thirteenth_mang (Braeden)
**Findings**: [Suno Bar Timing Research Report](../research/suno_bar_timing_research_report.md)

**Result**: ✅ VERIFIED — Bar count specifications do NOT work

**Evidence**:
- n=12 controlled tests
- 166-575% error rates
- Actually INCREASES randomness vs control
- Recommendation: Abandon bar-based timing approach

**Evidence Label**: VERIFIED

---

### ✅ Absolute Second-Level Timing

**Status**: ✅ COMPLETED
**Date**: 2025-11-15
**Tester**: @thirteenth_mang (Braeden)
**Findings**: [Controlling AI Music Generation Timing Research](../research/controlling_ai_music_generation_timing.md)

**Result**: ✅ VERIFIED — Architectural limitation, cannot be done with text alone

**Evidence**:
- Technical analysis of model architectures
- Compression rates (400-4000x)
- Training data structure analysis
- Platform comparison (Suno, Udio, Stable Audio, MusicGen)

**Evidence Label**: VERIFIED

---

## How to Contribute

### 1. Pick a Test

Choose from High or Medium priority tests above, or propose a new one.

### 2. Announce You're Testing

- Comment on [this issue](#) or
- Start a [discussion thread](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/discussions)
- Update this document with "🧪 IN PROGRESS — @yourusername"

### 3. Follow the Protocol

Use the [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md) template.

### 4. Share Your Results

- Submit via [Pull Request](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/pulls)
- Or create an [issue with test results](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new)
- Include completed test template and audio examples

### 5. Update Documentation

Once VERIFIED:
- Update relevant documentation files
- Add VERIFIED label with link to your findings
- Move test from "Needs Testing" to "Completed" section here

---

## Proposing New Tests

Think we should test something not listed here?

**Submit a proposal with:**
1. What claim needs testing (be specific)
2. Where the claim appears in documentation
3. Why it matters (impact on users)
4. Rough test design (how you'd measure it)
5. Estimated effort (hours, number of generations)

[Propose a new test](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new?title=Test%20Proposal:)

---

## Test Coordination

### Avoiding Duplicate Effort

Before starting a test:
1. Check this document for "🧪 IN PROGRESS"
2. Search [closed issues](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues?q=is%3Aissue+is%3Aclosed) for similar tests
3. Ask in [Discussions](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/discussions)

### Collaborating on Large Tests

Some tests (like #5: Suno Meta Tag Reliability) are large and can be divided:
- One person tests Energy tags
- Another tests Mood tags
- Another tests Instrumentation tags
- Combine results for comprehensive finding

**Want to collaborate?** Start a discussion thread for coordination.

---

## Questions?

- **"How do I use the testing tools?"** — See [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md)
- **"What makes a good test?"** — Clear hypothesis, controlled variables, sufficient N, objective measurement
- **"My results are unclear"** — Report them anyway! Mark as ⚠️ INCONCLUSIVE and explain limitations
- **"Can I test on platforms other than Suno?"** — Yes! We need cross-platform data. Note platform clearly.

---

## See Also

- [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md) — Systematic testing methodology
- [Evidence Standards](evidence-standards.md) — How we label claim quality
- [Prompt Interpretability](prompting/prompt-interpretability.md) — Framework with many untested claims
- [Contributing Guidelines](../CONTRIBUTING.md) — General contribution process

---

**Last Updated**: 2025-11-25

**Tests Completed**: 2
**Tests In Progress**: 0
**Tests Needed**: 13+ (and growing as we discover new questions!)
