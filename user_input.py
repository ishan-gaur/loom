"""
User Input Module for Loom
Handles audio recording and transcription using Whisper
"""

import os
import time
import threading
import pyaudio
import wave
import whisper
from typing import Optional

class UserInput:
    def __init__(self):
        # Audio configuration
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000
        
        # Initialize audio and Whisper
        self.audio = pyaudio.PyAudio()
        print("🔄 Loading Whisper model...")
        self.whisper_model = whisper.load_model("small.en")
        print("✅ Whisper model loaded and ready!")
        
        # Recording state
        self.stop_event = threading.Event()
        self.stop_event.set()  # Initially not recording
        self.frames = []
        self.stream = None
        self.record_thread = None
    
    def start_recording(self) -> None:
        """Start audio recording in separate thread"""
        if self.record_thread and self.record_thread.is_alive():
            return
            
        self.stop_event.clear()
        self.frames = []
        
        # Open audio stream
        self.stream = self.audio.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )
        
        print("🔴 Recording...")
        
        # Record in separate thread
        def record_audio():
            while not self.stop_event.is_set():
                try:
                    data = self.stream.read(self.CHUNK)
                    self.frames.append(data)
                except Exception as e:
                    print(f"❌ Recording error: {e}")
                    break
                    
        self.record_thread = threading.Thread(target=record_audio)
        self.record_thread.start()
    
    def stop_recording(self) -> Optional[str]:
        """Stop recording and return transcribed text"""
        if self.stop_event.is_set() or not self.frames:
            return None
            
        self.stop_event.set()
        
        # Wait for recording thread to finish
        if self.record_thread:
            self.record_thread.join()
        
        # Close audio stream
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        
        print("⏹️  Processing...")
        
        # Save audio to temporary file
        temp_filename = f"temp_audio_{int(time.time())}.wav"
        try:
            with wave.open(temp_filename, 'wb') as wf:
                wf.setnchannels(self.CHANNELS)
                wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
                wf.setframerate(self.RATE)
                wf.writeframes(b''.join(self.frames))
            
            # Check if we actually recorded anything
            if len(self.frames) == 0:
                print("🔇 No audio recorded")
                return None
            
            # Transcribe with Whisper
            result = self.whisper_model.transcribe(temp_filename)
            transcribed_text = result["text"].strip()
            
            if transcribed_text:
                print(f"📝 Transcribed: {transcribed_text}")
                return transcribed_text
            else:
                print("🔇 No speech detected")
                return None
                
        except Exception as e:
            print(f"❌ Transcription error: {e}")
            return None
        finally:
            # Clean up temp file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
    
    def cleanup(self) -> None:
        """Clean up audio resources"""
        if not self.stop_event.is_set():
            self.stop_recording()
        self.audio.terminate()


def fallback_input_mode(user_input):
    """Simple terminal-based recording mode"""
    print("📱 Terminal Mode: Press ENTER to start/stop recording")
    print("Type 'quit' to exit")
    print()
    
    recording = False
    
    while True:
        if not recording:
            command = input("Press ENTER to start recording (or 'quit'): ").strip().lower()
            
            if command == 'quit':
                print("👋 Exiting...")
                break
            
            if command == '':  # User pressed ENTER
                print("🔴 Recording... Press ENTER to stop")
                user_input.start_recording()
                recording = True
        else:
            input()  # Wait for ENTER to stop
            text = user_input.stop_recording()
            recording = False
            
            if text:
                print(f"✅ Transcribed: {text}")
            else:
                print("❌ No speech detected")
            print()



if __name__ == "__main__":
    print("🎙️  User Input Test")
    
    user_input = UserInput()
    
    try:
        fallback_input_mode(user_input)
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
    finally:
        user_input.cleanup()