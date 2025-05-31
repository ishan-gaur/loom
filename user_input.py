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
        self.whisper_model = whisper.load_model("small.en")
        
        # Recording state
        self.stop_event = threading.Event()
        self.frames = []
        self.stream = None
        self.record_thread = None
    
    def start_recording(self) -> None:
        """Start audio recording in separate thread"""
        if not self.stop_event.is_set():
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
        if self.stop_event.is_set():
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


if __name__ == "__main__":
    from pynput import keyboard
    
    print("🎙️  User Input Test")
    print("Hold SPACEBAR to record, release to transcribe")
    print("Press ESC to quit")
    print()
    
    user_input = UserInput()
    
    def on_press(key):
        if key == keyboard.Key.space:
            user_input.start_recording()
    
    def on_release(key):
        if key == keyboard.Key.space:
            text = user_input.stop_recording()
            if text:
                print(f"✅ Transcribed: {text}")
            else:
                print("❌ No speech detected")
        elif key == keyboard.Key.esc:
            print("👋 Exiting...")
            return False
    
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        pass
    finally:
        user_input.cleanup()