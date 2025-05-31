# Development Context

## Context File
- Purpose: maintain conversation continuity between sessions
- Update as needed, keep small, ask before pushing to git
- Add design decisions to project plan as discussed

## Working Rules
- Incremental changes, not large rewrites
- Allow course correction without waiting for long generations
- Do not edit anything inside agent_logs folder
- Explain design approach before implementing large changes
- Discuss each major component piece by piece before moving to next
- Ask clarifying questions about intentions when unclear

## Coding Style Preferences
- Keep test code concise and minimal
- Avoid verbose comments and docstrings in test files
- Prefer short, direct implementations over long explanatory code
- Maintain readability: avoid overly dense single-line operations
- Use proper line breaks and clear flow even in compact code
- Balance conciseness with clarity - readable but not verbose

## Loom Project
- Desktop app: voice-only text editing with LLM collaboration
- Goal: uncover STT/TTS/agent system limitations
- Constraint: user understands artifacts without any keystrokes

