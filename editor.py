"""
Editor Module for Loom
Handles file operations and terminal output for the application state
"""

import os
import subprocess
from typing import Optional

class Editor:
    def __init__(self, output_file: str = "loom_output.txt"):
        self.output_file = output_file
        self._open_in_textedit()
    
    def _open_in_textedit(self):
        """Open the output file in TextEdit"""
        try:
            # Create file if it doesn't exist
            if not os.path.exists(self.output_file):
                with open(self.output_file, 'w', encoding='utf-8') as f:
                    f.write("")
            
            # Open in TextEdit
            subprocess.run(['open', '-a', 'TextEdit', self.output_file], check=True)
            print(f"📖 Opened {self.output_file} in TextEdit")
        except Exception as e:
            print(f"⚠️  Could not open TextEdit: {e}")
    
    def write_content(self, content: str) -> str:
        """Write content to the output file"""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"📝 Content written to {self.output_file}")
            return f"Content successfully written to {self.output_file}"
        except Exception as e:
            error_msg = f"Error writing to file: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg
    
    def append_content(self, content: str) -> str:
        """Append content to the output file"""
        try:
            with open(self.output_file, 'a', encoding='utf-8') as f:
                f.write(content)
            print(f"📝 Content appended to {self.output_file}")
            return f"Content successfully appended to {self.output_file}"
        except Exception as e:
            error_msg = f"Error appending to file: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg
    
    def read_content(self) -> Optional[str]:
        """Read current content from the output file"""
        try:
            if os.path.exists(self.output_file):
                with open(self.output_file, 'r', encoding='utf-8') as f:
                    return f.read()
            return None
        except Exception as e:
            print(f"❌ Error reading file: {str(e)}")
            return None
    
    def show_note(self, message: str) -> str:
        """Display a note to the user in the terminal"""
        formatted_message = f"💬 {message}"
        print(formatted_message)
        return "Note displayed to user"
    
    def show_status(self, message: str) -> str:
        """Display a status message to the user"""
        formatted_message = f"ℹ️  {message}"
        print(formatted_message)
        return "Status displayed to user"
    
    def clear_file(self) -> str:
        """Clear the output file"""
        try:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write("")
            print(f"🗑️  Cleared {self.output_file}")
            return f"File {self.output_file} cleared"
        except Exception as e:
            error_msg = f"Error clearing file: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg
    
    def cleanup(self) -> str:
        """Remove the output file"""
        try:
            if os.path.exists(self.output_file):
                os.remove(self.output_file)
                print(f"🗑️  Removed {self.output_file}")
                return f"File {self.output_file} removed"
            else:
                print(f"📄 File {self.output_file} doesn't exist")
                return f"File {self.output_file} doesn't exist"
        except Exception as e:
            error_msg = f"Error removing file: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg