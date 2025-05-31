# Loom: Voice-Based Text Editor

Voice-only text editing with LLM collaboration to stress-test STT/TTS/agent systems.

## Setup

### macOS PyAudio Installation
```bash
brew install portaudio
```

### Install Dependencies
```bash
pip install pyaudio whisper-openai anthropic pynput python-dotenv transformers huggingface-hub[hf_xet]
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
echo "HF_TOKEN=your_hugging_face_token_here" >> .env
python loom.py
```

### Hugging Face Setup
1. Go to https://huggingface.co/settings/tokens
2. Create a new token with "Read" permissions
3. Add it to your `.env` file as `HF_TOKEN=your_token_here`

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
