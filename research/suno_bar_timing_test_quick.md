# Suno Bar Timing Quick Test

## Goal

Test if "(element for X bars)" has ANY measurable effect on duration.

## Time Required

20-30 minutes total

---

## Step 1: Generate Control (No Bar Tags)

**Prompt:**

```
[Intro]
Steady rock drums and bass

[Verse]
Electric guitar melody, moderate tempo

[Break]
Guitar solo

[Verse]
Back to main melody

[Outro]
Fade out
```

**Style/Genre:** rock

**Generate this ONCE.** Download as `control.mp3`

---

## Step 2: Measure Control BPM

Run:

```bash
python detect_bpm.py control.mp3
```

Note the BPM: _____ BPM

If you don't have the detector, use Audacity:

1. Find clear beat pattern
2. Select exactly 8 beats
3. Note duration in seconds
4. Calculate: BPM = (8 / duration) * 60

---

## Step 3: Generate Test Cases

Use **EXACT SAME PROMPT** but replace the Break section:

### TEST-A (Short)

```
[Break]
(guitar solo for 2 bars)
```

**Generate this ONCE.** Download as `test-2bar.mp3`

### TEST-B (Long)

```
[Break]
(guitar solo for 8 bars)
```

**Generate this ONCE.** Download as `test-8bar.mp3`

---

## Step 4: Measure Solo Durations

For each file (control, test-2bar, test-8bar):

1. Open in Audacity
2. Find where guitar solo starts (look for waveform change, listen for solo entry)
3. Find where guitar solo ends (solo drops out, verse returns)
4. Select solo section
5. Note duration at bottom of Audacity window

Record:

- Control solo duration: _____ seconds
- 2-bar solo duration: _____ seconds  
- 8-bar solo duration: _____ seconds

---

## Step 5: Calculate Expected Durations

Using measured BPM from Step 2:

**Formula:** duration = (bars × 4 × 60) / BPM

For 2 bars: (2 × 4 × 60) / [YOUR_BPM] = _____ seconds
For 8 bars: (8 × 4 × 60) / [YOUR_BPM] = _____ seconds

---

## Step 6: Compare Results

Fill in this table:

| Test | Specified | Expected | Measured | Error | Error % |
|------|-----------|----------|----------|-------|---------|
| Control | none | - | ___s | - | - |
| TEST-A | 2 bars | ___s | ___s | ___s | ___% |
| TEST-B | 8 bars | ___s | ___s | ___s | ___% |

**Error = Measured - Expected**
**Error % = (Error / Expected) × 100**

---

## Step 7: Decision

**Bars work if:**

- TEST-B duration > TEST-A duration (directional effect exists)
- TEST-B ≈ 4× TEST-A duration (ratio roughly matches 8÷2)
- Both within 30% of expected duration (reasonable accuracy)

**Bars don't work if:**

- All three similar duration (no effect)
- TEST-B shorter than TEST-A (wrong direction)
- No relationship between specified and measured

**Inconclusive if:**

- One test works, other doesn't (inconsistent)
- Ratio exists but accuracy >50% error (too imprecise)

---

## Example Results

```
Measured BPM: 125 BPM

Expected durations:
- 2 bars: (2 × 4 × 60) / 125 = 3.8s
- 8 bars: (8 × 4 × 60) / 125 = 15.4s

Measured durations:
- Control: 6.2s
- TEST-A (2 bars): 4.1s
- TEST-B (8 bars): 16.0s

Analysis:
- TEST-B > TEST-A ✓ (directional)
- Ratio: 16.0 / 4.1 = 3.9× (close to 4×) ✓
- TEST-A error: +0.3s (+7.9%) ✓
- TEST-B error: +0.6s (+3.9%) ✓

CONCLUSION: Bars work with good accuracy
```

---

## Quick Decision Tree

```
Did TEST-B last longer than TEST-A?
├─ NO → Bars don't work, stop testing
└─ YES → Continue

Is TEST-B roughly 3-5× longer than TEST-A?
├─ NO → Bars have effect but ratio wrong, investigate
└─ YES → Continue

Are both within 30% of expected?
├─ NO → Bars work but imprecise, use with caution
└─ YES → Bars work reliably, continue development
```

---

## What to Report Back

Just tell me:

1. The three measured durations
2. Your measured BPM
3. Your conclusion (work/don't work/inconclusive)

I'll help interpret if needed.
