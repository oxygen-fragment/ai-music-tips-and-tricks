#!/usr/bin/env python3
"""
Suno AI Timing Calculator & Prompt Builder
Calculates bar duration and generates formatted prompt tags
"""

def calculate_bars(seconds, bpm, beats_per_bar=4):
    """
    Calculate how many bars fit in a given duration.
    
    Args:
        seconds: desired duration in seconds
        bpm: beats per minute
        beats_per_bar: time signature numerator (default 4 for 4/4)
    
    Returns:
        float: number of bars
    """
    if seconds <= 0:
        raise ValueError(f"Duration must be positive (got {seconds}s)")
    if bpm <= 0 or bpm > 300:
        raise ValueError(f"BPM must be between 1-300 (got {bpm})")
    if beats_per_bar <= 0 or beats_per_bar > 16:
        raise ValueError(f"Beats per bar must be between 1-16 (got {beats_per_bar})")
    
    bars = (seconds * bpm) / (beats_per_bar * 60)
    return bars


def calculate_duration(bars, bpm, beats_per_bar=4):
    """
    Calculate duration in seconds for a given number of bars.
    
    Args:
        bars: number of bars
        bpm: beats per minute
        beats_per_bar: time signature numerator (default 4 for 4/4)
    
    Returns:
        float: duration in seconds
    """
    if bars <= 0:
        raise ValueError(f"Bars must be positive (got {bars})")
    if bpm <= 0 or bpm > 300:
        raise ValueError(f"BPM must be between 1-300 (got {bpm})")
    if beats_per_bar <= 0 or beats_per_bar > 16:
        raise ValueError(f"Beats per bar must be between 1-16 (got {beats_per_bar})")
    
    duration = (bars * beats_per_bar * 60) / bpm
    return duration


def round_bars(bars, suggest=True):
    """
    Round bars to practical values.
    
    Args:
        bars: calculated bars (float)
        suggest: if True, return dict with options
    
    Returns:
        dict or float: rounded value(s)
    """
    if not suggest:
        return round(bars * 2) / 2  # Round to nearest 0.5
    
    return {
        'exact': bars,
        'nearest_half': round(bars * 2) / 2,
        'nearest_whole': round(bars),
        'floor': int(bars),
        'ceil': int(bars) + (1 if bars % 1 > 0 else 0)
    }


def build_prompt_tag(description, seconds=None, bars=None, bpm=60, beats_per_bar=4, 
                     auto_round=True, format_style='parentheses'):
    """
    Build formatted Suno prompt tag with timing.
    
    Args:
        description: what's happening (e.g., "piano solo", "drum fill")
        seconds: desired duration in seconds (optional if bars provided)
        bars: number of bars (optional if seconds provided)
        bpm: beats per minute (default 60)
        beats_per_bar: time signature numerator (default 4)
        auto_round: round to nearest 0.5 bars (default True)
        format_style: 'parentheses' or 'brackets' (default 'parentheses')
    
    Returns:
        str: formatted prompt tag
    """
    if seconds is None and bars is None:
        raise ValueError("Must provide either seconds or bars")
    
    if bars is None:
        bars = calculate_bars(seconds, bpm, beats_per_bar)
    
    if auto_round:
        bars = round(bars * 2) / 2
    
    # Format bars display
    if bars == int(bars):
        bars_str = str(int(bars))
    else:
        bars_str = str(bars)
    
    bar_word = "bar" if bars == 1 else "bars"
    tag_content = f"{description} for {bars_str} {bar_word}"
    
    if format_style == 'brackets':
        return f"[{tag_content}]"
    return f"({tag_content})"


