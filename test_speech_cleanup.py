import pyaudio
import wave
import whisper
import os
import threading
from pynput import keyboard

print("Press ENTER to start/stop recording")

recording, frames, audio, stream = False, [], None, None

def on_press(key):
    global recording, frames, audio, stream
    if key == keyboard.Key.enter:
        if not recording:
            recording, frames = True, []
            audio = pyaudio.PyAudio()
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
            def record():
                while recording:
                    frames.append(stream.read(1024))
            threading.Thread(target=record).start()
        else:
            recording = False
            stream.close()
            audio.terminate()

            with wave.open("temp.wav", 'wb') as f:
                f.setnchannels(1)
                f.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
                f.setframerate(16000)
                f.writeframes(b''.join(frames))

            text = whisper.load_model("small.en").transcribe("temp.wav")["text"].strip()
            print(f"📝 {text}")
            os.remove("temp.wav")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
