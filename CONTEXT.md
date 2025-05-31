# Development Context

## Working Style
- Make incremental changes, not large rewrites
- Allow course correction without waiting for long generations

## Loom Project
- Desktop application for voice-based text editing with LLM collaboration
- Goal: uncover holes in STT, TTS, and agent systems
- Constraint: users understand their artifacts without typing any keystrokes
- All interactions must be voice-only

## Context File Updates
- Add information as required for development
- Keep total file size small
- Push to git on every change to maintain history
- Purpose: store key conversation info to maintain context between sessions
- This file will be included in future requests to preserve continuity