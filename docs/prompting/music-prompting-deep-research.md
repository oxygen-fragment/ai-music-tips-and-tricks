# Music Prompting Deep Research

## Goal

Our goal is to generate a prompt, that analyses what's known to work with AI music generation platforms that allow for nuanced control of the output. For example, having a specific piano melody play for exactly `X` seconds (e.g. 10 seconds), followed by a heavy guitar riff with double bass (this is just an example to illustrate our point, obviously we want this to extend to any genre, instruments, etc.). For testing, we're using Suno in the 'Custom' tab (where it seems to more "faithfully" adhere to instructions). We've tried the following:

- `Quiet verse, explosive chorus (30 seconds maximum)`
  - This resulted in an explosive part first, followed by the quieter part
  - adhered to the `30 seconds maximum` instruction
- `Begin quiet, end on an explosive note (30 seconds maximum)`
  - same result as above
- `Begin quiet piano, end with explosive guitars and double bass (30 seconds maximum)`
  - started with quiet piano (~5 seconds), launched into guitar and double bass
- `Begin quiet piano (first 10 seconds), end with explosive heavy guitars and double bass (15 seconds) (30 seconds maximum)`
  - interestingly, Suno changed our prompt (with our prompt seemingly taking a back seat) to: `rock, metal, piano ballad` (we had to click `Show More` to see our actual prompt)
  - quiet piano played for around 1 second, then launched straight into the guitar
  - songs were less than 30 seconds as instructed
- `First 10 seconds begin quiet piano, final 20 seconds end with explosive heavy guitars and double bass (30 seconds maximum)`
  - again, Suno changed our prompt (with our prompt seemingly taking a back seat) to: `rock, metal, piano ballad` (we had to click `Show More` to see our actual prompt)
  - quiet piano lasted all of about 1 second before launching into guitar and double bass
- `<first 10 seconds> begin quiet piano, <final 20 seconds> end with explosive heavy guitars and double bass (30 seconds maximum)`
  - Suno changed our prompt (with our prompt taking a back seat) to: `piano ballad, metal`
  - quiet piano lasted less than 5 seconds, then launch into the guitar and double bass
- `<10 seconds> begin quiet piano, <20 seconds> end with explosive heavy guitars and double bass (30 seconds maximum)`
  - Suno changed our prompt (with our prompt taking a back seat) to: `rock, metal`
  - quiet piano section lasted from between 1 and 3 seconds before launching into the guitar and double bass
- `<10 seconds> quiet piano, <20 seconds> explosive heavy guitars and double bass (30 seconds maximum)`
  - Suno left our prompt as-is
  - quiet piano section didn't even make it to 2–3 seconds before launching into the guitar and double bass
- `<0:00–0:10> quiet piano, <0:10–0:20> explosive heavy guitars and double bass <0:20–0:30> outro (30 seconds maximum)`
  - Suno changed our prompt (with our prompt taking a back seat) to: `rock, metal, instrumental`
  - quiet piano section lasted 1–2 seconds before launching to the heavy guitars and double bass
- `<0:00–0:10> quiet piano, <0:10–0:20> explosive heavy guitars and double bass <0:20–0:30> outro`
  - Suno left our prompt as-is
  - these were the lengths of the songs generated (in order of generation):
    - 27 seconds
      - piano for 5 seconds, gentle guiter for 2 seconds, launch into heavy guitar with double bass
    - 2 minutes 8 seconds
      - piano for 5 seconds, launched into heavy guitar with double bass
    - 2 minutes 9 seconds
      - piano for 5 seconds, launched into heavy guitar with double bass
    - 1 minute 21 seconds
      - piano for 5 seconds, launched into heavy guitar with double bass
    - 51 seconds
      - piano for 5 seconds, gentle guiter for 2–3 seconds, back to piano only for ~20 seconds, launches into heavy guitar with double bass
    - 2 minutes 29 seconds
      - piano for 5 seconds, gentle guiter for 5 seconds, launches into heavy guitar with double bass
  - `<0:00–0:10> quiet piano, <0:10–0:20> explosive heavy guitars and double bass, <0:20–0:30> outro (30 seconds maximum)`
    - Changed `Weirdness` from 50% to 40%
    - Changed `Style Influence` from 50% to 85%
    - Suno changed our prompt (with our prompt taking a back seat) to: `rock, metal`
    - piano for 1–4 seconds (multiple generations), launched into heavy guitar with double bass
