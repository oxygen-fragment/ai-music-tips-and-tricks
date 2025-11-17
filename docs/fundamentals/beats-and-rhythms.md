# Beats & Rhythms

A beginner-friendly guide to tempo, BPM, time signatures, and the production technicalities that matter when working with AI music generation.

---

## The Basics

### What is BPM?

**BPM** = **Beats Per Minute**. It measures how fast a song moves.

Think of it like a heartbeat:

- **Resting heart rate**: ~60-80 BPM → Slow, calm songs (ballads, lo-fi)
- **Walking pace**: ~90-120 BPM → Medium energy (pop, rock)
- **Running pace**: ~140-180 BPM → High energy (EDM, dance, punk)

**In practice:**

- 70 BPM = Slow and chill
- 120 BPM = Danceable, energetic
- 170 BPM = Fast, intense

### Time Signatures: The Framework

Time signatures tell you how beats are grouped in each measure (or "bar").

**Common time signatures:**

| Signature | What it means | Feels like | Common in |
|-----------|---------------|------------|-----------|
| **4/4** | 4 beats per bar | **1**-2-3-4, **1**-2-3-4 | Most pop, rock, hip-hop |
| **3/4** | 3 beats per bar | **1**-2-3, **1**-2-3 | Waltzes, some ballads |
| **6/8** | 6 beats per bar (grouped in 2s) | **1**-2-3-**4**-5-6 | Ballads, some rock |

**Why this matters:**

- 6/8 and 3/4 can have the same number of beats, but 6/8 has a rolling, lilting feel while 3/4 has a stronger waltz pulse
- AI models may interpret time signatures differently, so understanding the difference helps you prompt more precisely

---

## BPM Ranges by Genre

Here's a general guide to tempo ranges across genres:

| Genre | BPM Range | Feel |
|-------|-----------|------|
| **Ballad** | 60-80 | Slow, emotional, reflective |
| **Lo-fi / Chill** | 70-90 | Relaxed, laid-back |
| **Hip-hop / Boom-bap** | 85-95 | Head-nodding, groovy |
| **Trap** | 70-80* | Slow kick/snare, fast hi-hats (see technicalities below) |
| **Pop** | 100-130 | Upbeat, catchy |
| **House** | 120-130 | Steady, danceable |
| **Techno** | 125-135 | Driving, hypnotic |
| **Drum & Bass** | 160-180* | Fast, intense (often uses half-time feel) |
| **Dubstep** | 140* | Heavy, bass-focused (half-time feel) |
| **Punk / Hardcore** | 180-200+ | Aggressive, chaotic |

*See "Production Technicalities" below for important context on these genres.

---

## Common Beat Patterns

Understanding beat patterns helps you communicate rhythm to AI more effectively.

### 4-on-the-Floor

- **What it is**: Kick drum on every beat (1, 2, 3, 4)
- **Sounds like**: Boom-boom-boom-boom
- **Common in**: House, disco, dance music
- **Example prompt**: "Upbeat 125 BPM house track with four-on-the-floor kick pattern"

### Boom-Bap

- **What it is**: Kick on 1 and 3, snare on 2 and 4
- **Sounds like**: BOOM-bap-BOOM-bap
- **Common in**: Classic hip-hop, lo-fi beats
- **Example prompt**: "90 BPM boom-bap hip-hop beat with punchy snare"

### Trap Pattern

- **What it is**: Sparse kick/snare (70-80 BPM), rapid hi-hats (double-time or triple-time rolls)
- **Sounds like**: Slow BOOM...crack... with fast tktktktktk hi-hats
- **Common in**: Modern hip-hop, trap
- **Example prompt**: "70 BPM trap beat with rolling hi-hats and 808 bass"

### Breakbeat

- **What it is**: Syncopated, funky drum pattern (not straight like 4-on-the-floor)
- **Sounds like**: Irregular, groove-oriented
- **Common in**: Jungle, drum & bass, some hip-hop
- **Example prompt**: "100 BPM breakbeat with syncopated snare hits"

### Waltz (3/4)

- **What it is**: Strong beat on 1, lighter on 2 and 3
- **Sounds like**: **ONE**-two-three, **ONE**-two-three
- **Common in**: Ballads, classical, folk
- **Example prompt**: "3/4 waltz at 90 BPM with piano and strings"

### Shuffle / Swing

