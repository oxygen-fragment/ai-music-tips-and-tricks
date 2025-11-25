# Prompt Interpretability: What AI Music Models Actually Understand

> **Status**: In Development — Evidence labels being added
>
> **Last Updated**: 2025-11-25
>
> **⚠️ Evidence Standard Notice**: This document contains a mix of verified facts, hypotheses, and anecdotal observations. Claims are labeled with evidence quality:
> - ✅ **VERIFIED** — Tested in our research or documented in official sources
> - 💭 **HYPOTHESIS** — Logical inference, needs testing to confirm
> - 👥 **ANECDOTAL** — Community reports, not systematically tested
> - ❓ **UNKNOWN** — We don't know yet, needs research
>
> See [Evidence Standards](../evidence-standards.md) for details on how we label claims.

Understanding how AI music models "see" your prompts is the key to writing effective instructions. Not all prompts are created equal—some are crystal clear to the model while others are ambiguous or even architecturally impossible to execute.

This guide provides a **framework for evaluating prompt interpretability**: how "machine-readable" your instructions are, and how likely they are to produce your intended results.

**Note**: This is a theoretical framework to help you think about prompts. Many claims need systematic testing to verify.

---

## Table of Contents

- [Why This Matters](#why-this-matters)
- [The Four Dimensions of Interpretability](#the-four-dimensions-of-interpretability)
  - [1. Specificity Spectrum](#1-specificity-spectrum)
  - [2. Architectural Support](#2-architectural-support)
  - [3. Training Data Grounding](#3-training-data-grounding)
  - [4. Semantic Clarity](#4-semantic-clarity)
- [Interpretability Labels: Quick Reference](#interpretability-labels-quick-reference)
- [Transformation Examples: Improving Your Prompts](#transformation-examples-improving-your-prompts)
- [Platform-Specific Considerations](#platform-specific-considerations)
- [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)
- [Quick Reference Tables](#quick-reference-tables)

---

## Why This Matters

💭 **HYPOTHESIS**: When you write a prompt like **"Building intensity"**, the AI model:
- Has weaker associations (less likely in structured training metadata)
- Understands *trajectory* but not *specifics*
- Produces more variable results

💭 **HYPOTHESIS**: When you write **"120 BPM, distorted guitar, crescendo"**:
- Has stronger associations (likely present in structured metadata)
- Understands specific audio characteristics
- Produces more consistent results (though BPM may drift ±5-10)

**The difference?** Interpretability. The second prompt uses terms more likely to be in training data with clear audio correlates. The first prompt is relative—the model must infer meaning.

❓ **UNKNOWN**: The actual consistency difference between these prompt types hasn't been systematically measured. Needs A/B testing with variance analysis (n=10+ per prompt type).

---

## The Four Dimensions of Interpretability

Prompt interpretability isn't binary (good/bad). It exists across four key dimensions:

### 1. Specificity Spectrum

💭 **HYPOTHESIS**: Prompt effectiveness correlates with specificity. More specific terms likely have stronger, more structured representations in training data.

**How precise vs. vague is your instruction?**

| Level | Characteristics | Examples | Model Understanding |
|-------|----------------|----------|-------------------|
| **⭐⭐⭐⭐⭐ Quantified Parameters** | Measurable, objective, numeric | `120 BPM`, `Dm key`, `4/4 time` | Very High<br/>*But output may drift ±5-10%* |
| **⭐⭐⭐⭐ Technical Music Terms** | Industry-standard terminology | `Crescendo`, `Staccato`, `Arpeggio`, `Syncopation` | High<br/>*Strong training data associations* |
| **⭐⭐⭐⭐ Specific Descriptors** | Clear, concrete audio characteristics | `Distorted guitar`, `Rolling hi-hats`, `Warm analog synth` | High<br/>*Tied to recognizable timbres* |
| **⭐⭐⭐ General Descriptors** | Common but less specific | `Upbeat`, `Dark`, `Energetic`, `Intimate` | Medium<br/>*Understood but interpreted broadly* |
| **⭐⭐ Relative/Comparative** | Context-dependent meaning | `Building intensity`, `Gradual build`, `Getting louder` | Medium-Low<br/>*Trajectory understood, specifics vague* |
| **⭐ Abstract/Subjective** | Highly interpretive | `Emotional`, `Epic`, `Haunting`, `Atmospheric` | Low<br/>*Weak or inconsistent associations* |

**Key Insight:** As you move down this spectrum, your prompts become more open to interpretation. This isn't always bad—sometimes you *want* creative freedom—but it makes results less predictable.

---

### 2. Architectural Support

**What can the model actually do, regardless of how clearly you ask?**

This is critical: some prompts are interpretable but **architecturally impossible** to execute reliably.

| Prompt Type | Model Capability | Reliability | Evidence Status |
|-------------|------------------|-------------|----------------|
| **Section labels** | `[Intro]`, `[Verse]`, `[Chorus]` | ✅ HIGH | 📚 SOURCED: Platform documentation |
| **Genre/style tags** | `Rock`, `Jazz`, `Trap`, `Lo-fi` | ✅ HIGH | 👥 ANECDOTAL: Consistent community reports |
| **Instrument specification** | `Piano`, `808 bass`, `Distorted guitar` | ✅ MEDIUM-HIGH | 👥 ANECDOTAL: Usually works, front-loading helps |
| **Dynamic trajectories** | `Quiet to loud`, `Building intensity` | ⚠️ MEDIUM | ❓ UNKNOWN: Understood but needs consistency testing |
| **Approximate timing** | `Brief intro`, `Extended outro` | ⚠️ MEDIUM-LOW | 👥 ANECDOTAL: Unpredictable duration |
| **BPM/Key requests** | `120 BPM`, `Key of Dm` | ⚠️ MEDIUM | 👥 ANECDOTAL: ±5-10 BPM drift reported |
| **Instrument exclusion** | `No drums`, `Without percussion` | ❌ LOW | ❓ UNKNOWN: Claimed 50-70% failure, needs verification |
| **Absolute timing** | `10 seconds of X`, `[0:00-0:10]` | ❌ FAILS | ✅ VERIFIED: Architectural limitation (see below) |

✅ **VERIFIED — Critical Finding:** Absolute second-level timing is a **fundamental architectural limitation**, not a prompt engineering problem.

Source: [Controlling AI Music Generation Timing Research](../../research/controlling_ai_music_generation_timing.md)

**Why timing fails** (technical facts):
- Models compress audio 400-4000x before generation
- At 21.5 Hz (Stable Audio), each step = ~46ms of audio
- Training data lacks paired (text + timestamp + audio) annotations
- Text embeddings capture *what* (semantics), not *when* (temporal relationships)

---

### 3. Training Data Grounding

💭 **HYPOTHESIS**: Terms that appear as structured metadata in training data (genre tags, BPM fields, instrument names) have stronger, more consistent associations than descriptive phrases.

**How likely is your term to have strong associations in the model's training data?**

| Grounding Level | Examples | Model Understanding |
|----------------|----------|-------------------|
| **⭐⭐⭐⭐⭐ Standard Metadata Terms** | Genre names, section labels, common instruments | Very Strong<br/>*These ARE the training labels* |
| **⭐⭐⭐⭐ Common Production Terms** | `Reverb`, `Distortion`, `Lo-fi`, `Studio recording` | Strong<br/>*Common in music descriptions* |
| **⭐⭐⭐ Natural Descriptors** | `Energetic`, `Smooth`, `Aggressive`, `Gentle` | Moderate<br/>*Present but less technical* |
| **⭐⭐⭐ Cultural References** | `90s grunge`, `Chicago house`, `Motown soul` | Moderate<br/>*Depends on training data representation* |
| **⭐⭐ Novel Combinations** | `Trap meets classical`, `Jazz fusion with metal` | Weak<br/>*Model interpolates, results vary* |
| **⭐ Poetic/Metaphorical** | `Like a summer breeze`, `Sounds of thunder` | ❓ UNKNOWN<br/>*Seem weak but may work — see section below* |

**Pro Tip:** When in doubt, use terms that would appear in a music store category, streaming platform tag, or album liner notes. These are most likely to be in training data.

---

### Special Case: Poetic/Metaphorical Prompts That Work

👥 **ANECDOTAL**: Some seemingly abstract phrases produce sensible, consistent results despite appearing to have weak training data associations:

**Examples that work:**
- **"Like a summer breeze"** → Produces light, airy, gentle musical qualities
- **"Sounds of thunder"** → Heavy, dramatic, powerful sounds

❓ **UNKNOWN — Why this works**: We don't fully understand the mechanism. Possible explanations:

1. **Component Word Associations**:
   - "Breeze" → airy, light sounds
   - "Summer" → bright, warm tones
   - "Thunder" → deep, loud, dramatic

2. **Poetic Descriptions in Training Data**: Music descriptions often use metaphorical language. Models may learn these associations.

3. **Metaphorical Learning**: Models trained on paired text-audio learn to map metaphors to audio characteristics through statistical patterns.

**Needs systematic research:**
- Which types of metaphors work reliably?
- How consistent are results compared to literal equivalents?
- Can we predict which poetic phrases will work?
- What are the boundaries of metaphorical understanding?

**If you discover poetic prompts that work:** Please share! Include:
- Exact prompt used
- Platform and version
- Number of trials
- Audio examples
- What audio characteristics it produces

**[Submit findings here](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new)**

---

### 4. Semantic Clarity

💭 **HYPOTHESIS**: Clearer, less ambiguous instructions should produce more consistent results.

**How unambiguous is your instruction?**

| Clarity Level | Examples | Issues |
|--------------|----------|--------|
| **Unambiguous** | `Piano only`, `Instrumental toggle ON`, `808 bass` | Clear single meaning |
| **Context-Dependent** | `Loud` (how loud?), `Fast` (how fast?), `Heavy` (how heavy?) | Requires reference point model doesn't have |
| **Seemingly Conflicting** | `Soft heavy metal`, `Quiet trap`, `Slow uptempo` | *See note below* |
| **Highly Subjective** | `Emotional`, `Beautiful`, `Epic`, `Interesting` | Different associations per listener |

**Note on "Seemingly Conflicting" Prompts:**

👥 **ANECDOTAL**: Combinations like "Soft heavy metal" actually DO work and produce distinct results:
- "Soft heavy metal" → Gentler guitar tones, less distortion, but maintains metal rhythm/structure
- "Hard heavy metal" → More aggressive, more distortion

❓ **UNKNOWN**: Why these work when they seem contradictory. Possible explanations:
- Models learn that genre modifiers like "soft" adjust intensity while preserving core characteristics
- Training data contains examples of genre variations (e.g., "soft rock" vs "hard rock")
- Multi-dimensional representation allows independent control of timbre vs structure

**Needs testing**: Systematic comparison of modified genres vs unmodified (n=10+ each, measure timbre/intensity differences).

---

## Interpretability Labels: Quick Reference

Use these labels when documenting or thinking about prompts:

### 🟢 High Interpretability
**Clear, specific, well-supported by model architecture and training data**

**Examples:**
- `120 BPM`
- `Distorted guitar`
- `Rock`
- `[Verse]`
- `Crescendo`
- `808 bass`
- `Staccato strings`

**When to use:** Default choice for consistent results

---

### 🟡 Medium Interpretability
**Understood but approximate, variable, or context-dependent**

**Examples:**
- `Building intensity`
- `Dark mood`
- `Brief intro`
- `Emotional`
- `Upbeat`
- `Heavy`

**When to use:** When you want some creative freedom but still need general guidance

**Mitigation:** Combine with high-interpretability terms: `Building intensity, crescendo from 80 dB to 110 dB` → `Crescendo, increasing drum presence, layered guitars`

---

### 🔴 Low Interpretability
**Vague, subjective, or architecturally unsupported**

**Examples:**
- `Epic feel`
- `Like thunder`
- `Interesting rhythm`
- `Beautiful melody`
- `No drums` (exclusion)

**When to use:** Sparingly, if at all. High risk of unexpected results.

**Mitigation:** Transform into high/medium terms (see [Transformation Examples](#transformation-examples-improving-your-prompts))

---

### ⚫ Architecturally Impossible
**Model cannot reliably execute regardless of phrasing**

**Examples:**
- `10 seconds of piano, then 20 seconds of guitars`
- `[0:00-0:10] intro`
- `No drums` (guaranteed exclusion)
- `Exactly 142.5 BPM`

**When to use:** Don't. Use hybrid workflows instead.

**Solution:** Use multi-step generation, DAW editing, or platform-specific tools (Suno Replace Section, Udio Inpainting)

---

## Transformation Examples: Suggested Prompt Improvements

💭 **HYPOTHESIS — UNTESTED**: These examples show how to transform prompts from low to high interpretability based on the framework above. However, **these specific transformations have NOT been systematically tested**.

❓ **UNKNOWN**: Whether these "improved" prompts actually produce more consistent or desirable results. This needs A/B testing (n=10+ per prompt, comparing output variance and quality).

**Use these as starting points for experimentation, not as proven improvements.**

Here are suggested transformations:

### Example 1: Dynamic Changes

❌ **Low Interpretability:**
```
Building intensity, getting more epic as it goes
```

**Problems:**
- "Building intensity" is relative/comparative (⭐⭐)
- "Getting more epic" is abstract/subjective (⭐)
- No concrete audio characteristics specified

✅ **High Interpretability:**
```
Crescendo, layered guitars gradually entering, drums increasing from soft brush to full kit,
reaching climax with distorted power chords and crashing cymbals
```

**Improvements:**
- `Crescendo` is technical term (⭐⭐⭐⭐)
- Specific instruments named
- Clear progression: soft → full
- Concrete audio elements: brush drums → full kit, power chords, cymbals

---

### Example 2: Tempo/Energy

❌ **Low Interpretability:**
```
Fast and exciting
```

**Problems:**
- "Fast" is context-dependent (how fast?)
- "Exciting" is subjective
- No measurable reference

✅ **High Interpretability:**
```
140 BPM, uptempo, driving rhythm, energetic drum pattern, syncopated hi-hats
```

**Improvements:**
- `140 BPM` is quantified (⭐⭐⭐⭐⭐)
- `Uptempo`, `driving rhythm` are standard descriptors (⭐⭐⭐⭐)
- `Syncopated hi-hats` is specific + technical (⭐⭐⭐⭐)

---

### Example 3: Mood/Atmosphere

❌ **Low Interpretability:**
```
Emotional and haunting
```

**Problems:**
- Both terms are abstract/subjective (⭐)
- "Emotional" means different things to different people
- No audio characteristics specified

✅ **High Interpretability:**
```
Minor key, slow tempo 70 BPM, reverb-drenched piano, melancholic melody,
sparse arrangement, intimate close-mic'd vocals
```

**Improvements:**
- `Minor key` is technical (⭐⭐⭐⭐)
- `70 BPM` is quantified (⭐⭐⭐⭐⭐)
- `Reverb-drenched piano` is specific descriptor (⭐⭐⭐⭐)
- `Melancholic` more specific than "emotional" (⭐⭐⭐)
- `Sparse arrangement`, `close-mic'd` are production terms (⭐⭐⭐⭐)

---

### Example 4: Timing (The Impossible)

❌ **Architecturally Impossible:**
```
10 seconds of piano solo, then 20 seconds of full band with guitars and drums
```

**Problems:**
- Absolute timing is fundamentally unsupported (⚫)
- Timestamp syntax ignored by Suno/Udio
- Model has no concept of "10 seconds"

✅ **Workaround - Multi-Step Approach:**

**Step 1: Generate Intro**
```
Style: Minimal piano ballad, sparse, intimate
Lyrics:
[Long Instrumental Intro]
(solo piano, reflective melody, no drums, no other instruments)
```
*Result: 8-15 second intro typically*

**Step 2: Extend from Timestamp (e.g., 0:12)**
```
Style: Rock, explosive, heavy
Lyrics:
[Verse]
[Energy: High]
[Instrumentation: Distorted guitars, double bass drums, powerful bass]
```

**Alternative:** Generate sections separately, assemble in DAW with exact timing

---

### Example 5: Instrument Exclusion

❌ **Low Reliability:**
```
Piano ballad, no drums
```

**Problems:**
- Negative instructions (`no drums`) often fail (❓ UNKNOWN: claimed 50-70% but needs verification)
- Genre "ballad" may imply drums in training data

✅ **High Interpretability:**
```
Solo piano composition, unaccompanied, classical style, sparse arrangement,
intimate recording, no percussion
```

**Improvements:**
- `Solo piano` is positive specification (⭐⭐⭐⭐)
- `Unaccompanied` reinforces solo nature
- `Classical style` invokes training data where solo piano is common
- `Sparse arrangement` suggests minimal instrumentation
- Still include `no percussion` but rely on positive framing

👥 **ANECDOTAL Success rate:** ~70% with positive framing vs ~30-40% for negative-only (needs systematic verification)

---

### Example 6: Genre Modifiers vs. Complex Combinations

👥 **ANECDOTAL**: Simple genre modifiers like "Soft heavy metal" DO work:
- "Soft heavy metal" → Gentler guitar tones, less distortion, maintains metal structure
- "Hard rock" vs "Soft rock" → Models understand these as established subgenres

❌ **More Complex Combinations May Conflict:**
```
Heavy metal, soft acoustic guitar solo
```

**Problems:**
- Adding multiple conflicting elements (metal + acoustic + soft)
- Model must resolve which characteristics dominate
- Results may be inconsistent

💭 **SUGGESTED Alternative (untested):**
```
Acoustic ballad with metal-inspired intensity, clean fingerpicked guitar,
driving rhythm, powerful dynamics without distortion
```

**Reasoning:**
- Lead with primary characteristic: `Acoustic ballad`
- Clarify relationship: `metal-inspired intensity` (energy, not timbre)
- Explicit constraints: `clean`, `without distortion`
- Specify technique: `fingerpicked`

❓ **UNKNOWN**: Whether this alternative actually performs better. Needs A/B testing.

---

### Example 7: Cultural References

⚠️ **Medium Interpretability:**
```
Like 90s grunge bands
```

**Problems:**
- Assumes model knows "90s grunge" characteristics
- Cultural reference may have weak/inconsistent associations (⭐⭐⭐)

✅ **High Interpretability:**
```
Alternative rock, distorted guitars with chorus effect, raw lo-fi production,
angsty vocals, 90-110 BPM, heavy bass, dynamic quiet-loud transitions
```

**Improvements:**
- Break down cultural reference into audio characteristics
- Specific technical elements: `chorus effect`, `lo-fi production`
- Quantified tempo range
- Structural element: `quiet-loud transitions` (grunge hallmark)

---

## Platform-Specific Considerations

### Suno

**High Interpretability:**
- Section labels: `[Verse]`, `[Chorus]`, `[Bridge]`
- Meta tags (v5): `[Energy: High]`, `[Mood: Intimate]`, `[Instrumentation: Piano only]`
- Genre tags: `Rock`, `Jazz`, `Trap`
- Short, tag-like style field (4-7 descriptors optimal)

**Medium Interpretability:**
- `[Long Intro]` — extends intro but inconsistent (8-12s typical, not 20+)
- BPM specifications — model approximates but drifts ±5-10 BPM

**Low/Failing:**
- Bar counts: `(piano for 8 bars)` — proven ineffective in [research](../../research/suno_bar_timing_research_report.md)
- Multiple parenthetical instructions — model gets confused
- Timestamp syntax: `<0:00-0:10>` — ignored

**Workarounds:**
- Use `Extend from Time` for structural control
- Use `Replace Section` (Pro/Premier) for surgical edits
- Generate sections separately, assemble in DAW for exact timing

---

### Udio

**High Interpretability:**
- Incremental 30-second building — HIGH control per segment
- Section labels in lyrics field
- Manual Mode: Detailed prompts (500+ words) without preprocessor
- Inpainting: Edit 4 subsections within 28s context window

**Medium Interpretability:**
- Preprocessor Mode: AI enhances prompts, less direct control
- Dynamic descriptions work better than Suno for gradual builds

**Best Practices:**
- Build songs 30 seconds at a time for maximum control
- Use inpainting to fix specific problematic sections
- Manual Mode for experienced users, Auto for beginners

---

### Stable Audio

**High Interpretability:**
- **ONLY platform with exact duration control**: "2 minutes 13 seconds" → exactly that
- Technical production terms: `Lo-fi`, `Studio recording`, `Pristine quality`
- Structured prompt format: Genre → Instruments → Mood → BPM → Production

**Medium Interpretability:**
- Internal structure timing still approximate (can't say "drums at 0:45")

**Optimal Format:**
```
Progressive Rock | Post-rock |
Instruments: reverb guitar (primary), analog synths (supporting), minimal drums (rhythm) |
Mood: atmospheric, building tension |
125 BPM |
Production: Studio recording, modern polished, expansive reverb
```

---

### MusicGen (Meta)

**High Interpretability:**
- Technical music terminology
- Melody conditioning via chromagram (unique feature)
- Programmatic control through Python API

**Low Interpretability:**
- Short generation limit (30s native) reduces structural control
- Less polished than commercial platforms

**Best Use Case:** Research, custom training, melody-guided generation

---

## Common Pitfalls and Solutions

### Pitfall 1: Over-Reliance on Abstract Terms

**Problem:**
```
Create an epic, emotional journey that feels triumphant and inspiring
```

**Why it fails:** All abstract/subjective terms (⭐), no concrete audio characteristics

**Solution:** Translate emotions into audio characteristics
```
Orchestral arrangement, building from solo piano to full orchestra,
major key, triumphant brass fanfares, soaring string section,
powerful timpani, crescendo to climax, 110 BPM
```

---

### Pitfall 2: Expecting Precise Timing from Text Alone

**Problem:**
```
0-10 seconds: quiet piano
10-30 seconds: loud guitars
30-45 seconds: drums only
```

**Why it fails:** Fundamental architectural limitation (⚫)

**Solution:** Hybrid workflow
1. Generate separate clips for each section
2. Assemble in DAW with exact timing
3. Add crossfades and mixing

Or use platform-specific tools:
- Suno: `Extend from Time` at specific timestamps
- Udio: Incremental 30s generation + inpainting

---

### Pitfall 3: Negative Instructions (Exclusions)

**Problem:**
```
Rock song without drums, no percussion, exclude bass
```

**Why it fails:** Models trained on complete arrangements; exclusion is harder to learn than presence

**Solution:** Positive specification
```
Rock-inspired acoustic guitar solo, clean tone, fingerpicked melody,
unaccompanied, sparse arrangement, intimate
```

---

### Pitfall 4: Complex Genre + Instruction Combinations

**Note:** Simple modifiers like "Soft heavy metal" DO work (👥 ANECDOTAL). This pitfall is about more complex combinations.

**Problem:**
```
Heavy metal but make it soft and gentle
```

**Why this is tricky:**
- Instructional phrasing ("but make it") may be less effective than direct modification
- Adding multiple conflicting instructions increases ambiguity

💭 **SUGGESTED alternatives** (untested):
```
Option 1: Soft heavy metal, clean guitar tones, moderate distortion

Option 2: Power ballad, clean electric guitar, gentle dynamics, emotional vocals,
rock-inspired but intimate, 80 BPM
```

❓ **UNKNOWN**: Which approach works best. Needs testing.

---

### Pitfall 5: Too Many Instructions at Once

**Problem (especially Suno):**
```
(120 BPM, 30 seconds, piano only, no drums, quiet intro, loud ending)
```

**Why it fails:** Suno adheres to ONE instruction in parentheses; multiple confuse the model

**Solution:** Prioritize single instruction in parentheses, use other methods for rest
```
Style: Piano ballad, quiet to loud build, 120 BPM
(30 seconds maximum)

[Intro]
[Instrumentation: Piano only]
[Energy: Low]

[Outro]
[Energy: High]
```

---

## Quick Reference Tables

### When to Use Each Interpretability Level

| Your Goal | Use This Level | Why |
|-----------|---------------|-----|
| Consistent, predictable results | 🟢 High | Maximum control, minimum variation |
| Specific technical requirements | 🟢 High | BPM, key, specific instruments |
| General vibe with creative freedom | 🟡 Medium | Model interprets creatively within bounds |
| Exploration/experimentation | 🟡 Medium | Allows unexpected but interesting results |
| Avoid at all costs | 🔴 Low | High risk of missing the mark entirely |
| Precise timing control | Use hybrid workflow | Text alone cannot achieve this |

---

### Transformation Quick Guide

| Low Interpretability | → | High Interpretability |
|---------------------|---|---------------------|
| Fast | → | 140 BPM, uptempo |
| Loud | → | High energy, 110 dB, powerful drums |
| Emotional | → | Minor key, melancholic melody, intimate vocals |
| Epic | → | Orchestral, crescendo, triumphant brass, timpani |
| Building intensity | → | Crescendo, layered guitars, drums increasing |
| Cool rhythm | → | Syncopated hi-hats, off-beat accents, 95 BPM |
| No drums | → | Solo piano, unaccompanied, sparse, no percussion |
| 10 seconds of X | → | [Use multi-step workflow or DAW assembly] |

---

### Term Reliability by Platform

| Term Type | Suno | Udio | Stable Audio | MusicGen |
|-----------|------|------|--------------|----------|
| Section labels | ✅ High | ✅ High | ⚠️ Medium | ❌ Low |
| Genre tags | ✅ High | ✅ High | ✅ High | ✅ High |
| BPM | ⚠️ Medium (±5-10) | ⚠️ Medium | ✅ High | ⚠️ Medium |
| Instruments | ✅ Medium-High | ✅ High | ✅ High | ⚠️ Medium |
| "No [instrument]" | ❌ Low | ❌ Low | ❌ Low | ❌ Low |
| Exact timing | ❌ Fails | ❌ Fails | ✅ Duration only | ❌ Fails |
| Meta tags | ✅ High (v5) | ⚠️ Medium | N/A | N/A |

---

## See Also

- [Prompt Guide](prompt-guide.md) - General prompting principles and priority systems
- [Controlling AI Music Generation Timing Research](../../research/controlling_ai_music_generation_timing.md) - Deep dive into timing limitations
- [Suno Tags Reference](../platforms/suno-tags.md) - Complete tag library with reliability ratings
- [Music Terms](../fundamentals/music-terms.md) - Plain English explanations of technical terms
- [Sample Library](../../samples/) - Real examples demonstrating various techniques

---

## Contributing

Have examples of prompts that work exceptionally well or surprisingly poorly? We want to hear about them!

**What to include:**
1. The prompt you used
2. Platform and version
3. Expected vs actual result
4. Your interpretability analysis

[Submit via GitHub Issue](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new)
