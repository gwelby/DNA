"""
Quantum Audio Therapy 2.0
Enhanced with Muse EEG Integration

This version includes real-time brainwave monitoring and adaptive audio therapy.
"""

import asyncio
import numpy as np
import json
import os
import time
import math
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Dict, List, Optional, Callable, Any, Awaitable

PHI = (1 + math.sqrt(5)) / 2

# Import our modules
try:
    from muse_eeg import MuseEEG, BluetoothMuseEEG
except ImportError:
    MuseEEG = None
    BluetoothMuseEEG = None

class HealingGoal(Enum):
    PAIN_RELIEF = "pain_relief"
    STRESS_REDUCTION = "stress_reduction"
    FOCUS_ENHANCEMENT = "focus_enhancement"
    DEEP_RELAXATION = "deep_relaxation"
    SLEEP_AID = "sleep_aid"
    MEDITATION = "meditation"
    SEIZURE_STABILIZATION = "seizure_stabilization"
    BUZZING_BURNING_RELIEF = "buzzing_burning_relief"
    QUANTUM_OM = "quantum_om"

@dataclass
class FrequencyPreset:
    name: str
    base_freq: float
    beat_freq: float
    carrier_type: str = 'sine'
    audio_type: str = 'binaural'  # 'binaural' or 'isochronic' or 'om'
    description: str = ''
    target_bands: Dict[str, float] = None  # Target EEG band powers
    duty_cycle: float = 0.5  # for isochronic tones
    fade_in: float = 0.0     # seconds of fade-in
    fade_out: float = 0.0    # seconds of fade-out
    
    def __post_init__(self):
        if self.target_bands is None:
            self.target_bands = {
                'delta': 0.0,
                'theta': 0.0,
                'alpha': 0.0,
                'beta': 0.0,
                'gamma': 0.0
            }

