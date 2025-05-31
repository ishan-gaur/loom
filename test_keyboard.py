from pynput import keyboard
import threading
import time

print("Press any key to test permissions...")

detected = False

def on_press(key):
    global detected
    detected = True
    print(f"✅ Key detected: {key}")
    return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Wait 3 seconds for a key press
time.sleep(3)

if not detected:
    print("❌ No key detected - permissions likely missing")
    
listener.stop()