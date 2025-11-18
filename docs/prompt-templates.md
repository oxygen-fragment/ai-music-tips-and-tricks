# Prompt Templates Library

> ⚠️ **Status**: In Progress - Being actively developed
>
> **Platform Compatibility:** Templates are tagged with compatible platforms

Ready-to-use prompt templates for common AI music generation scenarios. Copy, customize, and create!

---

## Table of Contents

- [How to Use Templates](#how-to-use-templates)
- [Template Format](#template-format)
- [Genre Templates](#genre-templates)
- [Structure Templates](#structure-templates)
- [Mood/Energy Templates](#moodenergy-templates)
- [Instrumentation Templates](#instrumentation-templates)
- [Vocal Templates](#vocal-templates)
- [Experimental Templates](#experimental-templates)

---

## How to Use Templates

### Quick Start

1. Find a template that matches your goal
2. Copy the template
3. Replace `[PLACEHOLDERS]` with your content
4. Adjust parameters to taste
5. Generate!

### Template Notation

- `[REQUIRED]` - You must fill this in
- `{OPTIONAL}` - Can be removed if not needed
- `#SETTING: value` - Platform setting recommendation
- `✅ Tested` - Verified to work
- `⚠️ Experimental` - Not fully tested

---

## Template Format

Each template includes:
- **Platform** compatibility
- **Use case** description
- **Template** code
- **Settings** recommendations
- **Example** filled out
- **Expected result**
- **Tips** for customization

---

## Genre Templates

### Pop Song

**Platforms:** ✅ Suno | ⚠️ Udio (untested) | ⚠️ Producer.ai (untested)

**Use Case:** Radio-friendly pop song with verse-chorus structure

**Template:**
```
Style: upbeat pop, catchy melody, [YOUR_GENRE_MODIFIERS]
#SETTING: Weirdness 30-50%
#SETTING: Style Influence 70-80%

[intro]
{instrumental description}

[verse 1]
[YOUR_VERSE_1_LYRICS]

[pre-chorus]
[YOUR_PRE_CHORUS_LYRICS]

[chorus]
[YOUR_CHORUS_LYRICS]

[verse 2]
[YOUR_VERSE_2_LYRICS]

[pre-chorus]
[YOUR_PRE_CHORUS_LYRICS]

[chorus]
Repeat

[bridge]
[YOUR_BRIDGE_LYRICS]

[chorus]
Repeat

[outro]
{fade out or ending lyrics}
```

**Example:**
```
Style: upbeat pop, catchy melody, dance-pop, synthesizers

[intro]
(Bright synths, building energy)

[verse 1]
Walking down the boulevard
City lights and beating hearts

[pre-chorus]
Feel the rhythm start to grow
Let the music take control

[chorus]
We're dancing till the morning light
Everything will be alright
Let go of all your worries now
This is our moment, here and now

[verse 2]
Neon signs and summer nights
Everything just feels so right

[pre-chorus]
Feel the rhythm start to grow
Let the music take control

[chorus]
Repeat

[bridge]
In this moment, we're alive
Feel the energy inside

[chorus]
Repeat

[outro]
(Fade out with synth melody)
```

**Expected Result:**
- 2:30-3:00 duration
- Clear verse-chorus structure
- Upbeat, danceable tempo
- Catchy hook in chorus

**Customization Tips:**
- Add `(electronic drums)` or `(live drums)` to intro for specificity
- Adjust style field: `indie pop`, `synth-pop`, `dream pop`
- For Suno v5, add `[Energy: High]` before chorus

---

### Trap Beat

**Platforms:** ✅ Suno | ⚠️ Udio (untested) | ⚠️ Producer.ai (untested)

**Use Case:** Authentic trap instrumental with proper tempo

**Template:**
```
Style: [70-80] BPM trap, rolling hi-hats, 808 bass, [MOOD_MODIFIERS]
#SETTING: Weirdness 40-60%
#SETTING: Style Influence 70-85%

[intro]
(Instrumental - [YOUR_INTRO_ELEMENTS])

[verse]
{YOUR_LYRICS_OR_LEAVE_BLANK_FOR_INSTRUMENTAL}

[hook]
{YOUR_HOOK}

[verse]
{YOUR_LYRICS_OR_LEAVE_BLANK_FOR_INSTRUMENTAL}

[hook]
Repeat

[outro]
(Fade with 808)
```

**Example:**
```
Style: 70 BPM dark trap, rolling hi-hats, 808 bass, ominous pads

[intro]
(Instrumental - dark synth pad, minimal hi-hats)

[verse]

[hook]

[verse]

[hook]
Repeat

[outro]
(Fade with 808 bass slide)
```

**Expected Result:**
- Slow, heavy kick pattern (70-80 BPM)
- Fast, rolling hi-hats creating double-time feel
- Deep 808 bass hits
- Atmospheric, dark vibe

**Customization Tips:**
- **Important:** Use 70-80 BPM, NOT 140 BPM ([see why](../samples/beats/trap.md#the-trap-tempo-paradox))
- Add `pitched 808 slides` for melodic trap
- Specify `triplet hi-hats` for complex patterns
- For Suno v5: `[Instrumentation: 808 bass, rolling hi-hats, minimal kick]`

---

### Acoustic Singer-Songwriter

**Platforms:** ✅ Suno | ⚠️ Udio (untested) | ⚠️ Producer.ai (untested)

**Use Case:** Intimate acoustic performance

**Template:**
```
Style: acoustic, singer-songwriter, [YOUR_MOOD], [YOUR_VOCAL_STYLE]
#SETTING: Weirdness 20-40%
#SETTING: Style Influence 60-75%

[intro]
(Acoustic guitar, finger-picking)

[verse 1]
[YOUR_VERSE_1_LYRICS]

[chorus]
[YOUR_CHORUS_LYRICS]

[verse 2]
[YOUR_VERSE_2_LYRICS]

[chorus]
Repeat

[bridge]
[YOUR_BRIDGE_LYRICS]

[chorus]
Repeat

[outro]
(Guitar fade)
```

**For Suno v5, add:**
```
[Instrumentation: Acoustic guitar only]
[Mood: Intimate, vulnerable]
[Vocal Style: Soft, close-mic'd]
```

**Expected Result:**
- Warm acoustic guitar
- Intimate vocal performance
- Minimal production
- Emotional delivery

---

### Electronic Dance Music (EDM)

**Platforms:** TODO

**Template:**
```
TODO
```

---

### Rock Band

**Platforms:** TODO

**Template:**
```
TODO
```

---

### Jazz Standard

**Platforms:** TODO

**Template:**
```
TODO
```

---

### Classical/Orchestral

**Platforms:** TODO

**Template:**
```
TODO
```

---

## Structure Templates

### Simple Verse-Chorus

**Use Case:** Basic song structure for beginners

**Template:**
```
[verse 1]
[YOUR_LYRICS]

[chorus]
[YOUR_LYRICS]

[verse 2]
[YOUR_LYRICS]

[chorus]
Repeat

[outro]
```

---

### Verse-PreChorus-Chorus

**Use Case:** Build anticipation before chorus

**Template:**
```
[verse 1]
[YOUR_LYRICS]

[pre-chorus]
[BUILD_UP_LYRICS]

[chorus]
[YOUR_LYRICS]

[verse 2]
[YOUR_LYRICS]

[pre-chorus]
[BUILD_UP_LYRICS]

[chorus]
Repeat

[outro]
```

---

### Complex Structure with Bridge

**Use Case:** Full song with dynamic structure

**Template:**
```
[intro]
{instrumental}

[verse 1]
[YOUR_LYRICS]

[pre-chorus]
[YOUR_LYRICS]

[chorus]
[YOUR_LYRICS]

[verse 2]
[YOUR_LYRICS]

[pre-chorus]
[YOUR_LYRICS]

[chorus]
Repeat

[bridge]
[CONTRASTING_SECTION]

[breakdown]
{optional instrumental break}

[chorus]
Repeat

[outro]
```

---

## Mood/Energy Templates

> 🚧 **Suno v5+ Only** - These use meta tags

### Intimate to Explosive

**Use Case:** Dramatic dynamic range

**Template:**
```
[verse]
[Energy: Low]
[Mood: Intimate, vulnerable]
[Instrumentation: Piano only, reverb]
[YOUR_QUIET_LYRICS]

[pre-chorus]
[Energy: Building]
[Instrumentation: Add strings, light percussion]
[BUILD_UP_LYRICS]

[chorus]
[Energy: Maximum]
[Mood: Triumphant, powerful]
[Instrumentation: Full band, heavy drums]
[YOUR_POWERFUL_LYRICS]
```

**See:** [Quiet Verse/Explosive Chorus sample](../samples/dynamics/quiet-verse-explosive-chorus.md)

---

### Gradual Build

**Use Case:** Slowly increasing intensity

**Template:**
```
[verse 1]
[Energy: Minimal]
[Instrumentation: [SOLO_INSTRUMENT] only]
[YOUR_LYRICS]

[verse 2]
[Energy: Low]
[Instrumentation: Add [SECOND_INSTRUMENT]]
[YOUR_LYRICS]

[chorus]
[Energy: Medium]
[Instrumentation: Add [THIRD_INSTRUMENT]]
[YOUR_LYRICS]

[verse 3]
[Energy: Building]
[Instrumentation: Add [FOURTH_INSTRUMENT]]
[YOUR_LYRICS]

[chorus]
[Energy: Maximum]
[Instrumentation: Full arrangement]
Repeat
```

---

### Dark and Brooding

**Template:**
```
[Energy: Low to Medium]
[Mood: Dark, ominous, tension]
[Instrumentation: [YOUR_DARK_INSTRUMENTS]]

[YOUR_STRUCTURE_HERE]
```

**Instrument suggestions:**
- Deep 808 bass
- Dark synth pads
- Minor key piano
- Distorted guitar

---

## Instrumentation Templates

> 🚧 **Suno v5+ Only**

### Solo to Full Band Progression

**Template:**
```
[intro]
[Instrumentation: [SOLO_INSTRUMENT] only]

[verse 1]
[Instrumentation: [SOLO_INSTRUMENT] only]

[verse 2]
[Instrumentation: Add [INSTRUMENT_2]]

[chorus]
[Instrumentation: Full band - [LIST_ALL_INSTRUMENTS]]
```

---

### Stripped Back Acoustic

**Template:**
```
[Instrumentation: Acoustic guitar only, natural reverb]

{OR}

[Instrumentation: Piano only, room reverb]

{OR}

[Instrumentation: [YOUR_SOLO_INSTRUMENT] only]
```

**Works best with:**
- Acoustic guitar
- Piano
- Harpsichord
- Accordion
- See [full list](platforms/suno-tags.md#instruments-that-work-well-solo)

---

### Orchestral Arrangement

**Template:**
```
[Instrumentation: String section, brass section, woodwinds, timpani]

{OR for specific}

[Instrumentation: Violin, cello, French horn, flute, orchestral percussion]
```

---

### Electronic Production

**Template:**
```
[Instrumentation: Synthesizer, electronic drums, synth bass, ambient pads]

{OR}

[Instrumentation: 808 bass, drum machine, synth leads, arpeggiator]
```

---

## Vocal Templates

### A Cappella

**Platforms:** ✅ Suno

**Template:**
```
Style: a cappella, vocal only, no instruments

[YOUR_STRUCTURE]
[YOUR_LYRICS]
```

**See:** [A cappella sample](../samples/vocals/acapella.md)

---

### Alternating Vocal Styles

**Platforms:** ✅ Suno

**Template:**
```
[YOUR_ROLE_1]: [LYRICS]
[YOUR_ROLE_2]: [LYRICS]
[YOUR_ROLE_1]: [LYRICS]
[YOUR_ROLE_2]: [LYRICS]
```

**Example:**
```
Lead: I'm walking through the fire
Choir: Walking through the fire
Lead: Nothing can stop me now
Choir: Nothing can stop us now
```

**Credit:** [@mixofthings](https://suno.com/@mixofthings)

---

### Whispered Vocals

**Platforms:** ✅ Suno

**Template:**
```
[reading to a church]
[YOUR_LYRICS_TO_BE_WHISPERED]
```

**Credit:** [@mixofthings](https://suno.com/@mixofthings)

---

### Powerful Belt

**Platforms:** ⚠️ Suno v5 (untested)

**Template:**
```
[Vocal Style: Powerful belt, soaring]
[YOUR_CLIMACTIC_LYRICS]
```

---

## Experimental Templates

> ⚠️ **Status:** These are untested or community-reported

### Genre Blending

**Template:**
```
Style: [GENRE_1] meets [GENRE_2], [SHARED_ELEMENTS]

Example: trap meets classical, orchestral strings with 808 bass
```

---

### Dynamic Tempo Changes

**Template:**
```
TODO - Research if tempo changes work mid-song
```

---

### Spoken Word with Music

**Template:**
```
Style: spoken word, [GENRE], [MOOD]

[verse]
[SPOKEN_WORD_LYRICS_NO_MELODY]

[instrumental]
(Musical interlude)
```

---

## Contributing Templates

Have a template that works great? Share it!

**What to include:**
1. Template code
2. Platform(s) tested on
3. Example output (link to audio)
4. Settings used
5. Tips for customization

[Submit via GitHub Issue](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new)

---

## Template Requests

Need a template for a specific use case?

**Current requests:**
- TODO - Add community requests

[Request a template](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new?title=Template%20Request:)

---

## See Also

- [Prompt Guide](prompting/prompt-guide.md) - Prompting principles
- [Suno Tags Reference](platforms/suno-tags.md) - All available tags
- [Sample Library](../samples/) - Real examples
- [Platform Comparison](platform-comparison.md) - Platform-specific features