- **What it is**: Triplet-based rhythm (not straight eighth notes)
- **Sounds like**: da-DAH-da, da-DAH-da (swung, bouncy)
- **Common in**: Blues, jazz, some rock
- **Example prompt**: "120 BPM blues shuffle with swing feel"

---

## Production Technicalities: What You Need to Know

This section addresses the **production vs perception gap**—when the "technical" BPM differs from how the music actually feels.

Understanding these nuances will help you avoid common confusions when prompting AI (and also help you hold your own when someone nitpicks your terminology).

### Understanding "Felt Tempo" vs "Actual Tempo"

**The core issue:** Sometimes the BPM that a producer uses in their DAW (Digital Audio Workstation) is NOT the same as the BPM the listener perceives.

This happens because of **rhythmic density**—how fast the most prominent rhythmic elements are moving.

---

### The Trap Paradox: 70 BPM or 140 BPM?

**The confusion:**

- Someone says "140 BPM trap" → They probably mean the hi-hat speed
- A producer says "70 BPM trap" → They mean the actual project tempo

**What's actually happening:**

- Trap is produced at **70-80 BPM** (that's the kick drum and snare tempo)
- But the **hi-hats** are programmed at **double-time** (140-160 BPM feel)
- So the kick/snare hits every 0.75-0.86 seconds (slow), while hi-hats fire every 0.21-0.25 seconds (fast)

**Why this matters for AI prompting:**

- If you say **"140 BPM trap"**, AI might give you a track where the KICK is at 140 BPM (which would be way too fast for trapthat's techno speed)
- If you say **"70 BPM trap with rolling hi-hats"**, you'll get the authentic slow kick + fast hi-hat combo

**Correct prompting:**

- ✅ "70 BPM trap beat with rolling hi-hats and 808 bass"
- ✅ "Slow trap beat around 75 BPM with double-time hi-hat rolls"
- ❌ "140 BPM trap" (AI might make it too fast)

---

### Half-Time vs Double-Time

These are **rhythmic illusions** where the tempo stays the same, but the perceived speed changes.

#### Half-Time

**What it is:** The drums play at half speed while the BPM stays the same.

**Example:**

- A 170 BPM drum & bass track goes into "half-time"
- The kick/snare now hit at 85 BPM (every other beat)
- But the hi-hats and bass are still at 170 BPM
- Result: Feels slower and heavier, even though the BPM didn't change

**Common in:** Drum & bass breakdowns, dubstep drops, some hip-hop

**Prompting for half-time:**

- ✅ "170 BPM drum and bass with half-time breakdown"
- ✅ "140 BPM dubstep with heavy half-time drop"

#### Double-Time

**What it is:** The drums play twice as fast while the BPM stays the same.

**Example:**

- A 90 BPM boom-bap track switches to double-time
- Snare now hits on every beat instead of just 2 and 4
- Feels like 180 BPM even though the project tempo is still 90

**Common in:** Hip-hop, jazz, transitions in electronic music

**Prompting for double-time:**

- ✅ "90 BPM hip-hop beat with double-time snare section"
- ✅ "Boom-bap track that switches to double-time for the hook"

---

### Quick Reference: Common Tempo Confusions

| Genre | Producer Tempo | Perceived Tempo | Why the Difference |
|-------|----------------|-----------------|-------------------|
| **Trap** | 70-80 BPM | 140-160 BPM | Double-time hi-hats create fast feel |
| **Dubstep** | 140 BPM | 70 BPM | Half-time drums (kick/snare every other beat) |
| **Half-time DnB** | 170-180 BPM | 85-90 BPM | Drums play at half speed during breakdowns |
| **Boom-bap** | 90 BPM | 90 BPM | Straightforward (no timing tricks) |
| **House** | 125 BPM | 125 BPM | Straightforward 4-on-the-floor |

---

### Genre Tempo Conventions to Know

Some genres have **systematic tempo quirks** that can trip you up:

#### Hip-Hop Sub-Genres

- **Boom-bap**: 85-95 BPM (actual tempo = perceived tempo)
- **Trap**: 70-80 BPM (but feels faster due to hi-hats)
- **Drill**: 60-70 BPM (but with aggressive hi-hat patterns)

#### Electronic Music

- **Dubstep**: 140 BPM (but half-time drums make it feel like 70 BPM)
- **Drum & Bass**: 170-180 BPM (often uses half-time for drops)
- **House**: 120-130 BPM (straightforward)
- **Techno**: 125-135 BPM (straightforward)

---

### Time Signature Quirks

Sometimes the time signature affects how a tempo *feels*, even at the same BPM.

#### 6/8 vs 3/4: Same Beats, Different Feel

Both have 6 beats, but they're grouped differently:

**3/4 (Waltz):**

- **Grouped as:** [**1** 2 3] [**1** 2 3]
- **Feels like:** Strong-weak-weak, Strong-weak-weak
- **Example:** Classic waltz, country ballad

**6/8 (Compound meter):**

- **Grouped as:** [**1** 2 3 **4** 5 6]
- **Feels like:** Rolling, lilting, two pulses per bar
- **Example:** "We Are the Champions" by Queen, many ballads

**At the same BPM:**

- 90 BPM in 3/4 = clear waltz pulse
- 90 BPM in 6/8 = smoother, more flowing

**Why this matters:**

- If you want a waltz, specify **3/4**
- If you want a rolling ballad feel, specify **6/8**
- Don't assume AI will know which you mean

---

## In AI Prompts: How to Communicate Tempo Effectively

### Be Specific About What You Want

| L Vague |  Clear |
|---------|---------|
| "Fast trap beat" | "70 BPM trap with double-time hi-hats and 808 bass" |
| "Slow dubstep" | "140 BPM dubstep with heavy half-time drop" |
| "Upbeat pop" | "120 BPM pop with four-on-the-floor kick" |

### Common Prompting Mistakes to Avoid

**Mistake 1: Confusing perceived tempo with actual tempo**

- ❌ "140 BPM trap" → Might give you kick drums at 140 (too fast!)
- ✅ "70 BPM trap with rolling hi-hats"

**Mistake 2: Not specifying the beat pattern**

- ❌ "120 BPM electronic" → Could be house, techno, breakbeat, anything
- ✅ "120 BPM house with four-on-the-floor kick"

**Mistake 3: Assuming genre = tempo**

- ❌ "Trap beat" → Could be 60 BPM, could be 80 BPM
- ✅ "75 BPM trap beat"

### Examples of Clear Tempo Requests

**For trap:**

- "70 BPM trap beat with 808 bass, rolling hi-hats, and minimal kick pattern"

**For boom-bap:**

- "90 BPM boom-bap hip-hop beat with punchy snare on 2 and 4"

**For dubstep:**

- "140 BPM dubstep with aggressive bass wobbles and half-time drop"

**For house:**

- "125 BPM deep house with four-on-the-floor kick and smooth synth pads"

**For drum & bass:**

- "174 BPM liquid drum and bass with breakbeat pattern and atmospheric pads"

---

## Terminology Bridge: Producer vs Beginner Language

One of this guide's goals is to **bridge the gap** between production terminology and beginner understanding.

When there's a difference between "technically correct" and "commonly understood," I'll document both:

| Producer Says | Beginner Hears | Reality |
|---------------|----------------|---------|
| "70 BPM trap" | "That sounds fast though?" | Hi-hats are double-time (140 BPM feel) |
| "140 BPM dubstep" | "That sounds slow though?" | Drums are half-time (70 BPM feel) |
| "6/8 ballad" | "Isn't that just slow?" | It's about the rolling feel, not just speed |
| "Swing 16ths" | "What does that mean?" | Hi-hats with a triplet bounce |

**Why this matters:**

- You're not "wrong" to describe trap as feeling like 140 BPMthat's the hi-hat speed
- But if you're prompting AI or talking to producers, knowing the "technical" 70 BPM helps
- This guide teaches you **both languages** so you can communicate effectively

---

## Further Reading

- [Song Structure](song-structure.md) - How tempo and rhythm interact with song sections
- [Tempo](music-terms/sound-elements/tempo.md) - Deep dive into tempo terminology
- [Rhythm](music-terms/sound-elements/rhythm.md) - Rhythm patterns and syncopation
- [Music Terms Index](music-terms.md) - Full glossary of music terminology

---

**Contributing:**
Found a tempo/rhythm technicality that tripped you up? Submit a PR with:

1. The confusion (what you thought vs what it actually means)
2. An example showing the difference
3. How to prompt AI correctly for what you want

Let's build the resource we all wish existed when we started.
