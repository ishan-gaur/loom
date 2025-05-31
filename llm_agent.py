"""
LLM Agent Module for Loom
Handles Claude API integration and tool calling capabilities
"""

import os
from typing import Dict, Any
from anthropic import Anthropic
from dotenv import load_dotenv
from editor import Editor

class LLMAgent:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        
        self.client = Anthropic(api_key=api_key)
        self.editor = Editor()
        
        # Define available tools
        self.tools = [
            {
                "name": "write_to_file",
                "description": "Replace entire contents of the loom output file with new content",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The complete content to replace the entire file with"
                        }
                    },
                    "required": ["content"]
                }
            },
            {
                "name": "show_note_to_user",
                "description": "Display a message to the user in the terminal",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "The message to show to the user"
                        }
                    },
                    "required": ["message"]
                }
            },

        ]
    
    def process_text(self, transcribed_text: str) -> None:
        """Process transcribed text with Claude and execute tool calls"""
        try:
            print(f"🤖 Processing: {transcribed_text}")
            
            system_prompt = """You are assisting with voice-based text editing. Key constraints:

- The user can only edit by completely rewriting the entire file
- Use write_to_file to replace ALL file contents, not append
- If editing existing content, read what's there and rewrite the whole thing
- The user cannot make incremental edits - only full file replacements
- Always provide complete, final versions when using write_to_file"""
            
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                system=system_prompt,
                tools=self.tools,
                messages=[{
                    "role": "user",
                    "content": transcribed_text
                }]
            )
            
            # Execute any tool calls in the response
            for content_block in response.content:
                if content_block.type == "tool_use":
                    result = self._execute_tool_call(content_block.name, content_block.input)
                    print(f"🔧 Tool executed: {content_block.name}")
                elif content_block.type == "text":
                    print(f"💬 Claude: {content_block.text}")
                    
        except Exception as e:
            print(f"❌ LLM Agent error: {e}")
            self.editor.show_note(f"Error processing request: {str(e)}")
    
    def _execute_tool_call(self, tool_name: str, args: Dict[str, Any]) -> str:
        """Execute a tool call and return the result"""
        if tool_name == "write_to_file":
            return self.editor.write_content(args["content"])
        elif tool_name == "show_note_to_user":
            return self.editor.show_note(args["message"])
        else:
            return f"Unknown tool: {tool_name}"
