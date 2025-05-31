# Loom: Voice-Based Text Editor

Voice-only text editing with LLM collaboration to stress-test STT/TTS/agent systems.

## Setup

### macOS PyAudio Installation
```bash
brew install portaudio
```

### Install Dependencies
```bash
pip install pyaudio whisper-openai anthropic pynput python-dotenv
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
python loom.py
```

### macOS Accessibility Permissions
If you see this error:
```
This process is not trusted! Input event monitoring will not be possible until it is added to accessibility clients.
```
Add your terminal or IDE to System Preferences → Security & Privacy → Accessibility.

## Usage

### Test User Input Module
```bash
python user_input.py
```
- Hold **SPACEBAR** to record
- Release to transcribe with Whisper
- **ESC** to quit

### Full Application (coming soon)
```bash
python loom.py
```
- Hold **SPACEBAR** to record
- Release to process with Whisper → Claude
- Open `loom_output.txt` in TextEdit for responses
- **ESC** to quit