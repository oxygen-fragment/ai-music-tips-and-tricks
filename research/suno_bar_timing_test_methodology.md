# Suno Bar Timing Test Methodology

## Hypothesis

Specifying "(element for X bars)" in Suno prompts controls the duration of that element with measurable accuracy.

## Test Design

### Control Variables

- **BPM:** 120 (middle ground, easy math: 1 bar = 2 seconds in 4/4)
- **Time Signature:** 4/4 (always)
- **Element:** "guitar solo" (consistent, recognizable)
- **Style:** "rock" (stable instrumentation)

### Test Cases

Run each test case **3 times** to assess consistency.

| Test ID | Prompt | Expected Duration | Purpose |
|---------|--------|-------------------|---------|
| CTRL-1 | No bar specification | Baseline | Establish natural duration |
| TEST-1 | (guitar solo for 1 bar) | 2.0s | Minimum viable duration |
| TEST-2 | (guitar solo for 2 bars) | 4.0s | Standard short duration |
| TEST-4 | (guitar solo for 4 bars) | 8.0s | Standard medium duration |
| TEST-8 | (guitar solo for 8 bars) | 16.0s | Extended duration |
| TEST-2.5 | (guitar solo for 2.5 bars) | 5.0s | Decimal bar handling |
| TEST-0.5 | (guitar solo for 0.5 bars) | 1.0s | Sub-bar precision |

### Full Prompt Template

```
[Intro]
(upbeat rock guitar riff)

[Verse]
Simple rock melody, steady drums

[Break]
{TEST ELEMENT HERE}

[Verse]
Back to the main melody

[End]
```

Replace `{TEST ELEMENT HERE}` with test case prompt.

**Why this structure:**

- Break section isolates the test element
- Surrounding structure ensures consistent context
- Easy to identify solo start/end in audio

## Measurement Protocol

### Tools Required

- Audio editor (Audacity, Logic, Ableton, etc.) with waveform view
- Spreadsheet for data collection

### Measurement Steps

1. **Import audio** into editor
2. **Identify solo start** - visual + audio cues (waveform spike, solo instrument entry)
3. **Identify solo end** - instrument drops out, verse returns
4. **Measure duration** - difference between start and end timestamps
5. **Record** to nearest 0.1 second

### Data Collection Template

```
Test ID: TEST-2
Run: 1/3
Specified Duration: 4.0s
Measured Duration: 4.3s
Error: +0.3s (+7.5%)
Notes: Clean start, slightly long tail on reverb
```

## Success Criteria

### Hypothesis Supported If

1. **Effect exists:** Specified bars produce different durations than control
2. **Directional:** Larger bar values → longer durations (monotonic)
3. **Accuracy:** Mean error within ±15% of expected duration
4. **Consistency:** Standard deviation within runs <20% of mean

### Hypothesis Rejected If

1. **No effect:** All test cases produce similar durations to control
2. **Random:** No correlation between specified bars and measured duration
3. **Inconsistent:** Same prompt produces wildly different durations (>40% variance)

## Analysis Method

### Step 1: Calculate Per-Test Metrics

For each test case:

```
Mean Duration = (Run1 + Run2 + Run3) / 3
Standard Deviation = σ
Error = Mean - Expected
Error % = (Error / Expected) * 100
```

### Step 2: Correlation Analysis

Plot specified bars (X) vs measured duration (Y).

- **Strong correlation (r > 0.9):** Bars work
- **Moderate (0.7 < r < 0.9):** Bars influence but imprecise
- **Weak (r < 0.7):** Bars don't work reliably

### Step 3: Decision Matrix

| Accuracy | Consistency | Verdict | Action |
|----------|-------------|---------|--------|
| <10% error | <10% SD | Excellent | Use with confidence, calculator valuable |
| 10-20% error | 10-20% SD | Acceptable | Use with rounding, note limitations |
| 20-30% error | 20-30% SD | Marginal | Use only for rough guidance |
| >30% error | >30% SD | Unreliable | Abandon approach, bars don't work |

## Quick Test (15 minutes)

If you want fast validation before full test:

1. Run **TEST-2** and **TEST-8** once each
2. Measure durations
3. **If TEST-8 ≈ 2x TEST-2:** Promising, continue full test
4. **If TEST-8 ≈ TEST-2:** Bars don't work, stop testing

## Expected Time Investment

- **Quick test:** 15 minutes
- **Full test:** 60-90 minutes (21 generations + measurement)
- **Analysis:** 15 minutes

## Red Flags to Watch For

1. **Suno ignores tags entirely** - solo doesn't appear where specified
2. **Tags work for placement but not duration** - solo appears in break but duration random
3. **Tags work sometimes** - inconsistent between generations
4. **Reverb/decay confusion** - hard to measure where solo "ends"

## Reporting Results

Summarize with:

```
Hypothesis: [SUPPORTED / REJECTED / INCONCLUSIVE]
Correlation: r = [value]
Mean Error: [X]% ± [SD]%
Recommendation: [Use confidently / Use with caution / Don't use]
```

## Post-Test

If bars work:

- Continue calculator development
- Test more complex scenarios (multiple tagged elements)
- Build timing library for common sections

If bars don't work:

- Investigate alternative timing approaches
- Test different tag formats
- Consider placement-only use cases
