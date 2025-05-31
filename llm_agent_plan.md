# LLM Agent Module Implementation Plan

## Overview
Build the second module in Loom's three-module architecture: an LLM agent that takes transcribed text and processes it with Claude using tool calling capabilities.

## Core Requirements
- Receive transcribed text from User Input Module
- Send text to Claude via Anthropic API
- Implement tool calling system for file operations and user notifications
- Handle Claude responses and execute tool calls

## Tool Calling Design
Based on PROJECT_PLAN.md, implement these initial tools:
1. `write_to_file(content)` - Rewrites entire file with new content
2. `show_note_to_user(message)` - Displays message in terminal alongside TextEdit artifact

## Module Interface
```python
class LLMAgent:
    def __init__(self, api_key: str)
    def process_text(self, transcribed_text: str) -> None
    def _execute_tool_call(self, tool_name: str, args: dict) -> str
```

## Implementation Steps
1. Create basic LLMAgent class with Claude API integration
2. Implement tool calling framework 
3. Add write_to_file tool that writes to `loom_output.txt`
4. Add show_note_to_user tool for terminal notifications
5. Create sample input file with test scenario
6. Create simple test script to verify Claude integration
7. Test with sample input before integrating with User Input Module

## File Structure
- `llm_agent.py` - Main agent implementation
- `sample_input.txt` - Test input: "Write an opening paragraph for my blog post about diffusion models, summarizing the development of the field"
- `test_llm_agent.py` - Test script for Claude integration
- Update `loom.py` to integrate User Input + LLM Agent modules

## Technical Considerations
- Use Anthropic Python SDK for Claude API calls
- Handle API errors gracefully with fallback messages
- Keep tool responses concise and actionable
- Ensure file writing doesn't conflict with concurrent access

## Test Scenario
Sample input: "Write an opening paragraph for my blog post about diffusion models, summarizing the development of the field"
Expected behavior: Claude should use write_to_file tool to create opening paragraph in loom_output.txt

## Success Criteria
- Agent receives sample text and makes appropriate tool calls
- Files are written correctly to `loom_output.txt`
- User notifications appear in terminal
- Sample scenario produces quality blog post opening paragraph
- Integration with User Input Module works seamlessly