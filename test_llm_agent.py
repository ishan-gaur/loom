"""
Simple test script for LLM Agent Module
"""

from llm_agent import LLMAgent
import os

def test_llm_agent():
    print("🧪 Testing LLM Agent Module")
    
    # Check if sample input exists
    if not os.path.exists("sample_input.txt"):
        print("❌ sample_input.txt not found")
        return
    
    input("Press ENTER to start the test and initialize LLM Agent...")
    
    # Create agent
    try:
        agent = LLMAgent()
        print("✅ LLM Agent initialized")
    except Exception as e:
        print(f"❌ Failed to initialize agent: {e}")
        return
    
    # Read sample input
    with open("sample_input.txt", "r") as f:
        sample_text = f.read().strip()
    
    print(f"📝 Sample input: {sample_text}")
    print()
    
    input("TextEdit should now be open. Press ENTER to send request to Claude...")
    
    # Process with agent
    agent.process_text(sample_text)
    
    input("Check TextEdit to verify Claude wrote the blog post content, then press ENTER to finish...")
    
    # Check if output file was created
    if os.path.exists("loom_output.txt"):
        print()
        print("📄 Output file contents:")
        with open("loom_output.txt", "r") as f:
            print(f.read())
    else:
        print("❌ No output file created")
    
    # Optional cleanup
    cleanup = input("\nDelete the output file? (y/N): ").strip().lower()
    if cleanup == 'y':
        agent.editor.cleanup()

if __name__ == "__main__":
    test_llm_agent()