def interactive_builder():
    """Interactive prompt builder"""
    print("=== Suno Timing Prompt Builder ===\n")
    
    description = input("Description (e.g., 'piano solo'): ").strip()
    
    mode = input("Calculate from (s)econds or (b)ars? [s]: ").strip().lower() or 's'
    
    try:
        bpm = float(input("BPM [60]: ").strip() or 60)
        beats_per_bar = int(input("Beats per bar [4]: ").strip() or 4)
    except ValueError:
        print("\nError: BPM and beats per bar must be numbers")
        return None
    
    try:
        if mode == 's':
            seconds = float(input("Duration (seconds): ").strip())
            bars = calculate_bars(seconds, bpm, beats_per_bar)
            
            print(f"\nCalculated: {bars:.2f} bars")
            print(f"Rounded options:")
            rounded = round_bars(bars)
            for key, val in rounded.items():
                if key == 'exact':
                    continue
                duration = calculate_duration(val, bpm, beats_per_bar)
                print(f"  {key}: {val} bars ({duration:.1f}s)")
            
            bars = rounded['nearest_half']
        else:
            bars = float(input("Number of bars: ").strip())
            duration = calculate_duration(bars, bpm, beats_per_bar)
            print(f"\nDuration: {duration:.1f} seconds")
    
    except ValueError as e:
        if "could not convert" in str(e):
            print("\nError: Please enter valid numbers for duration/bars")
        else:
            print(f"\nError: {e}")
        return None
    
    format_style = input("\nFormat: (p)arentheses or (b)rackets? [p]: ").strip().lower()
    format_style = 'brackets' if format_style == 'b' else 'parentheses'
    
    prompt = build_prompt_tag(description, bars=bars, bpm=bpm, 
                              beats_per_bar=beats_per_bar, 
                              auto_round=False, format_style=format_style)
    
    print(f"\n{'='*50}")
    print(f"PROMPT TAG: {prompt}")
    print(f"{'='*50}\n")
    
    return prompt


def quick_reference():
    """Print quick reference for common durations at 60 BPM"""
    print("\n=== Quick Reference (60 BPM, 4/4 time) ===")
    print("Duration | Bars | Prompt Tag")
    print("-" * 45)
    
    durations = [4, 8, 10, 12, 16, 20, 24, 32]
    for seconds in durations:
        bars = calculate_bars(seconds, 60, 4)
        rounded = round(bars * 2) / 2
        print(f"{seconds:2d}s      | {rounded:4.1f} | (element for {rounded} bars)")
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command-line mode
        if sys.argv[1] == '--calc':
            # Advanced: Simple calculator
            if len(sys.argv) < 4:
                print("Usage: --calc <seconds> <bpm> [beats_per_bar]")
                sys.exit(1)
            
            try:
                seconds = float(sys.argv[2])
                bpm = float(sys.argv[3])
                beats = int(sys.argv[4]) if len(sys.argv) > 4 else 4
                bars = calculate_bars(seconds, bpm, beats)
                print(f"{bars:.2f} bars")
                print(f"Rounded: {round(bars * 2) / 2} bars")
            except ValueError as e:
                if "could not convert" in str(e):
                    print(f"Error: Invalid number format. Use: --calc <seconds> <bpm> [beats_per_bar]")
                    print(f"Example: --calc 10 120 4")
                else:
                    print(f"Error: {e}")
                sys.exit(1)
        
        elif sys.argv[1] == '--reverse':
            # Advanced: Reverse calculator
            if len(sys.argv) < 4:
                print("Usage: --reverse <bars> <bpm> [beats_per_bar]")
                sys.exit(1)
            
            try:
                bars = float(sys.argv[2])
                bpm = float(sys.argv[3])
                beats = int(sys.argv[4]) if len(sys.argv) > 4 else 4
                duration = calculate_duration(bars, bpm, beats)
                print(f"{duration:.2f} seconds")
            except ValueError as e:
                if "could not convert" in str(e):
                    print(f"Error: Invalid number format. Use: --reverse <bars> <bpm> [beats_per_bar]")
                    print(f"Example: --reverse 2.5 120 4")
                else:
                    print(f"Error: {e}")
                sys.exit(1)
        
        elif sys.argv[1] == '--quick':
            # Quick reference table
            quick_reference()
        
        elif sys.argv[1] == '--help':
            print("Suno Timing Calculator")
            print("\nModes:")
            print("  (no args)              Interactive prompt builder")
            print("  --calc <s> <bpm>       Calculate bars from seconds")
            print("  --reverse <bars> <bpm> Calculate seconds from bars")
            print("  --quick                Show reference table")
            print("\nExamples:")
            print("  python suno_timing_calculator.py")
            print("  python suno_timing_calculator.py --calc 10 60")
            print("  python suno_timing_calculator.py --reverse 2.5 60")
        
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for usage")
    else:
        # Interactive mode
        while True:
            result = interactive_builder()
            if result is None:
                print("Try again or press Ctrl+C to exit.\n")
                continue
            again = input("Build another? (y/n): ").strip().lower()
            if again != 'y':
                break