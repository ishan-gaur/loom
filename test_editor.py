"""
Simple test script for Editor Module
"""

from editor import Editor

def test_editor():
    print("🧪 Testing Editor Module")
    
    input("Press ENTER to start the test and open TextEdit...")
    
    editor = Editor()
    
    input("Press ENTER to write test content to the file...")
    
    # Test writing content
    result = editor.write_content("This is a test blog post opening.\n\nDiffusion models have revolutionized...")
    print(f"Write result: {result}")
    
    input("Press ENTER to read content back from file...")
    
    # Test reading content
    content = editor.read_content()
    print(f"Read content: {content[:50]}..." if content else "No content")
    
    input("Press ENTER to append additional content...")
    
    # Test appending
    editor.append_content("\n\nThis is additional content.")
    
    # Test notes
    editor.show_note("Processing completed successfully")
    editor.show_status("File operations finished")
    
    input("Check TextEdit to verify the content looks correct, then press ENTER to clean up...")
    
    # Cleanup
    editor.cleanup()

if __name__ == "__main__":
    test_editor()