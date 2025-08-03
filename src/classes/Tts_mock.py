"""
Mock TTS class for testing purposes when the real TTS has import issues
"""

class TTS:
    def __init__(self):
        self.synthesizer = None
    
    def generate_speech(self, text, output_path):
        """Mock speech generation - just creates an empty file"""
        import os
        with open(output_path, 'w') as f:
            f.write("Mock audio file")
        return output_path 