- - `<0:00–0:10> quiet piano, <0:10–0:20> explosive heavy guitars and double bass, <0:20–0:30> outro (30 seconds maximum)`
    - Changed `Weirdness` from 50% to 40%
    - Changed `Style Influence` from 50% to 100%
    - Suno changed our prompt (with our prompt taking a back seat) to: `rock, metal, instrumental`, and `rock, metal, piano ballad` on other generations with the same base prompt
    - piano for 1–8 seconds (multiple generations), launched into heavy guitar with double bass

Help us create a prompt for Deep Research that collects all known prompting techniques that have been shown to work so we can create music and guide these platforms in any way we choose. Leave no stone unturned and be brave enough to dig into the details of prompt structure. We also want to use this information to help inform a guide we're creating (see [ai-music-tips-and-tricks](https://github.com/oxygen-fragment/ai-music-tips-and-tricks)).

---

## Prompt Rewriter Output (final prompt)

```
You are an AI research agent. Your task is to investigate, with evidence, how to reliably control structure, timing, dynamics, and instrumentation in modern AI music generation systems (with a special focus on Suno’s “Custom” mode, but including at least 2–3 other popular text-to-music platforms).

The core question:
What actually works today to steer AI music models in terms of **sections over time** (intro/verse/chorus/bridge/outro), **approximate timing** (early vs middle vs end, or rough seconds/bars), and **instrumental texture changes** (e.g., piano-only intro → heavy guitars with double kick), and what consistently fails or is unreliable?

Treat this as an evidence-seeking investigation, not a hype piece. Allow conclusions like “no reliable method” or “unknown”.

========================
SCOPE & ANGLES TO COVER
========================

1. Model capabilities and limits
- Summarize what current text-to-music systems can generally do regarding:
  - Structural control (multi-part songs, distinct sections).
  - Timing control: exact seconds vs rough segments (first third, last 10 seconds, etc.).
  - Instrument and dynamics control over time (e.g., quiet piano intro, loud guitar chorus).
- Explain, at a high level, why these models may struggle with precise timing (e.g., diffusion / latent audio behavior, training data).

2. Prompt syntax and structure
- Compare the effect of:
  - Short, tag-like prompts (e.g., "rock, metal, piano ballad") vs long narrative prompts.
  - Explicit structural markup:
    - Timestamps (`0:00–0:10`, `0–10s`, `<0:00–0:10>`).
    - Section labels (`[Intro]`, `Verse 1:`, `Chorus:`, `Bridge:`, `Outro:`).
    - Bulleted or numbered lists of sections.
  - Imperative vs descriptive phrasing:
    - Imperative: "Start with 10 seconds of quiet piano, then explode into heavy guitars and double kick for the rest of the track."
    - Descriptive: "A song that begins with a quiet piano section and ends on an explosive heavy metal riff."
  - Order sensitivity: does placing instructions earlier in the prompt matter in practice?

For each pattern, report:
- Evidence that it affects structure or timing (or not).
- Any platform-specific quirks.

3. Temporal control strategies
- Investigate methods for approximating control over WHEN things happen, such as:
  - Timestamps (`0:00–0:10`, `0:10–0:20`, etc.).
  - Time expressions (`first 10 seconds`, `final 20 seconds`, `last 4 bars`).
  - Bar- or measure-based instructions with assumed BPM (`first 4 bars`, etc.).
  - Relative sections (“first third of the track is quiet piano, last third is full band metal”).
- Determine whether any of these consistently help, across platforms or for specific ones.

Use the test scenario:
- A ~30 second track structured as:
  - [0:00–0:10] quiet piano
  - [0:10–0:20] explosive heavy guitars and double bass
  - [0:20–0:30] outro
- Look for ANY known prompting patterns or workflows that get *closer* to this kind of control, even if imperfect.

4. Instrument and texture changes over time
- Identify techniques for:
  - Enforcing or strongly encouraging “instrument handoff” (e.g., piano-only intro → guitars enter later).
  - Suppressing instruments in parts of the track (“no drums in the first 10 seconds”).
  - Controlling dynamics (quiet vs loud, “gradual build”, “sudden drop”).

Distinguish:
- What tends to consistently work (e.g., “intro with only piano, no drums, gentle and sparse”).
- What is inconsistent or usually ignored.

5. Platform-specific behavior (spotlight on Suno Custom)
- For Suno Custom, investigate:
  - How it uses/overrides user prompts with style tags like “rock, metal, piano ballad”.
  - Whether shorter, tag-like genre prompts plus a separate structural block outperform long mixed prompts.
  - The documented or observed meaning of:
    - “Weirdness”
    - “Style Influence”
  - How these sliders affect:
    - Obedience to structure and timing instructions.
    - Obedience to instrument and dynamics constraints.

- For at least 2–3 other platforms (e.g., Udio, Stable Audio, or others that are current at the time of research):
  - Describe their prompt syntax and any special tokens for sections, bars, or arrangement.
  - Note where they are stronger or weaker than Suno in sectional or temporal control.

6. Workflows beyond one-shot prompts
- Examine multi-step workflows to get better control than a single prompt can provide:
  - Generate a base track, then:
    - Extend or vary sections with new prompts.
    - Inpaint or regenerate segments with more precise instructions.
  - Use uploaded audio or stems (if supported) to:
    - Lock in an intro or outro.
    - Force certain instruments or motifs.

- Consider “arrangement by editing”:
  - Generate longer clips and cut/splice them to assemble the desired structure.
  - Use multiple generations for different sections (e.g., one prompt for intro piano, another for heavy chorus) and stitch them.

7. Failure modes and anti-patterns
- Document common patterns where models ignore or partially follow instructions, such as:
  - Intro instruments or quiet sections that collapse to ~1–5 seconds instead of the requested 10+ seconds.
  - Style tags or genre labels overriding specific structural or instrument instructions.
  - Very long, highly detailed prompts decreasing controllability.

For each failure mode, identify:
- Likely cause (hypothesized).
- Any mitigation strategies that have evidence behind them.

8. Evaluation and experiment design
- Propose a small, reusable experiment suite to validate prompting techniques over time, especially on Suno. For example:
  - A matrix of prompts varying:
    - Time syntax (timestamps vs “first 10 seconds” vs “intro/verse/chorus”).
    - Prompt length (short vs long).
    - Genre tags vs none.
    - Weirdness / Style Influence values.
  - Metrics:
    - Approximate duration of each section.
    - Presence or absence of target instruments in each segment.
    - Perceived dynamic shape (quiet to loud, etc.).

- Explain how someone can run these tests themselves and score results (e.g., listening plus checking waveforms).

========================
EVIDENCE & EPISTEMIC RULES
========================

- Back up non-obvious claims with citations when possible:
  - Official docs, dev blogs, FAQs.
  - Research papers or technical posts.
  - Community experiments where prompts and outputs are shown (GitHub, forums, Reddit/Discord summaries, videos with clear examples).
- Distinguish clearly between:
  - Well-supported patterns.
  - Community lore / anecdotal advice.
  - Speculation or educated guesses.

- If evidence is mixed or missing, say so explicitly:
  - Use labels like “Unknown / not well established” or “Limited anecdotal evidence”.
  - When uncertain, propose concrete prompts and experiment designs that a user could run to test the hypothesis.

========================
OUTPUT STRUCTURE
========================

Structure your final answer in three main parts:

1. Landscape & Theory
   - Overview of model capabilities and limits for structure, timing, and instrument control.
   - Comparison of at least 2–3 platforms (Suno Custom plus others).
   - Explanation, in accessible terms, of why precise second-level timing might be hard or impossible with current models.

2. Practical Playbook & Prompt Library
   - General principles for prompting AI music systems when you care about structure and timing.
   - Suno Custom section:
     - Recommended prompt formats and patterns.
     - Guidance on using genre tags vs detailed text.
     - Guidance on Weirdness and Style Influence in relation to instruction obedience.
   - Other-platforms section:
     - Key differences and platform-specific tricks where known.
   - A library of example prompts for:
     - Quiet intro → explosive chorus (e.g., piano to heavy guitars with double kick).
     - Intro/verse/chorus structures.
     - Gradual builds and breakdowns.
   - For each pattern:
     - Example prompt text.
     - Expected behavior.
     - Known caveats or failure rates.

3. Experiment Kit
   - A concise test matrix someone can run themselves to validate your recommendations (especially in Suno).
   - Instructions on how to iterate and adapt as platforms update.
   - Notes on how these findings could be integrated into a public guide (such as a GitHub “AI music tips and tricks” repository).

Write the final answer so that a technically literate musician or creator can both:
- Understand the constraints of current tools, and
- Immediately apply the prompt patterns and workflows in Suno and other platforms.
```

## Results
