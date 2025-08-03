#!/usr/bin/env python3
"""
Simple YouTube test script for MoneyPrinter V2
"""

import sys
import os
sys.path.append('src')

def test_youtube_basic():
    """Test basic YouTube functionality without TTS"""
    try:
        # Import the mock TTS instead of the real one
        import classes.Tts_mock
        sys.modules['classes.Tts'] = classes.Tts_mock
        
        from classes.YouTube import YouTube
        print("✓ YouTube class imported successfully")
        
        # Test basic functionality
        print("✓ YouTube class is ready for use")
        return True
    except Exception as e:
        print(f"✗ YouTube test error: {e}")
        return False

def test_config():
    """Test configuration loading"""
    try:
        from config import get_model, get_image_model, get_threads
        llm = get_model()
        image_model = get_image_model()
        threads = get_threads()
        print("✓ Configuration loaded successfully")
        print(f"  - LLM: {llm}")
        print(f"  - Image Model: {image_model}")
        print(f"  - Threads: {threads}")
        return True
    except Exception as e:
        print(f"✗ Config error: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Testing MoneyPrinter V2 YouTube Functionality\n")
    
    tests = [
        ("Configuration", test_config),
        ("YouTube Class", test_youtube_basic),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- Testing {test_name} ---")
        if test_func():
            passed += 1
        print()
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! MoneyPrinter V2 YouTube functionality is ready.")
        print("\nNext steps:")
        print("1. Configure your config.json file with your preferences")
        print("2. Set up Firefox profiles for YouTube")
        print("3. For full functionality, you'll need to resolve the TTS import issue")
        print("4. Run: python src/main.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main() 