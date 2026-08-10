import requests
import json
import os
import sys

# Ensure Windows terminal handles emojis and special characters
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1:8b"
IDENTITY_FILE = "identity.json"

def load_identity():
    if os.path.exists(IDENTITY_FILE):
        with open(IDENTITY_FILE, "r", encoding='utf-8') as f:
            return json.load(f)
    return {"name": "Agent", "personality": "Professional"}

def ask_ai(identity, user_query):
    system_prompt = (
        f"You are {identity['name']}. Your personality is {identity['personality']}. "
        f"Maintain this persona in every response. Be helpful, concise, and direct."
    )
    
    payload = {
        "model": MODEL,
        "prompt": f"{system_prompt}\nUser: {user_query}\nAssistant:",
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        response.raise_for_status()
        return response.json().get("response", "I am having trouble processing that.")
    except requests.exceptions.RequestException:
        return "CRITICAL ERROR: I cannot reach my brain. Is Ollama running?"

def main():
    identity = load_identity()
    print(f"--- {identity['name']} ({identity['personality']}) is Online ---")
    print("Commands: 'exit' or 'quit' to disconnect.\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print(f"{identity['name']}: Disconnecting. Goodbye.")
                break
            
            answer = ask_ai(identity, user_input)
            print(f"\n{identity['name']}: {answer}\n")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()