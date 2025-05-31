"""
Simple test to verify audio recording and Whisper transcription
"""

import time
import pyaudio
import wave
import whisper
import os

def test_basic_recording():
    # Audio configuration
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 3
    
    print("🎙️  Basic Audio Test")
    print(f"Recording for {RECORD_SECONDS} seconds...")
    
    # Initialize
    audio = pyaudio.PyAudio()
    
    # Open stream
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK
    )
    
    print("🔴 Recording now... speak something!")
    
    frames = []
    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("⏹️  Recording finished, processing...")
    
    # Stop and close
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    # Save to file
    filename = "test_recording.wav"
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
    # Load Whisper and transcribe
    print("🔄 Loading Whisper...")
    model = whisper.load_model("small.en")
    
    print("🔄 Transcribing...")
    result = model.transcribe(filename)
    
    print(f"📝 Transcribed: '{result['text'].strip()}'")
    
    # Cleanup
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == "__main__":
    test_basic_recording()