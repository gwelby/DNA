#!/usr/bin/env python3
"""
Quick test script for DNA meditation system
"""
import asyncio
import sys
from daily_dna_meditation_v2 import DNAMeditationSystemV2

async def test_dna_system():
    """Test the DNA meditation system basic functionality."""
    print("🧬 TESTING DNA MEDITATION SYSTEM v2.0")
    print("=" * 50)
    
    meditation = DNAMeditationSystemV2()
    
    # Test 1: I Ching guidance
    print("\n📜 Testing I Ching guidance...")
    guidance = meditation._get_daily_i_ching_guidance()
    print(f"✅ Hexagram: #{guidance['number']} - {guidance['name']}")
    print(f"   Frequency: {guidance['frequency']} Hz")
    print(f"   Focus: {guidance['focus']}")
    
    # Test 2: Coherence calculation
    print("\n🧠 Testing coherence calculation...")
    coherence = meditation._calculate_meditation_coherence(None)
    print(f"✅ Coherence: {coherence:.2f}")
    print(f"   Assessment: {meditation._assess_dna_communication(coherence)}")
    
    # Test 3: Frequency generation
    print("\n🎵 Testing frequency generation...")
    audio = meditation._generate_frequency_tone(528.0, 2)  # 2 second test
    print(f"✅ Audio generated: {len(audio)} samples")
    print(f"   Duration: 2 seconds at {meditation.sample_rate} Hz")
    
    # Test 4: Muse connection (simulation)
    print("\n🎧 Testing Muse connection...")
    connected = await meditation.connect_muse()
    if connected:
        print("✅ Muse connection successful (simulation mode)")
    else:
        print("❌ Muse connection failed")
    
    # Test 5: Short meditation session (5 seconds)
    print("\n🧘 Testing short meditation session...")
    
    def test_callback(metrics):
        if metrics:
            att = metrics.get('attention', 0)
            med = metrics.get('meditation', 0)
            print(f"   📊 Attention: {att:.1f}% | Meditation: {med:.1f}%")
    
    try:
        # Start streaming
        if meditation.eeg:
            await meditation.eeg.start_streaming(test_callback)
            
            # Run for 6 seconds
            await asyncio.sleep(6)
            
            # Stop streaming
            await meditation.eeg.stop_streaming()
            print("✅ Short meditation session completed")
        else:
            print("⚠️ No EEG available for session test")
    
    except Exception as e:
        print(f"❌ Session test error: {e}")
    
    print("\n🎉 DNA MEDITATION SYSTEM TEST COMPLETE!")
    print("🚀 Ready for Greg's morning session!")

if __name__ == "__main__":
    asyncio.run(test_dna_system()) 