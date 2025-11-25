# Evidence Standards

> **Why This Matters**: This repository aims to provide reliable, actionable guidance for AI music generation. To maintain credibility and help users make informed decisions, we clearly label the evidence quality behind every claim.

---

## How We Label Claims

Throughout this repository, you'll see evidence labels indicating the quality and source of information:

### ✅ VERIFIED
**What it means:**
- Tested in our controlled experiments (see `/research` directory)
- Documented in official platform documentation with links
- Consistently reproducible across multiple tests
- We can show you the data

**Example:**
> ✅ VERIFIED: Bar count specifications in Suno prompts do not reliably control element duration.
>
> Source: [Suno Bar Timing Research](../research/suno_bar_timing_research_report.md) — 12 controlled tests, 575% error rate observed

---

### 📚 SOURCED
**What it means:**
- Found in quality external sources
- Research papers, technical documentation, developer blogs
- Always cited with accessible links
- We trust the source but haven't independently verified

**Example:**
> 📚 SOURCED: Stable Audio can generate exact durations up to 3 minutes.
>
> Source: Official research paper (arXiv 2402.04825v3) + Stability AI documentation

---

### 👥 ANECDOTAL
**What it means:**
- Community reports (Reddit, Discord, forums, user submissions)
- Multiple people report similar experiences
- Not systematically tested in controlled conditions
- Useful patterns but treat as starting point for research, not proven fact

**Example:**
> 👥 ANECDOTAL: "Soft heavy metal" produces gentler metal tones while maintaining genre characteristics.
>
> Source: User report — works consistently for them, needs broader testing

---

### 💭 HYPOTHESIS
**What it means:**
- Based on understanding of model architecture
- Logical inference from verified facts
- Educated guess with reasoning explained
- **Needs testing to confirm**
- We're transparent about not knowing for certain

**Example:**
> 💭 HYPOTHESIS: Technical terms like "120 BPM" are more interpretable than descriptive terms like "fast" because they likely appear as structured metadata in training data.
>
> Reasoning: Models are typically trained on music databases with BPM fields. Needs A/B testing to confirm effectiveness difference.

---

### ❓ UNKNOWN
**What it means:**
- We genuinely don't know
- Needs research and testing
- We're asking for help to investigate
- Better to admit ignorance than guess

**Example:**
> ❓ UNKNOWN: Why does "Like a summer breeze" produce sensible audio results despite seeming abstract?
>
> Possible explanations: (1) Component words have audio associations, (2) Poetic descriptions in training data, (3) Metaphorical learning. Needs systematic testing.

---

## Reliability Scores Explained

When we provide reliability percentages (e.g., "Structure tags: 95% reliable"), we document:

### Required Information
- **Source**: Where the number comes from
- **N**: How many tests/examples/reports
- **Date**: When last verified (models and platforms update!)
- **Method**: How reliability was measured
- **Platform/Version**: Which platform and version tested

### Example (Good)
```markdown
**Structure Tags**: 95% reliable ✅ VERIFIED

- Source: Suno documentation + 50 community examples + our testing
- N: 73 total generations
- Date: 2025-11-15
- Method: Tag produced expected section type (verse/chorus/bridge recognition)
- Platform: Suno v5
```

### Example (Needs Improvement)
```markdown
**Structure Tags**: 95% reliable

[Missing: Where does 95% come from? How many tests? When?]
```

---

## When Claims Have No Label

**If you see a claim without an evidence label, please report it!**

This can happen when:
- Document is being actively developed
- We forgot to add labels (human error)
- Content was added by contributor without following guidelines

[Submit an issue](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new?title=Missing%20Evidence%20Label) pointing to the specific claim.

---

## Updating Claims as Evidence Changes

### When Evidence Gets Stronger
- Platform releases documentation → Upgrade HYPOTHESIS to SOURCED
- We complete systematic testing → Upgrade HYPOTHESIS/ANECDOTAL to VERIFIED
- Multiple community reports confirm → Note increased confidence in ANECDOTAL

