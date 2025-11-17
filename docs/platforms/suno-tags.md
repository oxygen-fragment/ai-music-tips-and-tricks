# Suno Tags Reference

A comprehensive guide to Suno's bracket notation system for controlling song structure, attributes, and effects.

---

## Table of Contents

- [What Are Tags?](#what-are-tags)
- [Tag Types Overview](#tag-types-overview)
- [Structure Tags](#structure-tags-high-reliability)
- [Meta Tags (Suno v5)](#meta-tags-suno-v5)
- [Vocal Effect Tags](#vocal-effect-tags)
- [Experimental Tags](#experimental-tags-community-discoveries)
- [Known Non-Working Tags](#known-non-working-tags)
- [Tag Combination Patterns](#tag-combination-patterns)
- [Testing & Contributing](#testing--contributing)
- [Resources](#resources)

---

## What Are Tags?

Tags are special markers using **bracket notation** `[like this]` that you include in your lyrics to control various aspects of your Suno generation.

**How to use:**
```
[intro]
Instrumental opening

[verse]
Your lyrics here
Tell your story

[chorus]
The main hook
Repeating section
```

**Version compatibility:**
- **Structure tags** work in Suno v4.5+
- **Meta tags** require Suno v5+
- Check individual tag entries for specific compatibility

---

## Tag Types Overview

| Category | Reliability | Version | Use Case |
|----------|-------------|---------|----------|
| **Structure** | 95%+ | v4.5+ | Song sections (verse, chorus) |
| **Meta** | 60-70% | v5+ | Energy, mood, instrumentation |
| **Vocal Effects** | Varies | v4.5+ | Voice modulation (whisper, belt) |
| **Experimental** | Unknown | Varies | Community discoveries, needs testing |
| **Duration** | 0-40% | v4.5+ | Most don't work reliably |

---

## Structure Tags (High Reliability)

### Tested ✓ | Reliability: 95%+ | Version: v4.5+

These are the most reliable tags in Suno. Use them to define song sections.

### [intro]

**Purpose:** Marks the opening section
**Effect:** Usually instrumental or minimal vocals, sets the mood
**Example:**
```
[intro]
(Instrumental - soft piano)
```

**Variations:**
- `[Intro - Instrumental]`
- `[Piano Intro]`
- `[Long Intro]` - May extend to 20-30 seconds (⚠ inconsistent)

**Related:** See [song structure guide](/docs/fundamentals/song-structure.md)

---

### [verse] / [verse 1] / [verse 2]

**Purpose:** Marks storytelling sections
**Effect:** Lower energy than chorus, builds tension
**Example:**
```
[verse 1]
Walking down the empty street
Memories beneath my feet

[verse 2]
Now the story's come full circle
Every ending is a start
```

**Notes:**
- Numbered verses help Suno differentiate sections
- Verses typically have different lyrics each time
- Energy usually lower than chorus

---

### [chorus] / [hook]

**Purpose:** Marks the main repeating section
**Effect:** Higher energy, memorable melody
**Example:**
```
[chorus]
We're dancing in the rain
Washing away the pain
```

**Notes:**
- Usually repeats with same lyrics
- Highest energy section of the song
- `[hook]` is interchangeable with `[chorus]`

---

### [pre-chorus] / [prechorus] / [pre chorus]

**Purpose:** Build-up section before chorus
**Effect:** Creates anticipation, rising energy
**Example:**
```
[pre-chorus]
And I can feel it coming
The moment's almost here
```

**Notes:**
- All spelling variations work
- Optional but effective for tension building

---

### [bridge]

**Purpose:** Contrasting section, usually appears once
**Effect:** Different melody/progression, provides variety
**Example:**
```
[bridge]
Maybe we've been looking
At this all wrong
Time to change perspective
```

**Notes:**
- Typically appears after second chorus
- Often features different instrumentation or energy level

---

### [outro] / [ending]

**Purpose:** Closing section
**Effect:** Wind-down, resolution
**Example:**
```
[outro]
(Fade out with piano)
```

**Notes:**
- Can be instrumental or vocal
- Often mirrors the intro musically

---

### [break]

**Purpose:** Breakdown or pause in the song
**Effect:** Stripped-down instrumentation, tension release
**Example:**
```
[break]
(Drums and bass only)
```

**Notes:**
- Good for dynamic contrast
- Common in electronic and hip-hop styles

---

## Meta Tags (Suno v5)

### Tested ⚠ | Reliability: 60-70% | Version: v5+

Meta tags allow fine control over section attributes. They work **within Custom mode** and require Suno v5+.

**Important:** Meta tags have moderate reliability. Results may vary between generations.

### [Energy: Level]

**Purpose:** Controls intensity/energy of a section
**Syntax:** `[Energy: Level]`
**Levels:**
- `Minimal` - Sparse, quiet
- `Low` - Calm, subdued
- `Low-Medium` - Gentle build
- `Medium` - Moderate energy
- `High` - Energetic, driving
- `Maximum` - Intense, powerful
- `Rising` - Gradual build within section

**Example:**
```
[verse 1]
[Energy: Low]
[Mood: Intimate]
Soft whispered words in the dark
```

**Testing notes:** Works 60-70% of the time in v5. May be ignored in some generations.

---

### [Mood: Descriptor]

**Purpose:** Sets emotional tone of a section
**Syntax:** `[Mood: Descriptor]` or `[Mood: Descriptor, Additional]`
**Common values:**
- `Intimate` - Close, personal
- `Triumphant` - Victorious, uplifting
- `Vulnerable` - Exposed, emotional
- `Reflective` - Thoughtful, contemplative
- `Sparse` - Minimal, stripped back
- `Explosive` - Intense, dramatic

**Example:**
```
[chorus]
[Mood: Triumphant]
[Energy: Maximum]
We rise above the storm!
```

**Notes:** Can combine descriptors with commas: `[Mood: Vulnerable, intimate]`

---

### [Instrumentation: Description]

**Purpose:** Specifies instruments for a section
**Syntax:** `[Instrumentation: Description]`
**Examples:**
```
[Instrumentation: Piano only, reverb]
[Instrumentation: Full band, distorted guitars, heavy drums]
[Instrumentation: Soft piano, ambient pads]
[Instrumentation: Bass and light hi-hat only]
[Instrumentation: Add strings, light percussion]
```

**Notes:**
- More specific = better results
- Use "Add" to layer instruments
- "Only" for stripped-down sections
- Works better with established style in Style field

---

### [Vocal Style: Description]

**Purpose:** Controls vocal delivery characteristics
**Syntax:** `[Vocal Style: Description]`
**Examples:**
```
[Vocal Style: Breathy, close-mic'd]
[Vocal Style: Powerful belt]
[Vocal Style: Powerful belt, soaring]
[Vocal Style: Whispered]
```

**Notes:**
- Can combine multiple descriptors
- More reliable when style is consistent with overall genre
- See [Vocal Effect Tags](#vocal-effect-tags) for bracket-only alternatives

---

## Vocal Effect Tags

### Testing Status: Limited | Reliability: Unknown - Needs Community Testing

These tags modify vocal delivery. Most are **community-discovered** and need systematic testing.

### [reading to a church]

**Effect:** Creates whispered voice effect
**Example:**
```
[verse]
[reading to a church]
Dominus Lucis, abandon the dawn…
```

**Testing status:** ✓ Confirmed working
**Version:** v4.5+
**Credit:** [@mixofthings](https://suno.com/@mixofthings)
**Sample:** [Sermon of the Hollow Sun](https://suno.com/song/4c0bd323-d5e5-4849-849a-dc49d105e976)

---

### [speaking through laughter]

**Effect:** Vocals with laugh-talk quality
**Testing status:** ? Community report, needs verification
**Version:** Unknown
**Notes:** Mentioned in community experiments, no confirmed examples yet

---

### Potential Vocal Effect Tags (Untested)

Based on music terminology in the guide, these tags are **candidates for testing**:

| Tag | Expected Effect | Source |
|-----|----------------|--------|
| `[whisper]` | Whispered vocals | Timbre terminology |
| `[belt]` | Powerful, projected vocals | Found in meta tag examples |
| `[scream]` / `[screaming]` | Aggressive, distorted vocals | Distortion techniques |
| `[growl]` / `[growling]` | Low, guttural vocals | Metal/hardcore techniques |
| `[falsetto]` | High-pitched head voice | TODO item |
| `[ad-lib]` | Improvised vocal runs | TODO item |
| `[breathy]` | Airy, intimate vocals | Meta tag variation |
| `[spoken]` / `[spoken word]` | Talking instead of singing | Rap/poetry |

**Status:** None of these have been systematically tested. **We need community help to verify!**

---

## Experimental Tags (Community Discoveries)

### Testing Status: ? Untested | Submit Your Findings!

These are tags based on music terminology from the fundamentals guide that **might** work:

### Texture/Articulation Tags

| Tag | Expected Effect | Related To |
|-----|----------------|-----------|
| `[staccato]` | Short, detached notes | [Staccato guide](/docs/fundamentals/music-terms/sound-effect-textures/staccato.md) |
| `[legato]` | Smooth, connected notes | [Legato guide](/docs/fundamentals/music-terms/sound-effect-textures/legato.md) |
| `[syncopation]` | Off-beat rhythm emphasis | [Syncopation guide](/docs/fundamentals/music-terms/sound-effect-textures/syncopation.md) |
| `[arpeggio]` | Broken chord patterns | [Arpeggio guide](/docs/fundamentals/music-terms/sound-effect-textures/arpeggio-chords.md) |

### Dynamic Tags

| Tag | Expected Effect | Related To |
|-----|----------------|-----------|
| `[crescendo]` | Gradually getting louder | [Crescendo guide](/docs/fundamentals/music-terms/sound-effect-textures/crescendo-dimuendo.md) |
| `[diminuendo]` / `[decrescendo]` | Gradually getting quieter | [Dynamics guide](/docs/fundamentals/music-terms/sound-effect-textures/crescendo-dimuendo.md) |

### Effect Tags

| Tag | Expected Effect | Related To |
|-----|----------------|-----------|
| `[reverb]` | Echoey, spacious sound | [Reverb guide](/docs/fundamentals/music-terms/sound-effect-textures/reverb.md) |
| `[distortion]` | Fuzzy, overdriven sound | [Distortion guide](/docs/fundamentals/music-terms/sound-effect-textures/distortion.md) |

**Testing needed:** These tags are based on documented music terminology but haven't been confirmed to work in Suno. If you test any of these, please report your findings!

---

## Known Non-Working Tags

### Tested ✗ | Do Not Use

These tags have been **systematically tested and confirmed NOT to work** as intended.

### Bar/Measure Timing Tags

**Syntax tested:** `(element for X bars)`, `[element for X bars]`
**Expected effect:** Control duration by musical bars (e.g., "8 bars of intro")
**Actual effect:** None - actually increases randomness
**Testing:** See [bar timing research report](/research/suno_bar_timing_research_report.md)

**Evidence:**
- Untagged control: 14% variance
- Tagged with bar counts: 45-194% variance
- Conclusion: Bar tags don't work and make timing LESS predictable

**What to use instead:**
- ✓ Meta tags: `[Energy: X]`, `[Instrumentation: X]`
- ✓ Extend-from-time workflow in Suno interface
- ✓ `[Long Intro]` for extended intros (inconsistent but better than bar tags)

---

### Second/Time Duration Tags (Partial)

**Syntax:** `(X seconds)`, `[X seconds maximum]`
**Works:** ✓ In **Simple mode only** with parentheses
**Doesn't work:** ✗ In Custom mode
**Doesn't work:** ✗ With bracket notation

**Example (Simple mode):**
```
(30 seconds maximum)
```

**Reliability:** Low even when it works - Suno often ignores time constraints

---

## Tag Combination Patterns

### Pattern 1: Structure + Meta Tags (v5)

**Most reliable approach for v5:**
```
[verse]
[Energy: Low]
[Mood: Intimate]
[Instrumentation: Piano only]
Your soft, emotional lyrics
```

**Notes:**
- Place structure tag first
- Add meta tags on separate lines
- Keep meta tags simple and clear

---

### Pattern 2: Structure + Vocal Effect

**For special vocal sections:**
```
[bridge]
[reading to a church]
Whispered bridge lyrics here
```

**Notes:**
- Vocal effect tags may override meta vocal style tags
- Test which works better for your use case

---

### Pattern 3: Combined Section Descriptors

**Alternative to meta tags:**
```
[Intro: Solo Piano]
[Verse 1 - Soft, Intimate]
[Chorus - Full Band, High Energy]
```

**Reliability:** ⚠ Unknown - less tested than separate meta tags
**Format:** May work in v4.5 (doesn't require v5 meta tag support)

---

### Pattern 4: Alternating Vocals (NOT Tags)

**Special case - use prefix notation, not brackets:**
```
Choir: Ave Solis Vacuus…
Lead: I am reborn in your ruinous sun.
Choir: Deus Mortis Vocet…
Lead: Salvation bleeds where faith begun.
```

**Notes:**
- This is NOT a bracket tag - it's a lyric prefix
- Works reliably for alternating vocal styles
- Credit: [@mixofthings](https://suno.com/@mixofthings)

---

## Testing & Contributing

### Testing Methodology

When testing new tags:

1. **Control test:** Generate WITHOUT the tag (3-5 times)
2. **Tagged test:** Generate WITH the tag (3-5 times)
3. **Compare:** Look for consistent differences
4. **Document:**
   - Tag syntax used
   - Expected vs actual effect
   - Success rate (%)
   - Version tested
   - Style/genre tested

See [bar timing research methodology](/research/suno_bar_timing_test_methodology.md) for detailed testing framework.

### How to Contribute

Found a working tag? Submit a PR with:

1. **Tag name and syntax**
2. **Tested effect** (what it actually does)
3. **Examples** (link to Suno generations)
4. **Success rate** (X out of Y attempts worked)
5. **Version tested** (v4.5, v5, etc.)
6. **Your credit** (username/handle)

**Format:**
```markdown
### [your-tag]

**Effect:** What it does
**Example:**
[your-tag]
Example usage

**Testing status:** ✓ Confirmed (8/10 successful)
**Version:** v5
**Credit:** @yourusername
**Sample:** [Link](https://suno.com/...)
```

---

## Testing Status Legend

- **✓ Tested** - Multiple successful tests, reliable
- **⚠ Partially working** - Inconsistent results (50-80% success)
- **? Untested** - Community report or hypothesis, needs verification
- **✗ Confirmed non-working** - Systematically tested, doesn't work

**Reliability ratings:**
- **95%+** - Works almost always
- **60-70%** - Works more often than not, but inconsistent
- **30-50%** - Sometimes works, unreliable
- **0-20%** - Rarely or never works
- **Unknown** - Not enough data

---

## Resources

### External Guides
- [Jack Righteous: Suno AI Meta Tags Guide](https://jackrighteous.com/pages/suno-ai-meta-tags-guide) - Comprehensive v5 meta tags reference (October 2025)

### Internal Research
- [Controlling AI Music Generation Timing](/research/controlling_ai_music_generation_timing.md) - Detailed research on meta tags and timing control
- [Bar Timing Research Report](/research/suno_bar_timing_research_report.md) - Why bar tags don't work
- [Song Structure Fundamentals](/docs/fundamentals/song-structure.md) - Understanding the basics

### Community Sources
- [@mixofthings on Suno](https://suno.com/@mixofthings) - Vocal effect discoveries
- Suno Discord - Active community tag experiments

---

## Version History

- **v1.0** - Initial comprehensive tag reference
- Structure tags documented
- Meta tags (v5) documented from research
- Vocal effects from community
- Experimental tags identified
- Non-working tags documented

---

**Want to help expand this reference?** Test experimental tags and submit your findings! See [Contributing](#testing--contributing) section above.