class QuantumAudioTherapy:
    def __init__(self, sample_rate=44100, duration=300, volume=0.5):
        self.sample_rate = sample_rate
        self.duration = duration
        self.volume = volume
        self.t = np.linspace(0, duration, int(sample_rate * duration), False)
        
        # Output directories
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.output_dir = os.path.join(self.base_dir, 'output')
        self.eeg_dir = os.path.join(self.output_dir, 'eeg_data')
        self.audio_dir = os.path.join(self.output_dir, 'audio_sessions')
        
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.eeg_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)
        
        # Session tracking
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_log = []
        self.current_preset = None
        self.eeg = None
        self.running = False
        
        # Initialize presets
        self.presets = self._initialize_presets()
    
    def _initialize_presets(self) -> Dict[str, FrequencyPreset]:
        """Initialize the frequency presets."""
        return {
            HealingGoal.PAIN_RELIEF.value: FrequencyPreset(
                name="Pain Relief",
                base_freq=174.0,
                beat_freq=7.83,
                carrier_type='sine',
                audio_type='binaural',
                description="Combines 174Hz (pain relief) with 7.83Hz (Schumann Resonance)",
                target_bands={'theta': 0.4, 'alpha': 0.6}
            ),
            HealingGoal.STRESS_REDUCTION.value: FrequencyPreset(
                name="Stress Reduction",
                base_freq=396.0,
                beat_freq=7.83,
                carrier_type='sine',
                audio_type='binaural',
                description="396Hz for releasing fear and anxiety with Schumann Resonance",
                target_bands={'alpha': 0.7, 'theta': 0.3}
            ),
            HealingGoal.FOCUS_ENHANCEMENT.value: FrequencyPreset(
                name="Focus Enhancement",
                base_freq=40.0,
                beat_freq=10.0,
                carrier_type='sine',
                audio_type='isochronic',
                description="40Hz gamma waves for focus and cognitive enhancement",
                target_bands={'beta': 0.6, 'gamma': 0.4}
            ),
            HealingGoal.DEEP_RELAXATION.value: FrequencyPreset(
                name="Deep Relaxation",
                base_freq=432.0,
                beat_freq=4.0,
                carrier_type='sine',
                audio_type='binaural',
                description="432Hz for deep relaxation and stress relief",
                target_bands={'alpha': 0.5, 'theta': 0.5}
            ),
            HealingGoal.SLEEP_AID.value: FrequencyPreset(
                name="Sleep Aid",
                base_freq=128.0,
                beat_freq=3.0,
                carrier_type='sine',
                audio_type='binaural',
                description="Delta waves for deep sleep and restoration",
                target_bands={'delta': 0.8, 'theta': 0.2}
            ),
            HealingGoal.MEDITATION.value: FrequencyPreset(
                name="Meditation",
                base_freq=528.0,
                beat_freq=8.0,
                carrier_type='sine',
                audio_type='binaural',
                description="528Hz for DNA repair and deep meditation",
                target_bands={'theta': 0.6, 'alpha': 0.4}
            ),
            HealingGoal.SEIZURE_STABILIZATION.value: FrequencyPreset(
                name="Seizure Stabilization",
                base_freq=40.0,
                beat_freq=40.0,
                carrier_type='sine',
                audio_type='isochronic',
                duty_cycle=1.0,
                description="40Hz isochronic pulse for seizure stabilization",
                target_bands={'gamma': 0.8}
            ),
            HealingGoal.BUZZING_BURNING_RELIEF.value: FrequencyPreset(
                name="Buzzing-Burning Relief",
                base_freq=432.0,
                beat_freq=2.5,
                carrier_type='sine',
                audio_type='isochronic',
                duty_cycle=0.3,
                fade_in=5.0,
                fade_out=5.0,
                description="Low-frequency isochronic with gentle fade to relieve buzzing/burning",
                target_bands={'theta': 0.7}
            ),
            HealingGoal.QUANTUM_OM.value: FrequencyPreset(
                name="Quantum OM Formula",
                base_freq=432.0,
                beat_freq=0.0,
                carrier_type='sine',
                audio_type='om',
                fade_in=1.0,
                fade_out=1.0,
                description="Sacred OM phi-harmonic formula audio"
            ),
        }
    
    async def connect_eeg(self):
        """Connect to the Muse EEG headset."""
        if self.eeg is None:
            # Use BLE integration (MU-02) with fallback to LSL
            self.eeg = BluetoothMuseEEG()
            
        if not self.eeg.connected:
            return await self.eeg.connect()
        return True
    
    async def start_session(self, goal: str, duration: int = None, use_eeg: bool = True):
        """Start a new therapy session."""
        if goal not in self.presets:
            print(f"❌ Unknown goal: {goal}")
            return False
        
        self.current_preset = self.presets[goal]
        self.duration = duration or self.duration
        self.running = True
        
        print(f"\n🌟 Starting {self.current_preset.name} session")
        print(f"🎯 Goal: {goal.replace('_', ' ').title()}")
        print(f"⏱  Duration: {self.duration} seconds")
        
        # Connect to EEG if requested
        if use_eeg:
            print("🔌 Connecting to Muse EEG...")
            if not await self.connect_eeg():
                print("⚠️ Could not connect to Muse EEG. Continuing without biofeedback.")
                use_eeg = False
            else:
                print("✅ Connected to Muse EEG")
        
        # Generate the audio
        audio = self._generate_audio()
        
        # Save the audio file
        audio_filename = f"{self.current_preset.name.lower().replace(' ', '_')}_{self.session_id}"
        audio_path = self._save_audio(audio, audio_filename)
        
        # Start the session
        session_data = {
            'session_id': self.session_id,
            'start_time': datetime.now().isoformat(),
            'goal': goal,
            'preset': asdict(self.current_preset),
            'duration': self.duration,
            'audio_file': audio_path,
            'eeg_connected': use_eeg,
            'metrics': []
        }
        
        # Start EEG streaming if connected
        if use_eeg:
            await self.eeg.start_streaming(self._eeg_callback)
        
        # Play the audio
        self._play_audio(audio)
        
        # Wait for session to complete
        start_time = time.time()
        while self.running and (time.time() - start_time < self.duration):
            await asyncio.sleep(1)
            # Check for early termination
            
        # Clean up
        await self.stop_session()
        return session_data
    
    async def _eeg_callback(self, metrics):
        """Callback for EEG data updates."""
        if not self.running or not metrics:
            return
        
        # Log the metrics
        self.session_log.append({
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics
        })
        
        # Simple adaptive feedback (can be enhanced)
        self._adaptive_feedback(metrics)
        
        # Print status
        print(f"🧠 Attention: {metrics['attention']:.1f}% | "
              f"Meditation: {metrics['meditation']:.1f}% | "
              f"Stress: {metrics['stress_index']:.1f}%")
    
    def _adaptive_feedback(self, metrics):
        """Adjust audio based on EEG feedback."""
        # This is a simple example - can be enhanced with more sophisticated algorithms
        if not self.current_preset:
            return
        
        # Calculate how well the current brain state matches the target
        match_score = self._calculate_state_match(metrics['band_powers'])
        
        # Simple adaptive logic (can be expanded)
        if match_score < 0.5:
            # Not matching target state well - could adjust frequency or volume
            pass
    
    def _calculate_state_match(self, current_bands):
        """Calculate how well current brain state matches target state."""
        if not self.current_preset or not self.current_preset.target_bands:
            return 0.0
        
        # Simple cosine similarity between current and target band powers
        current = np.array([current_bands.get(band, 0) for band in ['delta', 'theta', 'alpha', 'beta', 'gamma']])
        target = np.array([self.current_preset.target_bands.get(band, 0) for band in ['delta', 'theta', 'alpha', 'beta', 'gamma']])
        
        # Normalize
        current_norm = current / (np.linalg.norm(current) + 1e-10)
        target_norm = target / (np.linalg.norm(target) + 1e-10)
        
        # Cosine similarity
        similarity = np.dot(current_norm, target_norm)
        return float(similarity)
    
    def _generate_audio(self):
        """Generate the audio based on current preset."""
        if self.current_preset.audio_type == 'om':
            return self._generate_om_formula()
        if not self.current_preset:
            return None
            
        if self.current_preset.audio_type == 'binaural':
            audio = self._generate_binaural_beat(
                self.current_preset.base_freq,
                self.current_preset.beat_freq,
                self.current_preset.carrier_type
            )
            if self.current_preset.fade_in or self.current_preset.fade_out:
                audio = self._apply_envelope(audio, self.current_preset.fade_in, self.current_preset.fade_out)
            return audio
        else:  # isochronic
            audio = self._generate_isochronic_tone(
                self.current_preset.base_freq,
                self.current_preset.beat_freq,
                self.current_preset.duty_cycle,
                self.current_preset.carrier_type
            )
            if self.current_preset.fade_in or self.current_preset.fade_out:
                audio = self._apply_envelope(audio, self.current_preset.fade_in, self.current_preset.fade_out)
            return audio
    
    def _apply_envelope(self, sound: np.ndarray, fade_in: float, fade_out: float) -> np.ndarray:
        """Apply linear fade-in and fade-out to sound."""
        total = sound.shape[0]
        env = np.ones(total)
        fi = int(self.sample_rate * fade_in)
        fo = int(self.sample_rate * fade_out)
        if fi > 0:
            env[:fi] = np.linspace(0, 1, fi)
        if fo > 0:
            env[-fo:] = np.linspace(1, 0, fo)
        if sound.ndim == 2:
            env = env[:, None]
        return sound * env
    
    def _generate_binaural_beat(self, base_freq, beat_freq, carrier_type='sine'):
        """Generate binaural beats."""
        left_freq = base_freq - (beat_freq / 2)
        right_freq = base_freq + (beat_freq / 2)
        
        left_channel = self._generate_tone(left_freq, carrier_type)
        right_channel = self._generate_tone(right_freq, carrier_type)
        
        # Combine channels
        stereo_sound = np.column_stack((left_channel, right_channel))
        
        # Normalize to prevent clipping
        max_amplitude = np.max(np.abs(stereo_sound))
        if max_amplitude > 0:
            stereo_sound = (stereo_sound / max_amplitude) * self.volume
            
        return stereo_sound
    
    def _generate_isochronic_tone(self, freq, pulse_freq, duty_cycle=0.5, carrier_type='sine'):
        """Generate isochronic tones."""
        # Generate the carrier wave
        carrier = self._generate_tone(freq, carrier_type)
        
        # Generate the pulse envelope
        pulse = np.zeros_like(self.t)
        pulse_period = 1.0 / pulse_freq
        samples_per_period = int(self.sample_rate / pulse_freq)
        samples_high = int(samples_per_period * duty_cycle)
        
        for i in range(0, len(pulse), samples_per_period):
            end = min(i + samples_high, len(pulse))
            pulse[i:end] = 1.0
        
        # Apply the pulse to the carrier
        mono_sound = carrier * pulse
        
        # Convert to stereo
        stereo_sound = np.column_stack((mono_sound, mono_sound))
        
        # Normalize
        max_amplitude = np.max(np.abs(stereo_sound))
        if max_amplitude > 0:
            stereo_sound = (stereo_sound / max_amplitude) * self.volume
            
        return stereo_sound
    
    def _generate_tone(self, frequency, tone_type='sine', phase=0.0):
        """Generate a single tone."""
        if tone_type == 'sine':
            return np.sin(2 * np.pi * frequency * self.t + phase)
        elif tone_type == 'square':
            return np.sign(np.sin(2 * np.pi * frequency * self.t + phase))
        elif tone_type == 'sawtooth':
            return 2 * (self.t * frequency - np.floor(0.5 + self.t * frequency))
        else:  # triangle
            return 2 * np.abs(2 * (self.t * frequency - np.floor(self.t * frequency + 0.5)))
    
    def _generate_om_formula(self):
        """Generate the OM phi-harmonic formula audio."""
        # Build phi-harmonic frequencies
        freqs = [
            self.current_preset.base_freq * (PHI ** 0),
            self.current_preset.base_freq * (PHI ** 1),
            self.current_preset.base_freq * (PHI ** 2),
            self.current_preset.base_freq * (PHI ** PHI)
        ]
        # Sum and normalize
        waves = [self._generate_tone(f) for f in freqs]
        mix = sum(waves) / len(waves)
        # Apply envelope if configured
        if self.current_preset.fade_in or self.current_preset.fade_out:
            mix = self._apply_envelope(mix, self.current_preset.fade_in, self.current_preset.fade_out)
        return mix
    
    def _save_audio(self, audio, filename):
        """Save audio to file."""
        if audio is None:
            print("No audio data to save.")
            return None
            
        # Ensure the audio is in the correct range
        audio = np.clip(audio, -1.0, 1.0)
        
        # Convert to 16-bit PCM
        audio_int16 = (audio * 32767).astype(np.int16)
        
        # Save as WAV file
        output_path = os.path.join(self.audio_dir, f"{filename}.wav")
        
        try:
            import soundfile as sf
            sf.write(output_path, audio_int16, self.sample_rate, 'PCM_16')
        except ImportError:
            import wave
            # Fallback to built-in wave module
            channels = audio_int16.shape[1] if audio_int16.ndim > 1 else 1
            with wave.open(output_path, 'wb') as wf:
                wf.setnchannels(channels)
                wf.setsampwidth(2)  # 16-bit audio
                wf.setframerate(self.sample_rate)
                wf.writeframes(audio_int16.tobytes())
        
        print(f"💾 Saved audio to {output_path}")
        return output_path
    
    def _play_audio(self, audio):
        """Play audio through the default sound device."""
        if audio is None:
            print("No audio data to play.")
            return
            
        try:
            import sounddevice as sd
            sd.play(audio, self.sample_rate)
            # Don't wait here - we'll handle the timing in the session loop
        except Exception as e:
            print(f"Error playing audio: {e}")
    
    async def stop_session(self):
        """Stop the current session."""
        self.running = False
        
        # Stop EEG if connected
        if self.eeg and self.eeg.connected:
            await self.eeg.stop_streaming()
            
            # Save EEG data
            self.eeg.save_session_data()
        
        # Save session log
        self._save_session_log()
        
        print("\n✅ Session complete!")
    
    def _save_session_log(self):
        """Save the session log to a file."""
        if not self.session_log:
            return
            
        session_data = {
            'session_id': self.session_id,
            'start_time': self.session_log[0]['timestamp'] if self.session_log else None,
            'end_time': datetime.now().isoformat(),
            'preset': asdict(self.current_preset) if self.current_preset else None,
            'duration': self.duration,
            'metrics': self.session_log
        }
        
        log_file = os.path.join(self.output_dir, f"session_{self.session_id}.json")
        with open(log_file, 'w') as f:
            json.dump(session_data, f, indent=2)
        
        print(f"💾 Saved session log to {log_file}")

async def main():
    """Main function to demonstrate usage."""
    # Create a new therapy session
    therapy = QuantumAudioTherapy(duration=300, volume=0.5)  # 5-minute session
    
    # List available presets
    print("\n=== Available Therapy Presets ===")
    for i, (key, preset) in enumerate(therapy.presets.items(), 1):
        print(f"{i}. {preset.name}: {preset.description}")
    
    # Get user input
    try:
        choice = int(input(f"\nSelect a preset (1-{len(therapy.presets)}): ")) - 1
        preset_keys = list(therapy.presets.keys())
        if 0 <= choice < len(preset_keys):
            selected_preset = preset_keys[choice]
            
            # Ask about EEG
            use_eeg = input("Use Muse EEG for biofeedback? (y/n): ").lower() == 'y'
            
            # Start the session
            print("\n🚀 Starting therapy session...")
            print("   Press Ctrl+C to stop early\n")
            
            await therapy.start_session(selected_preset, use_eeg=use_eeg)
            
        else:
            print("❌ Invalid selection")
            
    except (ValueError, KeyboardInterrupt):
        print("\n❌ Session cancelled")
    finally:
        # Ensure cleanup
        await therapy.stop_session()

if __name__ == "__main__":
    asyncio.run(main())