### When Evidence Gets Weaker
- Platform updates change behavior → Reverify or mark as OUTDATED
- New testing contradicts old findings → Update or mark for re-testing
- Source becomes unavailable → Document loss of source, downgrade if needed

### Version Dates Matter
Always include "Last verified: YYYY-MM-DD" for time-sensitive claims, especially:
- Platform-specific features
- Model version behavior
- Reliability percentages
- "Works/doesn't work" claims

---

## Testing Standards

### Minimum Standards for VERIFIED Status

**For Effectiveness Claims** (e.g., "X produces more consistent results than Y"):
- Minimum 5 trials per condition
- Document all settings (platform, version, sliders, etc.)
- Measure specific outcome (BPM variance, presence/absence, etc.)
- Report both successes and failures
- Include raw data or link to test report in `/research`

**For Reliability Claims** (e.g., "Works 70% of the time"):
- Minimum 10 trials
- Clear pass/fail criteria defined upfront
- Calculate actual percentage from results
- Document edge cases and failures

**For Architectural Claims** (e.g., "Model cannot do X"):
- Reference technical documentation or research papers
- Explain the architectural constraint
- Show multiple attempts at doing X, all failing for same reason

### Quick Test Template

For simple tests, use this format:

```markdown
## Test: [Descriptive Name]
**Date**: 2025-11-25
**Tester**: [Your GitHub username or name]
**Hypothesis**: [What you're testing]

**Method**:
- Platform: Suno v5
- Settings: Style Influence 70%, Weirdness 50%, etc.
- Prompt A: "[exact prompt including quotes]"
- Prompt B: "[exact prompt including quotes]"
- Trials: 5 each

**Results**:
| Trial | Prompt A Result | Prompt B Result |
|-------|----------------|----------------|
| 1     | [measurement]  | [measurement]  |
| 2     | [measurement]  | [measurement]  |
| ...   | ...            | ...            |

**Conclusion**: ✅ VERIFIED / ❌ REFUTED / ⚠️ INCONCLUSIVE
**Confidence**: High / Medium / Low
**Notes**: [Anything unexpected, edge cases, observations]
```

See [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md) for detailed guidelines.

---

## Community Contributions

### When Submitting Findings

**Include**:
1. Evidence label (be honest about what you know)
2. Platform and version
3. What you tested and how many times
4. Link to audio examples if possible
5. Settings used
6. Your reasoning

**Example Good Submission**:
> I tested "Soft heavy metal" vs "Heavy metal" 5 times each on Suno v5.
>
> Settings: Style Influence 70%, Weirdness 50%
>
> Result: "Soft heavy metal" produced cleaner guitar tones, less distortion, but maintained metal rhythm and structure in 4/5 trials.
>
> Audio examples: [links]
>
> Suggested label: 👥 ANECDOTAL (my testing only, needs broader verification)

**Example Poor Submission**:
> "Soft heavy metal" doesn't work, it's a contradictory prompt.
>
> [Missing: Did you test it? How many times? What happened? What makes it not work?]

### We Welcome
- ✅ Well-documented test results (become VERIFIED)
- ✅ Community reports with context (labeled ANECDOTAL)
- ✅ Hypotheses with clear reasoning (labeled HYPOTHESIS)
- ✅ Questions and "I don't know" (labeled UNKNOWN)

### We Ask You to Avoid
- ❌ Stating opinions as facts without evidence
- ❌ Using definitive language ("always", "never") without data
- ❌ Copying claims from forums without verification
- ❌ Assuming what "should" work without testing

---

## Special Case: "Works But Don't Know Why"

Sometimes you'll get consistent results from prompts that *theoretically* shouldn't work well:
- Abstract phrases: "Like a summer breeze"
- Poetic metaphors: "Sounds of thunder"
- Seeming contradictions: "Soft heavy metal"

**How we handle these:**

1. **Document the observation** with ANECDOTAL label
2. **List possible explanations** as HYPOTHESIS
3. **Call for research** with UNKNOWN label on the "why"

