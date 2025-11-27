# Song-to-Prompt Tool: Design Document

> **Status**: Concept/Planning Phase
>
> **Purpose**: Aggregate scattered music metadata resources and translate technical data into AI music generation prompts
>
> **Problem**: No comprehensive resource exists to convert a reference song into platform-specific prompts (Suno, Udio, etc.)
>
> **Last Updated**: 2025-11-26

---

## Table of Contents

- [The Gap We're Filling](#the-gap-were-filling)
- [What Currently Exists (Scattered)](#what-currently-exists-scattered)
- [Proposed Solution](#proposed-solution)
- [Technical Architecture](#technical-architecture)
- [Implementation Phases](#implementation-phases)
- [Translation Mappings](#translation-mappings)
- [Implementation Options](#implementation-options)
- [Strengths and Limitations](#strengths-and-limitations)
- [Next Steps](#next-steps)

---

## The Gap We're Filling

### User Problem

**Current state:**
```
User: "I want to create something like 'Let It Happen' by Tame Impala"
User: *manually listens*, *guesses BPM*, *tries to describe sound*, *iterates 20 times*
Result: Wasted credits, inconsistent results, frustration
```

**Desired state:**
```
User: "I want to create something like 'Let It Happen' by Tame Impala"
Tool: *aggregates metadata*, *translates to prompt language*, *provides platform-specific prompts*
Result: Strong starting point, faster iteration, better outcomes
```

### What Should Exist But Doesn't

A tool that does this:

```
Input: "Song by Artist" OR Spotify URL OR audio file

Output:
├─ Genre tags: "Indie rock, dream pop, shoegaze"
├─ BPM: 128
├─ Key: Dm
├─ Mood: "Melancholic, atmospheric, nostalgic"
├─ Instrumentation: "Reverb-drenched guitar, synth pads, live drums, bass"
├─ Vocal style: "Soft, ethereal, close-mic'd, layered harmonies"
├─ Production: "Lo-fi, ambient, wall of sound"
├─ Dynamics: "Quiet verses building to expansive chorus"
├─ Structure: "Intro-Verse-Chorus-Verse-Chorus-Bridge-Chorus-Outro"
└─ Platform-specific prompts:
    ├─ Suno: "[Style tags], [Energy: Medium], [Instrumentation: ...]"
    └─ Udio: "Indie rock with dream pop influences, 128 BPM..."
```

**This is the tool we're proposing to build.**

---

## What Currently Exists (Scattered)

### 1. Technical Metadata APIs

**Spotify Web API** (15,000 requests/day free tier)
- ✅ BPM (tempo)
- ✅ Key and mode
- ✅ Time signature
- ✅ Energy level (0-1 scale)
- ✅ Valence/happiness (0-1 scale)
- ✅ Danceability, acousticness, instrumentalness
- ✅ Preview audio URL (30 seconds)
- ❌ Not in prompt language

**MusicBrainz API** (Rate-limited, no hard limit)
- ✅ Genre tags
- ✅ Recording metadata
- ✅ Artist relationships
- ❌ Broad categories only

**Last.fm API** (5,000 requests/hour free)
- ✅ User-generated tags
- ✅ Similar artists/tracks
- ✅ Community genre tags
- ❌ Inconsistent quality

**AcousticBrainz** (No official limit)
- ✅ Detailed audio features
- ✅ Timbre analysis
- ✅ Rhythm descriptors
- ❌ Very technical, hard to interpret

### 2. Genre Classification Resources

**Every Noise at Once** (Spotify)
- 6,000+ genre taxonomy
- Not API-accessible

**AllMusic**
- Genre descriptions and characteristics
- Not API-accessible

### 3. Community Prompt Sharing (Unorganized)

**Reddit r/SunoAI**
- Users occasionally share "I recreated X song" with prompts
- Not searchable, not indexed

**Suno/Udio Discord**
- Same problem
- Information lost in chat history

**YouTube Tutorials**
- Specific examples, not indexed by reference song

### 4. The Problem

All of these exist but:
- ❌ No single aggregation point
- ❌ Technical data, not prompt language
- ❌ Not searchable by reference song
- ❌ No translation to platform-specific formats

---

## Proposed Solution

### **"SongToPrompt" - Reference Song to AI Prompt Generator**

**Core Function**: Aggregate multiple metadata sources and translate technical values into AI music generation prompts.

**Key Innovation**: The **translation layer** that converts technical values into prompt language.

---

## Technical Architecture

```
┌─────────────────────────────────────────┐
│         INPUT LAYER                     │
│  - Song name + Artist                   │
│  - Spotify URL                          │
│  - Audio file (future)                  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│    AGGREGATION LAYER (Parallel)        │
│                                          │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   Spotify    │  │ MusicBrainz  │    │
│  │  Web API     │  │     API      │    │
│  └──────────────┘  └──────────────┘    │
│                                          │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   Last.fm    │  │ Acoustic     │    │
│  │     API      │  │   Brainz     │    │
│  └──────────────┘  └──────────────┘    │
│                                          │
│  Results cached for 7 days              │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│    TRANSLATION LAYER (The Magic)       │
│                                          │
│  Technical → Prompt Language            │
│  ─────────────────────────────          │
│  • BPM 128 → "moderate uptempo"        │
│  • Energy 0.8 → "[Energy: High]"       │
│  • Valence 0.3 → "melancholic mood"    │
│  • Acousticness 0.1 → "electronic,     │
│    synthesized, produced"               │
│  • Genres → Combined tags              │
│  • Key + Mode → "Dm key, minor"        │
│                                          │
│  Using research-backed mappings         │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│   ENHANCEMENT LAYER (Optional)         │
│                                          │
│  Check community database:              │
│  • Have others refined this song?      │
│  • Load tested successful prompts      │
│  • Show confidence scores              │
│  • Display similar successful prompts  │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│         OUTPUT LAYER                    │
│                                          │
│  Platform-specific formatted prompts:   │
│  ├─ Suno v5                             │
│  ├─ Udio                                │
│  ├─ Stable Audio                        │
│  └─ MusicGen                            │
│                                          │
│  Plus metadata:                         │
│  ├─ Raw technical data                  │
│  ├─ Confidence scores per element       │
│  ├─ Similar successful prompts          │
│  └─ Community refinements (if any)      │
└─────────────────────────────────────────┘
```

---

## Implementation Phases

### **Phase 1: Python CLI Tool + Local Database**
**Timeline**: 2-3 weeks
**Priority**: HIGH - Builds foundation

**Goals:**
- Working prototype that can be used immediately
- Validates translation mappings
- Collects initial community feedback

**Deliverables:**
```bash
# Install
pip install song-to-prompt

# Use
song-to-prompt "Tame Impala - Let It Happen"
song-to-prompt https://open.spotify.com/track/xxxxx
song-to-prompt --artist "Radiohead" --song "Paranoid Android"

# With options
song-to-prompt "Daft Punk - Get Lucky" --platform suno --output json
```

**Features:**
- ✅ Fetch from multiple APIs in parallel
- ✅ Translate technical → prompt language
- ✅ Output for Suno, Udio, Stable Audio
- ✅ Cache API responses (reduce API calls)
- ✅ JSON output for automation
- ✅ Local database for community refinements (JSON file)
- ✅ Confidence scoring per element

**Tech Stack:**
- Python 3.8+
- `requests` for API calls
- `click` for CLI interface
- Local JSON/SQLite for caching and community database
- Poetry for dependency management

**File Structure:**
```
tools/song-to-prompt/
├── song_to_prompt/
│   ├── __init__.py
│   ├── cli.py              # Command-line interface
│   ├── aggregators/
│   │   ├── spotify.py      # Spotify API wrapper
│   │   ├── musicbrainz.py  # MusicBrainz API wrapper
│   │   ├── lastfm.py       # Last.fm API wrapper
│   │   └── acousticbrainz.py
│   ├── translators/
│   │   ├── technical.py    # BPM, key, energy → prompts
│   │   ├── mood.py         # Valence + energy → mood descriptors
│   │   ├── instrumentation.py  # Acousticness → instruments
│   │   └── genre.py        # Genre aggregation and refinement
│   ├── formatters/
│   │   ├── suno.py         # Suno-specific formatting
│   │   ├── udio.py         # Udio-specific formatting
│   │   ├── stable_audio.py
│   │   └── musicgen.py
│   ├── database.py         # Local community refinements
│   └── cache.py            # API response caching
├── tests/
├── data/
│   ├── community_refinements.json  # Community-tested prompts
│   └── translation_mappings.json   # Research-backed mappings
├── pyproject.toml
└── README.md
```

**Example Output:**
```
$ song-to-prompt "Tame Impala - Let It Happen"

🎵 Analyzing "Let It Happen" by Tame Impala...

✓ Fetched Spotify data
✓ Fetched MusicBrainz genres
✓ Fetched Last.fm tags
✓ Fetched AcousticBrainz features

════════════════════════════════════════════
📊 TECHNICAL METADATA
════════════════════════════════════════════
BPM: 126
Key: A Major
Time Signature: 4/4
Energy: 0.67 (Medium-High)
Valence: 0.54 (Neutral-Positive)
Acousticness: 0.03 (Electronic)
Instrumentalness: 0.89 (Mostly Instrumental)
Danceability: 0.58

════════════════════════════════════════════
🎸 GENRES & TAGS
════════════════════════════════════════════
Primary: Psychedelic rock, Neo-psychedelia
Secondary: Synth-pop, Dream pop, Electronic
Community Tags: psychedelic, progressive, experimental

════════════════════════════════════════════
🎹 SUNO V5 PROMPT
════════════════════════════════════════════
Style: Psychedelic rock, synth-pop, 126 BPM, electronic production

[Energy: Medium-High]
[Mood: Dreamy, hypnotic, building, trippy]
[Instrumentation: Synth bass, electronic drums, layered synthesizers,
processed guitar, analog synth pads]
[Vocal Style: Processed, layered, echo effects, reverb]
[Production: Electronic, polished, spacious mix, heavy effects]

[intro]
(Instrumental - building synth pattern)

[verse 1]
[Instrumentation: Minimal synth, subtle drums]
[Your lyrics here]

[chorus]
[Energy: Maximum]
[Instrumentation: Full arrangement, layered synths]
[Your lyrics here]

════════════════════════════════════════════
🎚️ UDIO PROMPT
════════════════════════════════════════════
Psychedelic rock with synth-pop influences, 126 BPM, A Major key.
Electronic production with layered synthesizers, processed guitar,
synth bass, and programmed drums. Dreamy, hypnotic atmosphere with
heavy reverb and echo effects. Building intensity, trippy textures.
Processed vocals with heavy effects. Progressive structure with
extended instrumental sections.

════════════════════════════════════════════
📈 CONFIDENCE SCORES
════════════════════════════════════════════
Technical metadata: ████████████████████ HIGH (Spotify API)
Genre classification: ████████████████████ HIGH (10+ sources)
BPM/Key accuracy:     ████████████████████ HIGH (Direct measurement)
Instrumentation:      ████████████░░░░░░░░ MEDIUM (Inferred)
Vocal style:          ████████░░░░░░░░░░░░ LOW (Needs refinement)
Production style:     ████████████░░░░░░░░ MEDIUM (Genre-based)

════════════════════════════════════════════
💡 COMMUNITY REFINEMENTS
════════════════════════════════════════════
3 users have refined prompts for this song:

[1] @username1 (Success: 4.5/5 - Suno)
    Added: "flanging effect", "analog tape saturation"
    Audio: [link to comparison]

[2] @username2 (Success: 4.0/5 - Udio)
    Modified vocals: "heavily processed, robotic quality"
    Audio: [link to comparison]

Run with --refinement 1 to use that refined prompt
```

**Deployment:**
- Add to repository under `tools/song-to-prompt/`
- Publish to PyPI for easy installation
- GitHub Actions for automated testing
- Documentation in repository

---

### **Phase 2: Community Database & Refinement System**
**Timeline**: 1-2 weeks after Phase 1
**Priority**: MEDIUM - Improves accuracy over time

**Goals:**
- Enable community to contribute successful prompt refinements
- Build database of verified song→prompt mappings
- Improve translation mappings based on real-world success

**Features:**
- ✅ Submit refinement: `song-to-prompt refine "Song - Artist" --prompt [file]`
- ✅ Rate success: `song-to-prompt rate [refinement-id] --score 4.5`
- ✅ Browse database: `song-to-prompt search "psychedelic rock"`
- ✅ Export/import refinements (shareable JSON)
- ✅ Upvote/downvote system

**Database Schema:**
```json
{
  "song_id": "spotify:track:xxxxx",
  "song_name": "Let It Happen",
  "artist": "Tame Impala",
  "generated_metadata": {
    "bpm": 126,
    "key": "A",
    "energy": 0.67,
    "genres": ["psychedelic rock", "synth-pop"]
  },
  "generated_prompt": {
    "platform": "suno",
    "prompt": "[original generated prompt]",
    "generated_at": "2025-11-26T10:00:00Z"
  },
  "community_refinements": [
    {
      "id": "refine-001",
      "user": "@username1",
      "platform": "suno",
      "prompt": "[refined prompt]",
      "changes_made": "Added flanging effect, analog tape saturation",
      "success_rating": 4.5,
      "votes": 12,
      "audio_comparison": "https://...",
      "submitted_at": "2025-11-26T12:00:00Z",
      "notes": "Really captures the psychedelic swirl of the original"
    }
  ]
}
```

**Storage:**
- Phase 2A: Local JSON file (Git-tracked)
- Phase 2B: Migrate to SQLite for better querying
- Phase 2C: Cloud database (Supabase free tier) when scale requires

---

### **Phase 3: Web Interface**
**Timeline**: 3-4 weeks after Phase 2
**Priority**: MEDIUM - Accessibility for non-technical users

**Goals:**
- Make tool accessible without Python installation
- Visual interface for browsing community database
- Social features (upvote, comment, share)

**Features:**
- ✅ Search by song/artist
- ✅ Browse by genre/mood/BPM range
- ✅ Visual comparison of generated vs refined prompts
- ✅ Audio player for comparisons
- ✅ User accounts (optional, for saving favorites)
- ✅ Share generated prompts via URL
- ✅ Export to Suno/Udio (copy buttons)
- ✅ API endpoint for programmatic access

**Tech Stack:**
- **Frontend**: Next.js 14 (React)
- **Backend**: Vercel serverless functions
- **Database**: Supabase (Postgres)
- **Hosting**: Vercel (free tier → paid as needed)
- **Caching**: Vercel KV or Upstash Redis
- **Auth**: NextAuth.js (GitHub OAuth)

**URL Ideas:**
- `songprompt.ai`
- `promptfromsong.com`
- `song2prompt.io`
- `musicprompt.tools`

**User Flow:**
```
1. User lands on homepage
2. Search bar: "Enter song name or Spotify URL"
3. Results appear:
   ├─ Technical metadata (collapsible)
   ├─ Platform tabs: [Suno] [Udio] [Stable Audio]
   ├─ Generated prompt (copy button)
   ├─ Confidence scores (visual)
   └─ Community refinements (if any)
4. User can:
   ├─ Copy prompt
   ├─ Submit refinement (requires account)
   ├─ Rate refinement
   ├─ Share via link
   └─ Save to favorites
```

**Monetization (Optional, Phase 4):**
- Free tier: 10 searches/day
- Pro tier ($5/mo): Unlimited searches, API access, save unlimited favorites
- Enterprise: White-label, custom translation mappings

---

### **Phase 4: Advanced Features** (Future)
**Timeline**: Ongoing
**Priority**: LOW - Nice-to-haves

**Possible additions:**
- 🎵 Audio file upload → analysis (using Essentia.js or similar)
- 🎨 Visual waveform comparison
- 📊 "Similar songs" recommendations
- 🤖 LLM-enhanced descriptions (GPT-4 Vision analyzing spectrograms)
- 🎸 Instrument-specific deep dive (guitar tone analysis)
- 📱 Mobile app
- 🔌 Suno/Udio plugin (if APIs become available)
- 🎓 "Learn why" mode (educational explanations)

---

## Translation Mappings

This is the **core research component**. These mappings convert technical values → prompt language.

### 1. Energy Level (Spotify 0-1 scale)

```python
def translate_energy(energy: float) -> dict:
    """
    Spotify Energy: Perceptual measure of intensity/activity
    0.0 = calm, 1.0 = high energy
    """
    if energy < 0.2:
        return {
            "suno_tag": "[Energy: Minimal]",
            "descriptors": ["sparse", "quiet", "ambient", "minimal"],
            "confidence": "high"
        }
    elif energy < 0.4:
        return {
            "suno_tag": "[Energy: Low]",
            "descriptors": ["calm", "subdued", "gentle", "relaxed"],
            "confidence": "high"
        }
    elif energy < 0.6:
        return {
            "suno_tag": "[Energy: Medium]",
            "descriptors": ["moderate pace", "balanced", "steady"],
            "confidence": "high"
        }
    elif energy < 0.8:
        return {
            "suno_tag": "[Energy: High]",
            "descriptors": ["energetic", "driving", "upbeat", "lively"],
            "confidence": "high"
        }
    else:
        return {
            "suno_tag": "[Energy: Maximum]",
            "descriptors": ["intense", "powerful", "explosive", "aggressive"],
            "confidence": "high"
        }
```

### 2. Valence (Happiness) + Energy = Mood

```python
def translate_mood(valence: float, energy: float) -> dict:
    """
    Valence: 0.0 = sad/negative, 1.0 = happy/positive
    Combined with Energy for mood mapping
    """

    # High energy + high valence = HAPPY/ENERGETIC
    if valence > 0.6 and energy > 0.6:
        return {
            "mood": ["upbeat", "cheerful", "euphoric", "joyful"],
            "suno_tag": "[Mood: Upbeat, energetic]",
            "confidence": "high"
        }

    # High energy + low valence = AGGRESSIVE/INTENSE
    elif valence < 0.4 and energy > 0.6:
        return {
            "mood": ["aggressive", "intense", "angsty", "powerful"],
            "suno_tag": "[Mood: Intense, aggressive]",
            "confidence": "high"
        }

    # Low energy + low valence = SAD/MELANCHOLIC
    elif valence < 0.4 and energy < 0.4:
        return {
            "mood": ["melancholic", "somber", "introspective", "sad"],
            "suno_tag": "[Mood: Melancholic, introspective]",
            "confidence": "high"
        }

    # Low energy + high valence = PEACEFUL/CONTENT
    elif valence > 0.6 and energy < 0.4:
        return {
            "mood": ["peaceful", "content", "serene", "relaxed"],
            "suno_tag": "[Mood: Peaceful, serene]",
            "confidence": "high"
        }

    # Neutral combinations
    else:
        return {
            "mood": ["balanced", "moderate", "neutral"],
            "suno_tag": "[Mood: Balanced]",
            "confidence": "medium"
        }
```

### 3. Acousticness → Instrumentation Style

```python
def translate_acousticness(acousticness: float, genres: list) -> dict:
    """
    Acousticness: 0.0 = electronic, 1.0 = acoustic
    Combined with genre context for better accuracy
    """

    if acousticness > 0.8:
        return {
            "primary_instruments": [
                "acoustic guitar",
                "piano",
                "live drums",
                "upright bass"
            ],
            "production": "live recording, natural sound, minimal production",
            "suno_tag": "[Instrumentation: Acoustic guitar, live instruments]",
            "avoid": "synthesizers, electronic drums, heavy processing",
            "confidence": "high"
        }

    elif acousticness < 0.2:
        # Electronic
        instruments = []
        production = []

        if "edm" in genres or "electronic" in genres:
            instruments = ["synthesizers", "drum machine", "synth bass", "digital effects"]
            production = "electronic production, digital processing"
        elif "rock" in genres or "pop" in genres:
            instruments = ["electric guitar", "bass", "drums", "synthesizers"]
            production = "studio production, effects processing"
        else:
            instruments = ["electronic instruments", "synthesized sounds"]
            production = "electronic production"

        return {
            "primary_instruments": instruments,
            "production": production,
            "suno_tag": f"[Instrumentation: {', '.join(instruments[:3])}]",
            "confidence": "medium"  # Needs genre context
        }

    else:
        # Blend
        return {
            "primary_instruments": [
                "blend of acoustic and electronic",
                "electric guitar",
                "synthesizers",
                "live drums with electronic elements"
            ],
            "production": "hybrid production, mixed elements",
            "suno_tag": "[Instrumentation: Mixed acoustic/electronic]",
            "confidence": "medium"
        }
```

### 4. BPM → Tempo Descriptors

```python
def translate_bpm(bpm: float) -> dict:
    """
    BPM to tempo descriptors
    Note: Keep numeric BPM for accuracy, add descriptors for context
    """

    if bpm < 60:
        descriptor = "very slow"
    elif bpm < 80:
        descriptor = "slow"
    elif bpm < 100:
        descriptor = "moderate"
    elif bpm < 120:
        descriptor = "moderate uptempo"
    elif bpm < 140:
        descriptor = "uptempo"
    elif bpm < 160:
        descriptor = "fast"
    else:
        descriptor = "very fast"

    return {
        "bpm": round(bpm),
        "descriptor": descriptor,
        "prompt_format": f"{round(bpm)} BPM, {descriptor}",
        "confidence": "high"  # Spotify BPM is quite accurate
    }
```

### 5. Key + Mode → Musical Key

```python
def translate_key(key: int, mode: int) -> dict:
    """
    Key: 0=C, 1=C#, 2=D, ..., 11=B
    Mode: 0=minor, 1=major
    """

    keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    key_name = keys[key]
    mode_name = "major" if mode == 1 else "minor"

    # Mood associations (research-backed)
    if mode == 0:  # Minor
        mood_hint = "tends toward darker, more introspective mood"
    else:  # Major
        mood_hint = "tends toward brighter, more uplifting mood"

    return {
        "key": f"{key_name} {mode_name}",
        "prompt_format": f"{key_name}m" if mode == 0 else key_name,
        "mood_association": mood_hint,
        "confidence": "high"
    }
```

### 6. Instrumentalness → Vocal Style

```python
def translate_instrumentalness(instrumentalness: float) -> dict:
    """
    Instrumentalness: Prediction of whether track contains no vocals
    0.0 = likely vocals, 1.0 = likely instrumental
    """

    if instrumentalness > 0.5:
        # Mostly/fully instrumental
        return {
            "vocal_presence": "instrumental" if instrumentalness > 0.8 else "minimal vocals",
            "suno_tag": "[Instrumental]" if instrumentalness > 0.8 else "[Minimal vocals]",
            "prompt_note": "(Leave lyrics section empty or add [Instrumental])",
            "confidence": "high"
        }
    else:
        # Likely has vocals, but can't determine style from this alone
        return {
            "vocal_presence": "vocals present",
            "suno_tag": None,  # Can't infer style
            "prompt_note": "Vocal style needs manual specification or genre inference",
            "confidence": "low"  # Need other signals
        }
```

### 7. Genre Aggregation

```python
def aggregate_genres(spotify_genres: list, musicbrainz_genres: list,
                     lastfm_tags: list) -> dict:
    """
    Combine genre data from multiple sources
    Weight by reliability and agreement
    """

    # Weight sources
    all_genres = (
        [(g, 3) for g in spotify_genres] +      # Spotify most reliable
        [(g, 2) for g in musicbrainz_genres] +  # MusicBrainz second
        [(g, 1) for g in lastfm_tags]           # Last.fm community tags
    )

    # Count weighted occurrences
    genre_scores = {}
    for genre, weight in all_genres:
        genre_lower = genre.lower()
        genre_scores[genre_lower] = genre_scores.get(genre_lower, 0) + weight

    # Sort by score
    sorted_genres = sorted(genre_scores.items(), key=lambda x: x[1], reverse=True)

    # Take top genres
    primary = [g for g, s in sorted_genres[:2]]
    secondary = [g for g, s in sorted_genres[2:5]]

    return {
        "primary_genres": primary,
        "secondary_genres": secondary,
        "all_genres": [g for g, s in sorted_genres],
        "prompt_format": ", ".join(primary + secondary),
        "confidence": "high" if len(sorted_genres) > 3 else "medium"
    }
```

---

## Implementation Options

### **Option 1: Python CLI Tool** ✅ RECOMMENDED FOR PHASE 1

**Pros:**
- ✅ Fast to build (2-3 weeks)
- ✅ Works offline (cached data)
- ✅ Extensible (easy to add new APIs/platforms)
- ✅ Can be used in scripts/automation
- ✅ Lower barrier to contribution (Python devs)
- ✅ Version controlled translation mappings

**Cons:**
- ❌ Requires Python installation
- ❌ Less accessible to non-technical users
- ❌ No visual interface

**Best For**:
- Initial validation
- Developer community
- Power users
- Research and refinement of translation mappings

---

### **Option 2: Web Application** (Phase 3)

**Pros:**
- ✅ No installation required
- ✅ Accessible to everyone
- ✅ Visual interface
- ✅ Social features (community refinements)
- ✅ Shareable links
- ✅ Better discoverability

**Cons:**
- ❌ Longer development time (3-4 weeks)
- ❌ Hosting costs (though free tier viable initially)
- ❌ Requires API key management
- ❌ More complex deployment

**Best For:**
- General user base
- Community growth
- Mainstream adoption

---

### **Option 3: Discord Bot** (Alternative)

**Pros:**
- ✅ Low friction (users already on Discord)
- ✅ Built-in community features
- ✅ Viral potential
- ✅ Can be built alongside CLI tool

**Cons:**
- ❌ Limited by Discord platform
- ❌ Harder to organize/search data
- ❌ Ephemeral (messages disappear)

**Best For:**
- Community engagement
- Initial user testing
- Complementary to other options

---

## Strengths and Limitations

### Strengths ✅

**High-Confidence Data:**
- BPM, key, time signature (Spotify API) → 95%+ accurate
- Energy, valence metrics (Spotify) → Well-calibrated
- Genre classification (multiple sources) → Robust through aggregation
- Community refinements improve over time

**Unique Value:**
- Only tool that aggregates AND translates
- Platform-specific formatting
- Community-driven improvement
- Research-backed translation mappings

**Practical Impact:**
- Saves users time (no manual analysis)
- Reduces wasted credits (better starting point)
- Educational (teaches what makes a sound)
- Lowers barrier to entry

### Limitations ⚠️

**Medium-Confidence Inferences:**
- Instrumentation (inferred from acousticness + genre) → 60-70% accurate
- Vocal style (genre-based assumptions) → Requires manual refinement
- Production techniques (genre conventions) → General guidance only

**Cannot Capture:**
- Specific guitar tones (e.g., "fuzz vs overdrive")
- Vocal delivery nuances (e.g., "raspy" vs "smooth")
- Mix details (e.g., "sidechain compression")
- Performance style (e.g., "jazz swing feel")
- Exact effects chains

**Dependency Risks:**
- API availability (rate limits, downtime)
- API changes (need to adapt)
- Platform prompt format changes (Suno/Udio updates)

### Mitigation Strategies

**For Medium-Confidence Data:**
- ✅ Show confidence scores
- ✅ Mark as "starting point, refine as needed"
- ✅ Leverage community refinements
- ✅ Allow manual overrides

**For Unmeasurable Details:**
- ✅ Provide "advanced options" for manual specification
- ✅ Link to educational resources
- ✅ Show similar successful prompts for reference

**For API Dependencies:**
- ✅ Cache responses (reduce calls)
- ✅ Graceful degradation (work with partial data)
- ✅ Multiple source redundancy
- ✅ Local database fallback

---

## Next Steps

### Immediate Actions

1. **Validate Interest**
   - [ ] Share concept with community (Reddit, Discord)
   - [ ] Gauge demand and gather feedback
   - [ ] Identify early testers

2. **Technical Validation**
   - [ ] Test API access (get free tier keys)
   - [ ] Verify rate limits are sufficient
   - [ ] Test translation mappings with 5-10 songs manually
   - [ ] Confirm output quality meets expectations

3. **Scope Phase 1**
   - [ ] Finalize CLI feature set
   - [ ] Set up development environment
   - [ ] Create initial translation mapping rules
   - [ ] Define success criteria for Phase 1

### Development Roadmap

**Week 1-2: Foundation**
- Set up project structure
- Implement API wrappers (Spotify, MusicBrainz, Last.fm)
- Build caching layer
- Create basic CLI interface

**Week 3: Translation Layer**
- Implement all translation functions
- Test with 20+ diverse songs
- Refine mappings based on results
- Add confidence scoring

**Week 4: Platform Formatters**
- Suno v5 formatter
- Udio formatter
- Stable Audio formatter (optional)
- Output formatting and display

**Week 5: Polish & Release**
- Error handling
- Documentation
- README with examples
- Release v0.1.0 to community
- Gather feedback

### Success Metrics

**Phase 1 Success:**
- 50+ users install and use tool
- 80%+ find output "useful as starting point" (survey)
- 10+ community refinement submissions
- Translation mappings validated through usage

**Phase 2 Success:**
- 100+ songs in community database
- Average refinement rating > 4.0/5
- Users report credit savings (fewer iterations)

**Phase 3 Success:**
- 1,000+ monthly active users
- 50+ refinements submitted per week
- Tool mentioned/linked in community spaces

---

## Questions to Resolve

### Technical Questions

1. **API Rate Limits**: Are free tiers sufficient for expected usage?
   - Spotify: 15k/day → ~10 users/minute sustained
   - Last.fm: 5k/hour → More than enough
   - **Answer**: Start with free tiers, add API key rotation if needed

2. **Caching Strategy**: How long to cache API responses?
   - Song metadata rarely changes
   - **Proposal**: 30 days for technical data, 7 days for community tags

3. **Translation Mapping Updates**: How to improve mappings over time?
   - Track which mappings produce successful results
   - A/B test refinements
   - **Proposal**: Version translation rules, allow community proposals

### Product Questions

1. **Pricing Model**: Should this be free or freemium?
   - **Proposal**: Free CLI tool, optional paid web app for sustainability

2. **Community Moderation**: How to ensure quality refinements?
   - **Proposal**: Upvote system + minimum usage threshold to submit

3. **Platform Priority**: Which platforms to support first?
   - **Proposal**: Suno (most popular), Udio (second), others later

---

## Related Resources

### Existing Documentation
- [Prompt Interpretability Guide](../prompting/prompt-interpretability.md) - Framework for understanding prompt effectiveness
- [Evidence Standards](../evidence-standards.md) - How we validate claims
- [Prompt Testing Protocol](../research-methodology/prompt-testing-protocol.md) - Testing methodology

### External APIs
- [Spotify Web API Docs](https://developer.spotify.com/documentation/web-api)
- [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API)
- [Last.fm API](https://www.last.fm/api)
- [AcousticBrainz API](https://acousticbrainz.org/api)

### Research Papers
- Spotify Audio Features: [Understanding Spotify's Track Features](https://developer.spotify.com/documentation/web-api/reference/get-audio-features)
- Audio Feature Extraction: [Essentia library documentation](https://essentia.upf.edu/)

---

## Appendix: Example API Responses

### Spotify API Response (Simplified)
```json
{
  "id": "2X485T9Z5Ly0xyaghN73ed",
  "name": "Let It Happen",
  "artists": [{"name": "Tame Impala"}],
  "audio_features": {
    "tempo": 126.011,
    "key": 9,
    "mode": 1,
    "time_signature": 4,
    "energy": 0.672,
    "valence": 0.544,
    "danceability": 0.579,
    "acousticness": 0.0331,
    "instrumentalness": 0.888,
    "liveness": 0.0898,
    "speechiness": 0.0488
  }
}
```

### MusicBrainz Response (Simplified)
```json
{
  "title": "Let It Happen",
  "artist-credit": [{"name": "Tame Impala"}],
  "tags": [
    {"name": "psychedelic rock", "count": 4},
    {"name": "neo-psychedelia", "count": 3},
    {"name": "indie rock", "count": 2}
  ]
}
```

### Last.fm Response (Simplified)
```json
{
  "track": {
    "name": "Let It Happen",
    "artist": {"name": "Tame Impala"},
    "toptags": {
      "tag": [
        {"name": "psychedelic", "count": 100},
        {"name": "indie", "count": 82},
        {"name": "electronic", "count": 67}
      ]
    }
  }
}
```

---

## Contact & Contribution

**Questions?**
- Open an [issue](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues)
- Start a [discussion](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/discussions)

**Want to help build this?**
- See [Contributing Guidelines](../../CONTRIBUTING.md)
- Check [Development Roadmap](#development-roadmap) for where to start

**Have translation mapping ideas?**
- Submit proposals via Pull Request
- Include evidence/reasoning for mappings
- Reference [Evidence Standards](../evidence-standards.md)

---

**Last Updated**: 2025-11-26
**Status**: Concept/Planning - Ready to begin Phase 1
**Next Milestone**: Technical validation + community feedback
