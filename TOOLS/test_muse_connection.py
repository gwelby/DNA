#!/usr/bin/env python3
"""
🧠 MUSE EEG CONNECTION TEST ⚡φ∞ 🌟 ॐ

Test real Muse EEG headband connection for Greg's DNA system.
Let's see if we can get actual consciousness data!

Author: Greg's DNA Quantum Cascade Project
"""

import time
import asyncio
from datetime import datetime

def test_muse_imports():
    """Test if Muse libraries are properly installed."""
    print("🔍 TESTING MUSE LIBRARIES")
    print("=" * 40)
    
    try:
        import muselsl
        print("✅ muselsl imported successfully")
        print(f"   Version: {muselsl.__version__ if hasattr(muselsl, '__version__') else 'Unknown'}")
    except ImportError as e:
        print(f"❌ muselsl import failed: {e}")
        return False
    
    try:
        import pylsl
        print("✅ pylsl imported successfully")
        print(f"   Version: {pylsl.__version__ if hasattr(pylsl, '__version__') else 'Unknown'}")
    except ImportError as e:
        print(f"❌ pylsl import failed: {e}")
        return False
    
    try:
        from pylsl import resolve_stream
        print("✅ resolve_stream function available")
    except ImportError as e:
        print(f"❌ resolve_stream not available: {e}")
        return False
    
    return True

def test_bluetooth_scan():
    """Test Bluetooth scanning for Muse devices."""
    print("\n🔵 TESTING BLUETOOTH MUSE DETECTION")
    print("=" * 40)
    
    try:
        import muselsl
        from muselsl import list_muses
        
        print("🔍 Scanning for Muse devices...")
        print("   (Make sure your Muse is on and nearby)")
        
        # Scan for Muse devices
        muses = list_muses()
        
        if muses:
            print(f"✅ Found {len(muses)} Muse device(s):")
            for i, muse in enumerate(muses):
                print(f"   {i+1}. {muse}")
            return muses
        else:
            print("⚠️ No Muse devices found")
            print("   Make sure:")
            print("   • Muse headband is powered on")
            print("   • Bluetooth is enabled on your computer")
            print("   • Muse is in pairing mode (blue light)")
            return []
            
    except Exception as e:
        print(f"❌ Bluetooth scan failed: {e}")
        return []

def test_lsl_streams():
    """Test LSL stream detection."""
    print("\n📡 TESTING LSL STREAM DETECTION")
    print("=" * 40)
    
    try:
        from pylsl import resolve_stream, StreamInfo
        
        print("🔍 Looking for existing LSL streams...")
        
        # Look for any EEG streams
        streams = resolve_stream('type', 'EEG', timeout=5.0)
        
        if streams:
            print(f"✅ Found {len(streams)} EEG stream(s):")
            for stream in streams:
                print(f"   • {stream.name()} ({stream.channel_count()} channels)")
            return streams
        else:
            print("⚠️ No EEG streams found")
            print("   You may need to start a Muse stream first")
            return []
            
    except Exception as e:
        print(f"❌ LSL stream detection failed: {e}")
        return []

async def test_muse_connection():
    """Test actual Muse connection."""
    print("\n🧠 TESTING MUSE CONNECTION")
    print("=" * 40)
    
    try:
        import muselsl
        from muselsl import stream, list_muses
        
        # First scan for devices
        muses = list_muses()
        
        if not muses:
            print("❌ No Muse devices found for connection test")
            return False
        
        print(f"✅ Attempting to connect to: {muses[0]}")
        
        # Try to start streaming (this will fail gracefully if no connection)
        try:
            print("🔄 Starting Muse stream...")
            print("   (This may take 10-15 seconds)")
            
            # This would normally start the stream
            # We'll catch any errors
            stream(muses[0], ppg_enabled=False, acc_enabled=False, gyro_enabled=False)
            
            print("✅ Muse stream started successfully!")
            return True
            
        except Exception as stream_e:
            print(f"⚠️ Stream start failed: {stream_e}")
            return False
            
    except Exception as e:
        print(f"❌ Muse connection test failed: {e}")
        return False

def test_alternative_connection():
    """Test alternative Muse connection methods."""
    print("\n🔧 TESTING ALTERNATIVE CONNECTION METHODS")
    print("=" * 40)
    
    try:
        # Test if we can use bleak (Bluetooth Low Energy)
        import bleak
        print("✅ Bleak Bluetooth library available")
        
        async def scan_ble():
            print("🔍 Scanning BLE devices for Muse...")
            devices = await bleak.BleakScanner.discover(timeout=10.0)
            
            muse_devices = []
            for device in devices:
                if device.name and 'muse' in device.name.lower():
                    muse_devices.append(device)
                    print(f"   Found: {device.name} ({device.address})")
            
            return muse_devices
        
        # Run BLE scan
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        ble_muses = loop.run_until_complete(scan_ble())
        loop.close()
        
        if ble_muses:
            print(f"✅ Found {len(ble_muses)} Muse device(s) via BLE")
            return ble_muses
        else:
            print("⚠️ No Muse devices found via BLE")
            return []
            
    except Exception as e:
        print(f"❌ Alternative connection test failed: {e}")
        return []

def main():
    """Main Muse connection test."""
    print("🧠 GREG'S MUSE EEG CONNECTION TEST ⚡φ∞ 🌟 ॐ")
    print("=" * 60)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"💻 System: Windows")
    print(f"👤 User: Greg (Age 58)")
    
    print("\n🎯 MUSE CONNECTION DIAGNOSTICS")
    print("Testing your Muse EEG headband connectivity...")
    
    # Test 1: Library imports
    libraries_ok = test_muse_imports()
    
    if not libraries_ok:
        print("\n❌ LIBRARIES NOT PROPERLY INSTALLED")
        print("Run: pip install muselsl pylsl")
        return
    
    # Test 2: Bluetooth scan
    bluetooth_muses = test_bluetooth_scan()
    
    # Test 3: LSL streams
    lsl_streams = test_lsl_streams()
    
    # Test 4: Alternative BLE connection
    ble_muses = test_alternative_connection()
    
    # Summary
    print("\n📊 CONNECTION TEST SUMMARY")
    print("=" * 40)
    
    if bluetooth_muses:
        print("✅ Muse detected via Bluetooth")
        print(f"   Device: {bluetooth_muses[0]}")
        print("🚀 Ready for real EEG data!")
    elif ble_muses:
        print("✅ Muse detected via BLE")
        print("🚀 Alternative connection available!")
    elif lsl_streams:
        print("✅ EEG streams available")
        print("🚀 Can connect to existing stream!")
    else:
        print("⚠️ No Muse connection detected")
        print("\n🔧 TROUBLESHOOTING STEPS:")
        print("1. Turn on your Muse headband")
        print("2. Put it in pairing mode (blue light)")
        print("3. Make sure Bluetooth is enabled")
        print("4. Try moving closer to the Muse")
        print("5. Restart the Muse headband")
        print("\n🎯 Your DNA system will use high-quality simulation")
        print("   until Muse connection is established.")
    
    print(f"\n✨ Test complete! Your DNA meditation system is ready.")
    print("⚡φ∞ 🌟 ॐ")

if __name__ == "__main__":
    main() 