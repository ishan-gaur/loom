# Loom: Voice-Based Text Editor with LLM Collaboration

## What We're Building

A desktop application where:
- All text creation and editing happens through voice commands
- An LLM agent assists with the collaborative editing process
- Users can produce complete, understood artifacts without any keyboard input
- We stress-test current voice and AI technologies to find their breaking points

## Architecture Decisions

### Three Module Design
- User Input Module: Audio capture + Whisper transcription
- LLM Agent Module: Claude with tool calling capabilities  
- Application State Module: File writing + user notifications

### Tool Calling Design (Prototype)
- write_to_file(content): rewrites entire file with new content
- show_note_to_user(message): displays in terminal alongside TextEdit artifact

### Technical Stack
- Python for prototype (familiar, good for ML models)
- Future: Rust backend, JS frontend, Python for ML models
- Audio recording in separate thread to keep main thread responsive

## Basic Design

### Audio Processing Pipeline
- Capture audio input using microphone
- Process audio to text using OpenAI Whisper model
- Send extracted text to Claude via Anthropic API
- Display output on screen

### Initial Prototype - Terminal Interface
- Terminal-based application for simplicity
- Recording control: spacebar (push-to-talk for prototype)
  - User holds spacebar while speaking
  - Audio automatically sent to Whisper when spacebar released
  - Python app must have focus during recording
- Output display: write Anthropic response to file in current folder
  - User opens file in TextEdit on split screen next to Python terminal
  - Real-time viewing of generated content
- First run: Whisper model downloads automatically, notify user when ready to record