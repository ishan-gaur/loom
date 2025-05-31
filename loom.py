#!/usr/bin/env python3
"""
Loom: Voice-based text editor with LLM collaboration
Initial prototype for terminal-based voice recording and processing
"""

import os
import sys
import time
import threading
import pyaudio
import wave
import whisper
import anthropic
from pynput import keyboard
from datetime import datetime
from dotenv import load_dotenv

# Configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
OUTPUT_FILE = "loom_output.txt"

class VoiceRecorder:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        self.audio = pyaudio.PyAudio()
        self.whisper_model = whisper.load_model("small.en")
        self.anthropic_client = anthropic.Anthropic()
        self.is_recording = False
        self.frames = []
        self.stream = None
        
    def start_recording(self):
        if self.is_recording:
            return
            
        self.is_recording = True
        self.frames = []
        
        self.stream = self.audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )
        
        print("🔴 Recording... (hold spacebar)")
        
        # Record audio in separate thread
        def record_audio():
            while self.is_recording:
                data = self.stream.read(CHUNK)
                self.frames.append(data)
                
        self.record_thread = threading.Thread(target=record_audio)
        self.record_thread.start()
    
    def stop_recording(self):
        if not self.is_recording:
            return
            
        self.is_recording = False
        self.record_thread.join()
        
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        
        print("⏹️  Recording stopped. Processing...")
        
        # Save audio to temporary file
        temp_filename = f"temp_audio_{int(time.time())}.wav"
        with wave.open(temp_filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(self.frames))
        
        # Process with Whisper
        try:
            result = self.whisper_model.transcribe(temp_filename)
            transcribed_text = result["text"].strip()
            print(f"📝 Transcribed: {transcribed_text}")
            
            if transcribed_text:
                self.send_to_claude(transcribed_text)
            
        except Exception as e:
            print(f"❌ Error processing audio: {e}")
        finally:
            # Clean up temp file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
    
    def send_to_claude(self, text):
        try:
            print("🤖 Sending to Claude...")
            
            message = self.anthropic_client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[
                    {"role": "user", "content": text}
                ]
            )
            
            response = message.content[0].text
            
            # Write to output file
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(f"\n--- {timestamp} ---\n")
                f.write(f"USER: {text}\n")
                f.write(f"CLAUDE: {response}\n")
            
            print(f"✅ Response written to {OUTPUT_FILE}")
            
        except Exception as e:
            print(f"❌ Error with Claude API: {e}")
    
    def cleanup(self):
        if self.is_recording:
            self.stop_recording()
        self.audio.terminate()

def on_press(key, recorder):
    if key == keyboard.Key.space:
        recorder.start_recording()

def on_release(key, recorder):
    if key == keyboard.Key.space:
        recorder.stop_recording()
    elif key == keyboard.Key.esc:
        print("\n👋 Exiting Loom...")
        return False

def main():
    print("🎙️  Loom Voice Editor Starting...")
    print("📋 Instructions:")
    print("   - Hold SPACEBAR to record")
    print("   - Release SPACEBAR to process")
    print(f"   - Open {OUTPUT_FILE} in TextEdit to see responses")
    print("   - Press ESC to quit")
    print()
    
    # Create output file if it doesn't exist
    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("Loom Voice Editor Output\n")
            f.write("=" * 30 + "\n")
    
    recorder = VoiceRecorder()
    
    try:
        # Set up keyboard listener
        with keyboard.Listener(
            on_press=lambda key: on_press(key, recorder),
            on_release=lambda key: on_release(key, recorder)
        ) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n👋 Interrupted. Exiting...")
    finally:
        recorder.cleanup()

if __name__ == "__main__":
    main()