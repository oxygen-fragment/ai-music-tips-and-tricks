# Prompt Testing Protocol

> **Purpose**: Systematic methodology for testing prompt effectiveness and reliability in AI music generation platforms.
>
> **Goal**: Convert anecdotal observations into verified findings through reproducible testing.

---

## Table of Contents

- [Why Test Systematically?](#why-test-systematically)
- [Testing Standards](#testing-standards)
- [Quick Test Template](#quick-test-template)
- [Test Types](#test-types)
  - [Effectiveness Tests](#effectiveness-tests-ab-comparison)
  - [Reliability Tests](#reliability-tests-consistency)
  - [Feature Verification Tests](#feature-verification-tests-does-it-work)
- [Reporting Results](#reporting-results)
- [Common Pitfalls](#common-pitfalls)
- [Example Tests](#example-tests)

---

## Why Test Systematically?

**The Problem:**
- "X works better than Y" — How much better? How do you know?
- "This prompt fails 70% of the time" — Based on what sample size?
- "Technical terms are more consistent" — Did you measure variance?

**The Solution:**
Systematic testing with:
- Clear hypotheses
- Controlled variables
- Sufficient sample sizes
- Measurable outcomes
- Reproducible methods

**The Benefit:**
- Build trust through evidence
- Help users make informed decisions
- Identify what actually works
- Advance the field collectively

---

## Testing Standards

### Minimum Requirements for VERIFIED Status

| Test Type | Minimum N | Required Documentation |
|-----------|-----------|----------------------|
| **Effectiveness comparison** | 5 per condition | Settings, prompts, measurement method, raw data |
| **Reliability percentage** | 10 trials | Pass/fail criteria, all results (not just successes) |
| **Feature verification** | 5 trials | Expected vs actual behavior, failure modes |

### What to Control

**Always document:**
1. **Platform & Version**: Suno v5, Udio v1.2, etc.
2. **All Settings**: Style Influence %, Weirdness %, toggles, etc.
3. **Exact Prompts**: Including quotes, maintain spacing
4. **Date Tested**: Models and platforms update frequently
5. **Measurement Method**: How you evaluated results

**Keep constant between trials:**
- Platform version (don't test across updates)
- Settings (unless testing setting effects)
- Genre/style (unless testing genre effects)
- Everything except the variable you're testing

---

## Quick Test Template

Copy this template for any test:

```markdown
## Test: [Descriptive Name]

**Date**: YYYY-MM-DD
**Tester**: [Your GitHub username or name]
**Platform**: [Suno v5 / Udio v1.2 / etc.]
**Hypothesis**: [What you're testing - be specific]

### Method

**Settings:**
- Style Influence: [%]
- Weirdness: [%]
- [Any other relevant settings]

**Prompt A (Control):**
```
[Exact prompt with all formatting]
```

**Prompt B (Test):**
```
[Exact prompt with all formatting - change ONLY what you're testing]
```

**Trials**: [Number] per condition

**Measurement**: [How you'll evaluate - BPM variance, presence/absence of element, subjective rating scale, etc.]

### Results

| Trial | Prompt A Result | Prompt B Result |
|-------|----------------|----------------|
| 1     | [measurement]  | [measurement]  |
| 2     | [measurement]  | [measurement]  |
| 3     | [measurement]  | [measurement]  |
| 4     | [measurement]  | [measurement]  |
| 5     | [measurement]  | [measurement]  |

**Summary Statistics:**
- Prompt A: Mean [X], Std Dev [Y]
- Prompt B: Mean [X], Std Dev [Y]

**Audio Examples:**
- Prompt A Trial 1: [Link]
- Prompt B Trial 1: [Link]
[Include at least 1-2 examples per condition]

### Analysis

[What the data shows]

### Conclusion

**Result**: ✅ VERIFIED / ⚠️ INCONCLUSIVE / ❌ REFUTED

**Confidence**: High / Medium / Low

**Evidence Label**: [VERIFIED / ANECDOTAL / etc.]

**Notes**: [Anything unexpected, edge cases, limitations]
```

---

## Test Types

### Effectiveness Tests (A/B Comparison)

**Question**: "Does X produce better/more consistent results than Y?"

**Examples:**
- "120 BPM" vs "fast tempo" → Which has lower BPM variance?
- "Crescendo" vs "building intensity" → Which produces clearer dynamic changes?
- "Piano only" vs "no drums" → Which more reliably excludes other instruments?

**Method:**

1. **Define "better"**: More consistent? Closer to target? More predictable?
2. **Create matched pairs**: Change ONLY the variable being tested
3. **Measure objectively**: Use tools when possible (BPM detection, dB meters)
4. **Calculate statistics**: Mean, standard deviation, variance
5. **Minimum 5 trials per condition** (more is better)

**Example Measurements:**
- BPM consistency: Use `detect_bpm.py` script, calculate variance
- Dynamic range: Measure dB difference between sections
- Instrument presence: Binary yes/no, calculate success rate
- Subjective quality: Use consistent rating scale (1-5), multiple raters if possible

**Template:**

```markdown
## Effectiveness Test: [X] vs [Y]

**Hypothesis**: [X] produces more [specific measurable outcome] than [Y]

**Prompt A**: [X version]
**Prompt B**: [Y version]
**N**: 5 per condition
**Measurement**: [Specific metric]

**Results**:
- Prompt A: Mean [value], SD [value], Range [min-max]
- Prompt B: Mean [value], SD [value], Range [min-max]
- Difference: [A-B], [%] more consistent/accurate

**Conclusion**: [Does data support hypothesis? By how much?]
```

---

### Reliability Tests (Consistency)

**Question**: "How often does X produce the expected result?"

**Examples:**
- "No drums" → Does it actually exclude drums? What % of the time?
- `[Long Intro]` → Does it extend intro? How consistently?
- "Soft heavy metal" → Does it produce softer metal? How reliably?

**Method:**

1. **Define success criteria upfront**: What counts as "working"?
2. **Generate 10+ samples** (minimum)
3. **Evaluate each**: Pass/fail against criteria
4. **Calculate percentage**: (passes / total) × 100
5. **Document failure modes**: When it fails, how does it fail?

**Template:**

```markdown
## Reliability Test: [Feature/Prompt]

**Hypothesis**: [Feature] works [expected %] of the time

**Prompt**: [Exact prompt]
**N**: 10 trials
**Success Criteria**: [Specific, measurable definition]

**Results**:
| Trial | Pass/Fail | Notes |
|-------|-----------|-------|
| 1     | Pass/Fail | [Why?] |
| 2     | Pass/Fail | [Why?] |
| ...   | ...       | ...    |

**Success Rate**: [X/10] = [%]

**Failure Modes**:
- [How it failed when it failed]

**Conclusion**: [Feature] works [actual %] of the time under these conditions
```

---

### Feature Verification Tests (Does It Work?)

**Question**: "Does feature X work at all?"

**Examples:**
- Do bar count tags control duration?
- Do exclusion tags prevent instruments?
- Do BPM specifications affect actual tempo?

**Method:**

1. **Test the feature** with clear expected behavior
2. **Minimum 5 trials**
3. **Compare expected vs actual**
4. **If it works**: Document reliability (see Reliability Tests)
5. **If it fails**: Document why and how

**Template:**

```markdown
## Feature Verification: [Feature Name]

**Hypothesis**: [Feature] produces [expected behavior]

**Prompt**: [Using the feature]
**N**: 5 trials
**Expected Behavior**: [Specific]
**Actual Behavior**: [What happened]

**Results**:
| Trial | Expected | Actual | Match? |
|-------|----------|--------|--------|
| 1     | [value]  | [value]| Y/N    |
| ...   | ...      | ...    | ...    |

**Conclusion**:
- ✅ Feature works: [If yes, proceed to reliability testing]
- ❌ Feature doesn't work: [Document evidence]
- ⚠️ Unclear: [More testing needed, what kind?]
```

---

## Reporting Results

### Where to Submit

1. **For verified findings**: Add to relevant documentation with VERIFIED label
2. **For anecdotal findings**: Add to documentation with ANECDOTAL label
3. **For unclear results**: Add to [needs-testing.md](../needs-testing.md)
4. **For community discussion**: [GitHub Discussions](https://github.com/oxygen-fragment/ai-music-tips-and-tricks/discussions)

### What to Include

**Required:**
- [ ] Completed test template (see above)
- [ ] All raw data or clear summary statistics
- [ ] Platform and version
- [ ] Date tested
- [ ] At least 1-2 audio examples per condition

**Recommended:**
- [ ] Links to all generated audio (if possible)
- [ ] Screenshots of settings
- [ ] Tool output (e.g., BPM detection results)
- [ ] Multiple tester confirmation (if available)

### Evidence Labels

Based on your test:
- **✅ VERIFIED**: Systematic test, n≥5, reproducible method, clear conclusion
- **👥 ANECDOTAL**: Smaller sample, less rigorous, but documented
- **❓ UNKNOWN**: Inconclusive, needs more testing

---

## Common Pitfalls

### ❌ Pitfall 1: Insufficient Sample Size

**Problem:**
```
Tested "120 BPM" once, got 118 BPM.
Conclusion: "120 BPM is inaccurate"
```

**Why it's wrong**: N=1, could be normal variance

**Fix**: Minimum 5 trials, measure variance

---

### ❌ Pitfall 2: Uncontrolled Variables

**Problem:**
```
Test A: "Pop song, 120 BPM, happy"
Test B: "Rock song, fast, energetic"
Conclusion: "120 BPM is more consistent than 'fast'"
```

**Why it's wrong**: Changed genre, mood, AND tempo specification

**Fix**: Change ONLY the variable being tested

---

### ❌ Pitfall 3: Vague Success Criteria

**Problem:**
```
Testing "No drums" tag
Trial 1: "Some percussion sounds" → Fail?
Trial 2: "Kick drum but no hi-hats" → Fail?
```

**Why it's wrong**: Unclear what counts as passing

**Fix**: Define success criteria upfront:
- Pass = Zero percussive elements
- Fail = Any drum, percussion, or rhythmic hits

---

### ❌ Pitfall 4: Confirmation Bias

**Problem:**
```
Hypothesis: "Crescendo" works better
Testing: Generated 10 samples, picked best 5 for each
Result: "Crescendo" examples sound better!
```

**Why it's wrong**: Cherry-picking results

**Fix**: Use ALL results, report ALL failures

---

### ❌ Pitfall 5: No Measurement Method

**Problem:**
```
Tested "120 BPM" vs "fast"
Result: "120 BPM sounds more consistent"
```

**Why it's wrong**: Subjective, not reproducible

**Fix**: Use objective measurement (BPM detection tool), report variance

---

### ❌ Pitfall 6: Testing Across Platform Updates

**Problem:**
```
Tests 1-5: Suno v5.0 (November 1)
Tests 6-10: Suno v5.1 (November 15)
Conclusion: Feature reliability decreased
```

**Why it's wrong**: Could be due to platform changes

**Fix**: Complete all trials on same platform version, or note version in each trial

---

## Example Tests

### Example 1: BPM Specification Consistency

```markdown
## Test: "120 BPM" vs "Fast Tempo" Consistency

**Date**: 2025-11-25
**Tester**: @username
**Platform**: Suno v5.0
**Hypothesis**: "120 BPM" produces more consistent tempo than "fast tempo"

### Method

**Settings:**
- Style Influence: 70%
- Weirdness: 50%
- Mode: Custom

**Prompt A (Specific):**
```
Style: Pop, 120 BPM, upbeat
[verse]
Sample lyrics here
[chorus]
More lyrics here
```

**Prompt B (Vague):**
```
Style: Pop, fast tempo, upbeat
[verse]
Sample lyrics here
[chorus]
More lyrics here
```

**Trials**: 10 per condition
**Measurement**: Actual BPM using detect_bpm.py script

### Results

| Trial | Prompt A (120 BPM) | Prompt B (fast) |
|-------|-------------------|-----------------|
| 1     | 118.2             | 128.5           |
| 2     | 121.7             | 135.2           |
| 3     | 119.8             | 122.1           |
| 4     | 120.3             | 140.3           |
| 5     | 122.1             | 118.9           |
| 6     | 118.9             | 131.7           |
| 7     | 119.5             | 125.8           |
| 8     | 121.2             | 137.2           |
| 9     | 120.8             | 129.4           |
| 10    | 119.1             | 133.6           |

**Summary Statistics:**
- Prompt A: Mean 120.16 BPM, Std Dev 1.12, Range 118.2-122.1
- Prompt B: Mean 130.27 BPM, Std Dev 6.95, Range 118.9-140.3
- Variance: Prompt A is 6.2× more consistent (lower std dev)

**Audio Examples:**
- Prompt A Trial 1: [link]
- Prompt B Trial 1: [link]

### Analysis

"120 BPM" specification:
- Stayed within ±2 BPM of target in all trials
- Very consistent (SD = 1.12)

"Fast tempo" specification:
- Wide range (118.9-140.3 BPM)
- Much higher variance (SD = 6.95)
- Averaged faster than "120 BPM" but unpredictable

### Conclusion

**Result**: ✅ VERIFIED

**Confidence**: High

**Evidence Label**: VERIFIED (n=10 per condition, objective measurement)

**Conclusion**: "120 BPM" produces significantly more consistent tempo than "fast tempo" (6.2× lower variance). Both specifications drift from exact values (±2 BPM typical), but numeric specification is far more predictable.

**Notes**: Tested only in pop genre. May need genre-specific testing for tempo-sensitive styles (trap, EDM, etc.)
```

---

### Example 2: Instrument Exclusion Reliability

```markdown
## Test: "Piano Only" vs "No Drums" Exclusion

**Date**: 2025-11-25
**Tester**: @username
**Platform**: Suno v5.0
**Hypothesis**: Positive specification ("piano only") is more reliable than negative ("no drums")

### Method

**Settings:**
- Style Influence: 70%
- Weirdness: 50%
- Mode: Custom

**Prompt A (Positive):**
```
Style: Ballad, piano only, unaccompanied, solo piano, no other instruments
[verse]
Sample lyrics
```

**Prompt B (Negative):**
```
Style: Ballad, no drums, no percussion
[verse]
Sample lyrics
```

**Trials**: 10 per condition

**Success Criteria:**
- **Prompt A Pass**: Only piano present, zero other instruments
- **Prompt B Pass**: Zero drums or percussion (other instruments OK)

### Results

**Prompt A (Piano Only):**
| Trial | Pass/Fail | Instruments Present |
|-------|-----------|-------------------|
| 1     | Pass      | Piano only |
| 2     | Fail      | Piano + strings |
| 3     | Pass      | Piano only |
| 4     | Pass      | Piano only |
| 5     | Fail      | Piano + vocal harmonies |
| 6     | Pass      | Piano only |
| 7     | Pass      | Piano only |
| 8     | Pass      | Piano only |
| 9     | Fail      | Piano + subtle bass |
| 10    | Pass      | Piano only |

**Success Rate**: 7/10 = 70%

**Prompt B (No Drums):**
| Trial | Pass/Fail | Instruments Present |
|-------|-----------|-------------------|
| 1     | Fail      | Piano + drums |
| 2     | Pass      | Piano + strings (no drums) |
| 3     | Fail      | Piano + percussion |
| 4     | Pass      | Piano + bass (no drums) |
| 5     | Fail      | Piano + hi-hats |
| 6     | Pass      | Piano only (no drums) |
| 7     | Fail      | Full drum kit |
| 8     | Pass      | Piano + synth (no drums) |
| 9     | Fail      | Piano + snare hits |
| 10    | Fail      | Piano + shakers |

**Success Rate**: 4/10 = 40%

**Audio Examples:**
- Prompt A Pass (Trial 1): [link]
- Prompt A Fail (Trial 2): [link]
- Prompt B Pass (Trial 2): [link]
- Prompt B Fail (Trial 1): [link]

### Analysis

**Positive specification ("piano only")**:
- 70% success rate
- Failures added complementary instruments (strings, bass) but maintained focus on piano
- Never added drums/percussion

**Negative specification ("no drums")**:
- 40% success rate
- Failures directly violated the constraint (added drums/percussion)
- Seemed to increase likelihood of percussion in some cases

### Conclusion

**Result**: ✅ VERIFIED

**Confidence**: High

**Evidence Label**: VERIFIED (n=10 per condition, clear pass/fail criteria)

**Conclusion**: Positive specification ("piano only") is 1.75× more reliable than negative specification ("no drums") for excluding unwanted instruments. However, even positive specification only works 70% of the time. For guaranteed instrument control, use multi-step generation or DAW editing.

**Notes**:
- Combined positive + negative ("piano only, no drums") not tested
- May be genre-dependent (tested ballad only)
- "Solo piano composition, classical style" might have higher success rate (needs testing)
```

---

## Tips for Effective Testing

### 1. Start Small, Then Scale
- Quick test (n=3): Is this worth investigating?
- Small test (n=5): Do I see a pattern?
- Full test (n=10+): Verify for VERIFIED label

### 2. Use Tools
- BPM detection: `scripts/testing/detect_bpm.py`
- Audio analysis: Audacity (spectrograms, waveforms)
- Timing: `scripts/testing/suno_timing_calculator.py`

### 3. Document Everything
- Take screenshots of settings
- Save all audio files (cloud storage)
- Write notes immediately (memory fades)

### 4. Collaborate
- Test others' hypotheses
- Ask for replication of your tests
- Different platforms behave differently

### 5. Know When to Stop
- Inconclusive after 10+ trials? → Mark as UNKNOWN, move on
- Clear pattern after 5 trials? → Can upgrade to VERIFIED if rigorous
- High variance? → May need larger sample or different measurement

---

## Next Steps

**After Testing:**
1. ✅ Complete test template
2. ✅ Label with appropriate evidence level
3. ✅ Submit findings (PR or issue)
4. ✅ Update relevant documentation
5. ✅ Add to needs-testing.md if follow-up needed

**Want to Help?**
Check [needs-testing.md](../needs-testing.md) for high-priority tests the community needs!

---

## See Also

- [Evidence Standards](../evidence-standards.md) - How we label claim quality
- [Needs Testing Tracker](../needs-testing.md) - What needs verification
- [Suno Bar Timing Research](../../research/suno_bar_timing_research_report.md) - Example of full systematic test
- [Contributing Guidelines](../../CONTRIBUTING.md) - How to submit findings
