# Dialect and Accent Control Experiments

## Overview

Testing whether phonetic spelling and dialect variations in lyrics can control vocal accent and pronunciation in AI-generated music.

**Platform:** Suno
**Discovery Date:** 2025-11-24
**Status:** 🧪 Active Testing

---

## Initial Discovery

**Hypothesis:** Lyrics written in different dialects/phonetic spellings will produce vocals with matching accents.

### Test 1: UK vs US vs Jamaican Patois

**Control Phrase:** "You are my favorite/favourite color"

| Variation | Lyrics | Expected Accent | Result | Audio Link | Notes |
|-----------|--------|----------------|---------|------------|-------|
| US Standard | "You are my favorite color" | General American | [Status] | [Link] | Baseline |
| UK Standard | "You are my favourite colour" | British RP | [Status] | [Link] | UK spelling test |
| Jamaican Patois | "Yu a fi mi favorite color" | Jamaican | ✅ SUCCESS | [Link] | **Produced Jamaican accent!** |

**Key Finding:** Jamaican Patois phonetic spelling successfully triggered Jamaican accent. This suggests lyric spelling controls vocal delivery.

---

## Experiment Set 1: Dialect Control Test

**Objective:** Test if various English dialects can be controlled through phonetic spelling.

**Base phrase:** "I'm going to the store right now"

**Genre:** Pop, upbeat (consistent across all tests to isolate dialect variable)

### Test Matrix

| Test ID | Dialect | Lyrics | Expected Accent | Success (1-5) | Audio Link | Notes |
|---------|---------|--------|----------------|---------------|------------|-------|
| D1 | Standard American | "I'm going to the store right now" | General American | - | - | Baseline |
| D2 | Cockney | "Oi'm goin' to the shop roight now, innit" | London Cockney | - | - | |
| D3 | Scottish | "Ah'm gonnae the shop the noo" | Scottish | - | - | |
| D4 | Irish | "I'm goin' to the shop now, so I am" | Irish | - | - | |
| D5 | Southern US | "Ah'm fixin' to go to the sto' right now, y'all" | Southern drawl | - | - | |
| D6 | Australian | "I'm headin' to the servo right now, mate" | Australian | - | - | |
| D7 | New York | "I'm goin' to the staw right now" | NYC accent | - | - | |

**Success Rating:**
- 1 = No accent detected, sounds generic
- 2 = Slight inflection
- 3 = Noticeable accent
- 4 = Strong accent
- 5 = Perfect native-sounding accent

---

## Experiment Set 2: Phonetic Pronunciation Control

**Objective:** Test if phonetic spelling forces specific pronunciations of ambiguous words.

### Test 2A: Route

| Test ID | Spelling | Expected Pronunciation | Success | Audio Link | Notes |
|---------|----------|----------------------|---------|------------|-------|
| P1 | "route" | (random - root or rowt) | - | - | Control |
| P2 | "rowt" | "ROWT" | - | - | Forced US pronunciation |
| P3 | "root" | "ROOT" | - | - | Forced UK pronunciation |

### Test 2B: Tomato

| Test ID | Spelling | Expected Pronunciation | Success | Audio Link | Notes |
|---------|----------|----------------------|---------|------------|-------|
| P4 | "tomato" | (random) | - | - | Control |
| P5 | "tuh-MAY-toe" | US pronunciation | - | - | Forced phonetic |
| P6 | "tuh-MAH-toe" | UK pronunciation | - | - | Forced phonetic |

---

## Experiment Set 3: Extreme Phonetic Spelling

**Objective:** Find the breaking point - how extreme can phonetic spelling get before the model fails?

**Base phrase:** "I want to dance with you tonight"

| Test ID | Phonetic Level | Lyrics | Expected Result | Success | Audio Link | Notes |
|---------|----------------|--------|----------------|---------|------------|-------|
| E1 | Standard | "I want to dance with you tonight" | Clear pronunciation | - | - | Baseline |
| E2 | Casual | "I wanna dance with you tonight" | Slightly casual | - | - | |
| E3 | Moderate | "I wanna danz witchu tuhnite" | Slurred/casual accent | - | - | |
| E4 | Extreme | "Ah wunna daynz witchoo tuhnyt" | Heavy accent/slur | - | - | |
| E5 | Maximum | "Uh wuh daynz witchoo t'nyt" | Extreme slur/mumble | - | - | Breaking point test |

---

## Experiment Set 4: Mixed Dialect Within Song

**Objective:** Test if accent can be switched between song sections.

**Song Structure:**

