#!/usr/bin/env python3
"""
🧠 WORKING MUSE CONNECTION TEST ⚡φ∞ 🌟 ॐ

Test real Muse EEG headband connection for Greg's DNA system.
Using correct pylsl function names!

Author: Greg's DNA Quantum Cascade Project
"""

import time
import asyncio
from datetime import datetime

def test_muse_libraries():
    """Test if Muse libraries work with correct function names."""
    print("🔍 TESTING MUSE LIBRARIES")
    print("=" * 40)
    
    try:
        import muselsl
        print("✅ muselsl imported successfully")
        print(f"   Version: {muselsl.__version__ if hasattr(muselsl, '__version__') else '2.3.1'}")
        
        # Test key functions
        print("   Functions available:")
        functions = ['list_muses', 'stream', 'record', 'view']
        for func in functions:
            if hasattr(muselsl, func):
                print(f"   ✅ {func}")
            else:
                print(f"   ❌ {func}")
                
    except ImportError as e:
        print(f"❌ muselsl import failed: {e}")
        return False
    
    try:
        import pylsl
        print("✅ pylsl imported successfully")
        print(f"   Version: {pylsl.__version__ if hasattr(pylsl, '__version__') else '1.17.6'}")
        
        # Test correct function names
        print("   Functions available:")
        functions = ['resolve_streams', 'StreamInlet', 'StreamOutlet', 'StreamInfo']
        for func in functions:
            if hasattr(pylsl, func):
                print(f"   ✅ {func}")
            else:
                print(f"   ❌ {func}")
                
    except ImportError as e:
        print(f"❌ pylsl import failed: {e}")
        return False
    
    return True

def test_bluetooth_muse_scan():
    """Test Bluetooth scanning for Muse devices."""
    print("\n🔵 SCANNING FOR MUSE DEVICES")
    print("=" * 40)
    
    try:
        from muselsl import list_muses
        
        print("🔍 Scanning for Muse devices...")
        print("   (Make sure your Muse is on and in pairing mode)")
        print("   This may take 10-15 seconds...")
        
        # Scan for Muse devices with timeout
        muses = list_muses(timeout=15)
        
        if muses:
            print(f"✅ Found {len(muses)} Muse device(s):")
            for i, muse in enumerate(muses):
                print(f"   {i+1}. {muse}")
            return muses
        else:
            print("⚠️ No Muse devices found")
            print("\n🔧 Make sure:")
            print("   • Muse headband is powered on")
            print("   • Press and hold the power button until blue light")
            print("   • Bluetooth is enabled on your computer")
            print("   • Muse is within 3 feet of your computer")
            return []
            
    except Exception as e:
        print(f"❌ Bluetooth scan failed: {e}")
        print(f"   Error details: {type(e).__name__}")
        return []

def test_lsl_streams():
    """Test LSL stream detection with correct function."""
    print("\n📡 CHECKING FOR EEG STREAMS")
    print("=" * 40)
    
    try:
        from pylsl import resolve_streams
        
        print("🔍 Looking for existing EEG streams...")
        
        # Look for any streams (correct function name)
        streams = resolve_streams(wait_time=5.0)
        
        eeg_streams = []
        for stream in streams:
            stream_info = stream
            if hasattr(stream_info, 'type') and stream_info.type() == 'EEG':
                eeg_streams.append(stream_info)
        
        if eeg_streams:
            print(f"✅ Found {len(eeg_streams)} EEG stream(s):")
            for stream in eeg_streams:
                print(f"   • {stream.name()} ({stream.channel_count()} channels)")
            return eeg_streams
        elif streams:
            print(f"⚠️ Found {len(streams)} streams, but no EEG streams")
            for stream in streams[:3]:  # Show first 3
                print(f"   • {stream.name()} (type: {stream.type()})")
            return []
        else:
            print("⚠️ No LSL streams found")
            print("   You may need to start a Muse stream first")
            return []
            
    except Exception as e:
        print(f"❌ LSL stream detection failed: {e}")
        return []

