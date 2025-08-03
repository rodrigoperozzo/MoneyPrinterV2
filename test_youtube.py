#!/usr/bin/env python3
"""
Simple test script for MoneyPrinter V2 YouTube functionality
"""

import sys
import os
sys.path.append('src')

def test_basic_imports():
    """Test basic imports without TTS"""
    try:
        import config
        print("✓ Config imported successfully")
        
        import utils
        print("✓ Utils imported successfully")
        
        import cache
        print("✓ Cache imported successfully")
        
        import constants
        print("✓ Constants imported successfully")
        
        print("\n✓ All basic imports successful!")
        return True
    except Exception as e:
        print(f"✗ Import error: {e}")
        return False

def test_g4f():
    """Test g4f functionality"""
    try:
        import g4f
        print("✓ g4f imported successfully")
        
        # Test a simple prompt
        response = g4f.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello, this is a test."}]
        )
        print(f"✓ g4f test response: {response[:50]}...")
        return True
    except Exception as e:
        print(f"✗ g4f error: {e}")
        return False

def test_moviepy():
    """Test MoviePy functionality"""
    try:
        import moviepy.editor
        print("✓ MoviePy imported successfully")
        
        # Test ImageMagick path
        from moviepy.config import change_settings
        change_settings({"IMAGEMAGICK_BINARY": "/opt/homebrew/bin/convert"})
        print("✓ ImageMagick path set successfully")
        return True
    except Exception as e:
        print(f"✗ MoviePy error: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Testing MoneyPrinter V2 Installation\n")
    
    tests = [
        ("Basic Imports", test_basic_imports),
        ("g4f (AI Models)", test_g4f),
        ("MoviePy (Video Processing)", test_moviepy),
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
        print("🎉 All tests passed! MoneyPrinter V2 is ready to use.")
        print("\nNext steps:")
        print("1. Configure your config.json file")
        print("2. Set up Firefox profiles for YouTube/Twitter")
        print("3. Run: python src/main.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main() 