**Example**:

> 👥 ANECDOTAL: "Like a summer breeze" produces light, airy, gentle musical qualities
> - Tested: 3 times on Suno v5, consistent results
> - Audio: [link]
>
> 💭 HYPOTHESIS - Possible explanations:
> 1. Component words have audio associations ("breeze" → airy sounds, "summer" → bright)
> 2. Training data includes poetic music descriptions
> 3. Models learn metaphorical associations from paired text-audio
>
> ❓ UNKNOWN: Which explanation is correct? Does it work consistently? What's the mechanism?
> - Needs: Systematic testing of metaphorical prompts, comparison to literal equivalents

---

## For Maintainers

### Reviewing Pull Requests
- [ ] All claims have evidence labels
- [ ] Sources are cited for VERIFIED and SOURCED claims
- [ ] Reliability percentages include source/N/date/method
- [ ] No definitive language without VERIFIED backing
- [ ] HYPOTHESIS and ANECDOTAL clearly labeled as such

### Quarterly Audits
Every 3 months, check:
- Are VERIFIED claims still verified? (platforms update)
- Are sources still accessible?
- Has ANECDOTAL evidence grown stronger (more reports)?
- Are there unlabeled claims that slipped through?

### When Uncertain
**Default to more conservative labels:**
- Not sure if verified? → ANECDOTAL
- Anecdotal but makes logical sense? → HYPOTHESIS
- Don't know the mechanism? → UNKNOWN

Better to under-claim and be trusted than over-claim and lose credibility.

---

## Why This Matters

**For Users:**
- You know what's proven vs. what's experimental
- You can make informed decisions about what to trust
- You know where to focus your own testing efforts
- You understand limitations before wasting credits

**For Contributors:**
- Clear standards for submissions
- Recognition for quality research
- Build credibility in the community
- Push the field forward with evidence

**For the Repository:**
- Maintain scientific rigor
- Build trust with users
- Focus research efforts on UNKNOWN areas
- Improve over time as evidence accumulates

---

## Examples Throughout the Repository

### Good Examples

**From Suno Bar Timing Research**:
> ✅ VERIFIED: Bar count specifications like "(piano for 8 bars)" do NOT reliably control element duration in Suno.
>
> Evidence: Controlled research (n=12), mean 575% error for 2-bar requests, 166% error for 8-bar requests.
> Full report: [suno_bar_timing_research_report.md](../research/suno_bar_timing_research_report.md)

**From Architectural Limitations**:
> ✅ VERIFIED: Models cannot achieve second-level timing precision through text prompts alone.
>
> Evidence: Technical architectural constraint. Models compress audio 400-4000x (Stable Audio: 21.5 Hz = ~46ms per step). Text embeddings capture semantics not temporal relationships.
> Source: [Controlling AI Music Generation Timing](../research/controlling_ai_music_generation_timing.md)

### Needs Improvement

**Before**:
> "Building intensity" is low interpretability and produces inconsistent results.

**After**:
> 💭 HYPOTHESIS: "Building intensity" has lower interpretability than technical terms like "Crescendo" due to lack of structured metadata in training data.
>
> ❓ UNKNOWN: Actual consistency difference not measured. Needs A/B testing: "building intensity" vs "crescendo" (n=10+, measure section dynamic range variance).

---

## Questions?

- Not sure which label to use? → Start with most conservative (HYPOTHESIS/UNKNOWN)
- Have test results to share? → See [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md)
- Found unlabeled claims? → [Submit an issue](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/issues/new)
- Want to discuss methodology? → [Start a discussion](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/discussions)

---

## See Also

- [Prompt Testing Protocol](research-methodology/prompt-testing-protocol.md) - How to conduct systematic tests
- [Research Directory](../research/) - Published research and test reports
- [Contributing Guidelines](../CONTRIBUTING.md) - How to contribute evidence-based findings
- [Needs Testing Tracker](needs-testing.md) - Claims that need verification