```
Style: Pop, emotional, dynamic

[Verse 1 - Jamaican]
Yu a fi mi favorite color
Mi love di way yu shine
[phonetic: Jamaican Patois]

[Chorus - Standard]
You are my favorite color
I love the way you shine
[phonetic: Standard American]

[Verse 2 - Southern US]
You're mah fav'rit color, darlin'
Ah love the way y'all shine
[phonetic: Southern drawl]

[Bridge - Cockney]
You're my fav'rit colour, innit
Love the way you shine, mate
[phonetic: London Cockney]
```

| Test ID | Structure | Result | Audio Link | Notes |
|---------|-----------|--------|------------|-------|
| M1 | Full mixed structure | - | - | Does it switch accents per section? |
| M2 | Two-way (Patois + Standard) | - | - | Simpler test |
| M3 | Two-way (Southern + Standard) | - | - | Alternative simpler test |

---

## Experiment Set 5: Slang Density Test

**Objective:** Test if slang concentration affects vocal style/delivery.

**Genre:** Hip-hop, laid-back (consistent across all)

| Test ID | Slang Level | Lyrics | Expected Delivery | Success | Audio Link | Notes |
|---------|-------------|--------|------------------|---------|------------|-------|
| S1 | None | "That's really good, I like it" | Neutral/sung | - | - | Baseline |
| S2 | Light | "That's dope, I like it" | Slightly casual | - | - | |
| S3 | Medium | "That's fire, I'm vibing with it" | Hip-hop inflection | - | - | |
| S4 | Heavy | "Yo that's straight fire fam, I'm deadass vibing with this joint, no cap" | Full hip-hop delivery | - | - | |

---

## Experiment Set 6: Genre + Dialect Matching

**Objective:** Test if matching dialect to culturally-associated genre reinforces accent effect.

| Test ID | Genre | Dialect | Lyrics | Hypothesis | Success | Audio Link | Notes |
|---------|-------|---------|--------|------------|---------|------------|-------|
| G1 | Reggae | Jamaican Patois | "Yu a fi mi favorite color" | Strong Jamaican accent | - | - | Matched pair |
| G2 | Classical | Jamaican Patois | "Yu a fi mi favorite color" | Weaker accent (conflict) | - | - | Mismatched pair |
| G3 | Country | Southern US | "You're mah fav'rit color darlin'" | Strong Southern drawl | - | - | Matched pair |
| G4 | EDM | Southern US | "You're mah fav'rit color darlin'" | Weaker accent (conflict) | - | - | Mismatched pair |
| G5 | UK Grime | Cockney | "You're my fav'rit colour innit" | Strong Cockney accent | - | - | Matched pair |
| G6 | NYC Drill | NYC slang | "Deadass you my favorite color" | Strong NYC accent | - | - | Matched pair |

**Hypothesis:** Genre-dialect cultural match should amplify accent effect.

---

## Experiment Set 7: Non-English Language Test

**Objective:** Test pronunciation quality and consistency in non-English lyrics.

**Base phrase:** "I love you very much, my love" (same meaning, different languages)

**Genre:** Romantic pop ballad (consistent)

| Test ID | Language | Lyrics | Expected | Success (1-5) | Audio Link | Notes |
|---------|----------|--------|----------|---------------|------------|-------|
| L1 | Spanish | "Te quiero mucho, mi amor" | Spanish pronunciation | - | - | |
| L2 | French | "Je t'aime beaucoup, mon amour" | French pronunciation | - | - | |
| L3 | Italian | "Ti amo tanto, amore mio" | Italian pronunciation | - | - | |
| L4 | German | "Ich liebe dich sehr, mein Schatz" | German pronunciation | - | - | |
| L5 | Japanese | "愛してるよ、僕の愛" | Japanese pronunciation | - | - | Can it handle non-Latin script? |

---

## Experiment Set 8: Punctuation & Emphasis Control

**Objective:** Test if punctuation affects vocal delivery and emphasis.

**Genre:** Pop, emotional

| Test ID | Punctuation Style | Lyrics | Expected Effect | Success | Audio Link | Notes |
|---------|------------------|--------|----------------|---------|------------|-------|
| PU1 | Neutral | "You are my favorite color" | Normal delivery | - | - | Baseline |
| PU2 | ALL CAPS emphasis | "You ARE my favorite color" | Emphasis on "ARE" | - | - | |
| PU3 | Ellipsis pauses | "You... are my favorite color" | Dramatic pause | - | - | |
| PU4 | Exclamation staccato | "You! Are! My! Favorite! Color!" | Staccato/punchy | - | - | |
| PU5 | Tilde elongation | "You are my favorite color~" | Elongated last word | - | - | Anime-style? |
| PU6 | Multiple punctuation | "You are my favorite color!!!" | Very emphatic | - | - | |

