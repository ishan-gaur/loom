# Loom: Voice-Based Text Editor

Voice-only text editing with LLM collaboration to stress-test STT/TTS/agent systems.

## Setup

```bash
pip install pyaudio whisper-openai anthropic pynput python-dotenv
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
python loom.py
```

## Usage

- Hold **SPACEBAR** to record
- Release to process with Whisper → Claude
- Open `loom_output.txt` in TextEdit for responses
- **ESC** to quit