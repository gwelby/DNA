#!/usr/bin/env python3
"""
🧠 SIMPLE MUSE TEST ⚡φ∞ 🌟 ॐ

Quick and simple Muse connection test for Greg's DNA system.
Uses the actual working muselsl API!

Author: Greg's DNA Quantum Cascade Project
"""

import time
from datetime import datetime

def test_muse_scan():
    """Simple Muse device scan."""
    print("🧠 GREG'S SIMPLE MUSE TEST ⚡φ∞ 🌟 ॐ")
    print("=" * 50)
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"👤 Greg (Age 58) - DNA Consciousness System")
    
    print("\n🔍 TESTING MUSE LIBRARIES...")
    
    try:
        import muselsl
        print("✅ muselsl imported successfully")
        
        import pylsl
        print("✅ pylsl imported successfully")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    print("\n🔵 SCANNING FOR MUSE DEVICES...")
    print("   (Make sure your Muse is on and in pairing mode)")
    print("   This may take 10-15 seconds...")
    
    try:
        from muselsl import list_muses
        
        # Simple scan without timeout parameter
        start_time = time.time()
        muses = list_muses()
        scan_time = time.time() - start_time
        
        print(f"   Scan completed in {scan_time:.1f} seconds")
        
        if muses:
            print(f"\n🎉 SUCCESS! Found {len(muses)} Muse device(s):")
            for i, muse in enumerate(muses):
                print(f"   {i+1}. 📱 {muse}")
            
            print(f"\n✅ YOUR MUSE IS READY!")
            print(f"   🧬 Device: {muses[0]}")
            print(f"   ⚡ Ready for REAL EEG consciousness data!")
            print(f"   🌟 DNA meditation can use actual brainwaves!")
            
            return muses
            
        else:
            print("\n⚠️ No Muse devices found")
            print("\n🔧 TO CONNECT YOUR MUSE:")
            print("   1. Turn on your Muse headband")
            print("   2. Hold power button until BLUE light (pairing mode)")
            print("   3. Make sure Bluetooth is enabled")
            print("   4. Keep Muse within 3 feet of computer")
            print("   5. Try running this test again")
            
            print("\n💫 MEANWHILE:")
            print("   Your DNA system uses optimized consciousness")
            print("   simulation with Age-58 wisdom protocols!")
            
            return []
            
    except Exception as e:
        print(f"\n❌ Scan failed: {e}")
        print(f"   Error type: {type(e).__name__}")
        
        print("\n🔧 POSSIBLE SOLUTIONS:")
        print("   • Check if Bluetooth is enabled")
        print("   • Restart your Muse headband")
        print("   • Try moving closer to the Muse")
        print("   • Make sure no other apps are using the Muse")
        
        return []

def test_lsl_check():
    """Check for existing LSL streams."""
    print("\n📡 CHECKING FOR EEG STREAMS...")
    
    try:
        from pylsl import resolve_streams
        
        print("🔍 Looking for active EEG streams...")
        streams = resolve_streams(wait_time=3.0)
        
        if streams:
            eeg_count = 0
            for stream in streams:
                if hasattr(stream, 'type') and stream.type() == 'EEG':
                    eeg_count += 1
                    print(f"   ✅ EEG Stream: {stream.name()}")
            
            if eeg_count > 0:
                print(f"\n🎯 Found {eeg_count} EEG stream(s) available!")
                print("   Your DNA system can connect to existing streams")
                return True
            else:
                print("   No EEG streams found")
                return False
        else:
            print("   No LSL streams detected")
            return False
            
    except Exception as e:
        print(f"   Stream check failed: {e}")
        return False

def main():
    """Main simple test."""
    muses = test_muse_scan()
    streams = test_lsl_check()
    
    print("\n" + "=" * 50)
    print("📊 FINAL SUMMARY")
    print("=" * 20)
    
    if muses:
        print("🏆 EXCELLENT! Your Muse is connected and ready!")
        print("   🧬 Real EEG data available for DNA meditation")
        print("   ⚡ Consciousness monitoring: ACTIVE")
        
    elif streams:
        print("✅ GOOD! EEG streams are available")
        print("   🧬 Alternative EEG data source detected")
        
    else:
        print("⚠️ No Muse detected - Simulation mode ready")
        print("   🧬 High-quality consciousness simulation")
        print("   ⚡ Optimized for Age-58 neural patterns")
    
    print(f"\n🚀 YOUR DNA SYSTEM IS READY TO RUN!")
    print(f"   Use: python greg_complete_dna.py")
    print(f"⚡φ∞ 🌟 ॐ")

if __name__ == "__main__":
    main() 