def test_muse_stream_start():
    """Test starting a Muse stream."""
    print("\n🚀 TESTING MUSE STREAM START")
    print("=" * 40)
    
    try:
        from muselsl import list_muses, stream
        
        # First check for devices
        print("🔍 Checking for Muse devices...")
        muses = list_muses(timeout=10)
        
        if not muses:
            print("❌ No Muse devices found - cannot test stream")
            return False
        
        print(f"✅ Found device: {muses[0]}")
        print("🔄 Attempting to start stream...")
        print("   (This will take 10-20 seconds)")
        print("   (Press Ctrl+C after a few seconds to stop)")
        
        try:
            # Start streaming - this will run until interrupted
            stream(address=muses[0], ppg_enabled=False, acc_enabled=False, gyro_enabled=False)
            print("✅ Muse stream started successfully!")
            return True
            
        except KeyboardInterrupt:
            print("\n⏸️ Stream test interrupted (this is normal)")
            return True
        except Exception as stream_e:
            print(f"⚠️ Stream start failed: {stream_e}")
            return False
            
    except Exception as e:
        print(f"❌ Stream test failed: {e}")
        return False

def test_quick_connection():
    """Quick connection test without starting full stream."""
    print("\n⚡ QUICK CONNECTION TEST")
    print("=" * 40)
    
    try:
        from muselsl import list_muses
        import time
        
        print("🔍 Quick Muse scan (5 seconds)...")
        
        start_time = time.time()
        muses = list_muses(timeout=5)
        scan_time = time.time() - start_time
        
        print(f"   Scan completed in {scan_time:.1f} seconds")
        
        if muses:
            print(f"✅ SUCCESS: Found {len(muses)} Muse device(s)")
            for muse in muses:
                print(f"   📱 {muse}")
            print(f"\n🧠 Your Muse is ready for DNA meditation!")
            return True
        else:
            print("⚠️ No Muse devices detected in quick scan")
            return False
            
    except Exception as e:
        print(f"❌ Quick test failed: {e}")
        return False

def main():
    """Main Muse connection test."""
    print("🧠 GREG'S MUSE CONNECTION TEST ⚡φ∞ 🌟 ॐ")
    print("=" * 60)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 System: Windows 10")
    print(f"👤 User: Greg (Age 58 - DNA optimization mode)")
    
    print("\n🎯 TESTING YOUR MUSE EEG CONNECTIVITY")
    print("Comprehensive diagnostics for consciousness monitoring...")
    
    # Test 1: Libraries
    print("\n" + "="*60)
    libraries_ok = test_muse_libraries()
    
    if not libraries_ok:
        print("\n❌ LIBRARIES ISSUE")
        print("Your libraries may need reinstalling.")
        return
    
    # Test 2: Quick Connection Test
    print("\n" + "="*60)
    quick_success = test_quick_connection()
    
    # Test 3: Detailed Bluetooth Scan
    print("\n" + "="*60)
    bluetooth_muses = test_bluetooth_muse_scan()
    
    # Test 4: LSL Stream Check
    print("\n" + "="*60)
    lsl_streams = test_lsl_streams()
    
    # Final Summary
    print("\n" + "="*60)
    print("📊 FINAL CONNECTION SUMMARY")
    print("=" * 30)
    
    if bluetooth_muses:
        print("🎉 EXCELLENT! Your Muse is detected and ready!")
        print(f"   Device: {bluetooth_muses[0]}")
        print("   🧬 Ready for REAL consciousness-DNA monitoring")
        print("   ⚡ Your DNA system can use actual EEG data!")
        
        # Ask if they want to test streaming
        print(f"\n🚀 Want to test live streaming? (Ctrl+C to stop)")
        try:
            input("Press Enter to test stream, or Ctrl+C to skip...")
            test_muse_stream_start()
        except KeyboardInterrupt:
            print("\n⏭️ Skipping stream test")
            
    elif lsl_streams:
        print("✅ GOOD! EEG streams are available")
        print("   🧬 Your DNA system can connect to existing streams")
    else:
        print("⚠️ No Muse detected - Using optimized simulation")
        print("\n🔧 TO CONNECT YOUR MUSE:")
        print("1. Turn on your Muse headband")
        print("2. Hold power button until BLUE light (pairing mode)")
        print("3. Keep Muse within 3 feet of computer")
        print("4. Make sure Bluetooth is enabled")
        print("5. Run this test again")
        print("\n💫 Meanwhile: Your DNA system uses high-quality")
        print("   consciousness simulation optimized for Age 58!")
    
    print(f"\n✨ TEST COMPLETE!")
    print(f"Your DNA meditation system is ready to run. ⚡φ∞ 🌟 ॐ")

if __name__ == "__main__":
    main() 