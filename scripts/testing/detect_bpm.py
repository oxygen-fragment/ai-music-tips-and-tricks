#!/usr/bin/env python3
"""
BPM Detector using librosa
Analyzes audio files and estimates tempo
"""

import sys
import librosa
import numpy as np

def detect_bpm(audio_file, show_confidence=False):
    """
    Detect BPM of audio file.
    
    Args:
        audio_file: path to audio file
        show_confidence: if True, return tempo and confidence
    
    Returns:
        float or tuple: BPM value (or BPM, confidence)
    """
    # Load audio file
    y, sr = librosa.load(audio_file)
    
    # Detect tempo
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    # Convert to scalar if array
    if isinstance(tempo, np.ndarray):
        tempo = float(tempo[0]) if len(tempo) > 0 else float(tempo)
    else:
        tempo = float(tempo)
    
    if show_confidence:
        # Calculate confidence based on beat strength
        onset_env = librosa.onset.onset_strength(y=y, sr=sr)
        pulse = librosa.beat.plp(onset_envelope=onset_env, sr=sr)
        confidence = float(np.mean(pulse))
        return tempo, confidence
    
    return tempo


def detect_bpm_multiple_methods(audio_file):
    """
    Use multiple detection methods and show results.
    Helps identify when BPM detection is ambiguous.
    """
    y, sr = librosa.load(audio_file)
    
    # Method 1: Standard beat tracker
    tempo1, _ = librosa.beat.beat_track(y=y, sr=sr)
    tempo1 = float(tempo1[0]) if isinstance(tempo1, np.ndarray) else float(tempo1)
    
    # Method 2: Onset strength
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    tempo2 = librosa.feature.tempo(onset_envelope=onset_env, sr=sr)
    tempo2 = float(tempo2[0]) if isinstance(tempo2, np.ndarray) else float(tempo2)
    
    # Method 3: Autocorrelation
    ac = librosa.autocorrelate(onset_env)
    tempo3_period = np.argmax(ac[1:]) + 1
    tempo3 = 60 * sr / (tempo3_period * 512)  # 512 is hop_length
    
    return {
        'beat_track': tempo1,
        'onset_strength': tempo2,
        'autocorrelation': tempo3,
        'mean': np.mean([tempo1, tempo2, tempo3]),
        'std': np.std([tempo1, tempo2, tempo3])
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python detect_bpm.py <audio_file> [--detailed]")
        print("\nSupported formats: mp3, wav, ogg, flac, m4a")
        print("\nExamples:")
        print("  python detect_bpm.py song.mp3")
        print("  python detect_bpm.py song.mp3 --detailed")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    detailed = '--detailed' in sys.argv
    
    try:
        if detailed:
            print(f"Analyzing: {audio_file}")
            print("=" * 50)
            results = detect_bpm_multiple_methods(audio_file)
            print(f"Beat Tracker:     {results['beat_track']:.1f} BPM")
            print(f"Onset Strength:   {results['onset_strength']:.1f} BPM")
            print(f"Autocorrelation:  {results['autocorrelation']:.1f} BPM")
            print("=" * 50)
            print(f"Mean:             {results['mean']:.1f} BPM")
            print(f"Std Deviation:    {results['std']:.1f} BPM")
            print()
            if results['std'] > 10:
                print("⚠ Warning: High variance suggests ambiguous tempo")
            else:
                print("✓ Consistent tempo detected")
        else:
            bpm = detect_bpm(audio_file)
            print(f"{bpm:.1f} BPM")
    
    except FileNotFoundError:
        print(f"Error: File not found: {audio_file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error analyzing audio: {e}")
        sys.exit(1)