---

## Comprehensive Tests (Recommended)

**Issue with short phrases:** Initial testing showed mixed results with short phrases like "You are my favorite color." Not enough phonetic material for model to establish consistent accent.

**Solution:** Full song structures (verse + chorus) provide larger sample size for accent to emerge clearly.

**See:** [Comprehensive Dialect Tests](./dialect-comprehensive-tests.md) - 18 full-length tests with complete lyrics

### Available Test Sets:

1. **"Summer Rain"** - Same song in 5 dialects (American, Jamaican, Southern, Cockney, Australian)
2. **"City Lights"** - Progressive phonetic intensity (5 levels from standard to maximum)
3. **Genre-Dialect Matching** - 6 matched/mismatched pairs testing cultural reinforcement
4. **Mixed Sections** - Accent switching between song sections

---

## Testing Protocol

### Standard Test Procedure

1. **Generation Settings:**
   - Platform: Suno v4 or v5 (document which)
   - Mode: Custom
   - Instrumental: Off (unless testing instrumental)
   - Keep genre consistent within experiment set

2. **Prompt Format:**
   ```
   Style: [Genre tags]
   Lyrics: [Test lyrics with phonetic spelling]
   ```

3. **Documentation:**
   - Record Suno URL
   - Note generation date
   - Rate success (1-5 scale)
   - Document unexpected behaviors
   - Save audio file locally for backup

4. **Success Criteria:**
   - Clear accent/pronunciation difference from baseline
   - Matches expected dialect characteristics
   - Consistent throughout clip (doesn't drift)

---

## Analysis Framework

### Qualitative Assessment

For each test, evaluate:

1. **Accent Authenticity** (1-5)
   - Does it sound like native speaker?
   - Are characteristic sounds present?

2. **Consistency** (1-5)
   - Does accent hold throughout?
   - Or does it drift to generic?

3. **Clarity** (1-5)
   - Is vocal intelligible?
   - Or does phonetic spelling create artifacts?

4. **Overall Success** (1-5)
   - Does technique reliably control accent?
   - Would you recommend this approach?

### Quantitative Measures (Optional)

- Formant analysis (F1, F2 vowel space)
- Pitch contour analysis
- Rhythm/timing patterns
- Spectral comparison

---

## Findings Summary

*(To be filled in as experiments complete)*

### What Works

- ✅ Jamaican Patois spelling produces Jamaican accent (confirmed)
- [ ] [Other successful techniques]

### What Doesn't Work

- [ ] [Failed approaches]

### Reliability Ratings

| Technique | Success Rate | Recommended? | Notes |
|-----------|-------------|--------------|-------|
| Patois spelling | TBD | ✅ Yes | Initial test successful |
| Other dialects | TBD | - | Testing in progress |

### Best Practices

*(To be documented after testing)*

---

## Applications

### Use Cases for Accent Control

1. **Cultural Authenticity** - Match vocal style to genre origins (Reggae with Patois, Country with Southern accent)
2. **Character Differentiation** - Different accents for different "characters" in narrative songs
3. **Pronunciation Control** - Force specific word pronunciations
4. **Stylistic Effect** - Create unique vocal character through deliberate dialect choice

### Integration with Other Techniques

- Combine with genre tags for reinforcement
- Use with vocal style tags (breathy, powerful, etc.)
- Apply to specific song sections via structure tags

---

## Related Experiments

- [Shattered Sky](./shattered-sky.md) - Dynamic build experiment
- [UK vs US Spelling Impact](../todo.md#line-13) - Original hypothesis from TODO

---

## Contributing

If you test these experiments:

1. Follow the standard test procedure above
2. Document your results in the tables
3. Include audio links (or note if keeping private)
4. Submit PR or open issue with findings

**Credit:** Initial discovery during research session 2025-11-24

---

## Questions for Further Research

- Does this work in Udio? Other platforms?
- Can you combine multiple dialects in harmony? (backing vocals in different accent)
- Does training data include specific dialect examples, or is this emergent behavior?
- How does this interact with the Style field vs Lyrics field?
- Can you control accent strength with "light" vs "heavy" phonetic spelling?

---

## References

- [Suno Platform Guide](../docs/platforms/suno.md)
- [Prompt Guide](../docs/prompting/prompt-guide.md)
- [Music Prompting Deep Research](../docs/prompting/music-prompting-deep-research.md)
