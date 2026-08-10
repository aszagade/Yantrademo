import shutil
import sys
import requests
import json
import os

def check_lib(lib_name):
    try:
        __import__(lib_name)
        return True
    except ImportError:
        return False

print("═══════════════════════════════════════════════════════")
print("             AI WEEK – YANTRAX")
print("      MISSION 0 : SYSTEM INITIALIZATION")
print("═══════════════════════════════════════════════════════")
print("Workshop Progress")
print("█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 5%")
print("Preparing your workshop environment...")

# 1. Environment Checks
python_check = sys.version_info >= (3, 0)
vscode_check = shutil.which("code") is not None
ollama_check = shutil.which("ollama") is not None

try:
    res = requests.get("http://localhost:11434/api/tags")
    model_check = any("llama3.1" in m['name'] for m in res.json().get('models', []))
except:
    model_check = False

print(f"{'✓' if python_check else '✗'} Python Installed")
print(f"{'✓' if vscode_check else '✗'} Visual Studio Code Found")
print(f"{'✓' if ollama_check else '✗'} Ollama Installed")
print(f"{'✓' if model_check else '✗'} AI Model (llama3.1:8b) Found")

if not (python_check and ollama_check and model_check):
    print("\n🔴 ERROR: Please fix the environment issues before proceeding.")
    sys.exit()

# 2. Identity Setup (The Onboarding)
print("═══════════════════════════════════════════════════════")
print("ONBOARDING: GIVE YOUR INTERN AN IDENTITY")
name = input("What is your Intern's name? : ")

print("\nSelect Personality:")
print("1. Professional (Polite & Direct)")
print("2. Casual (Friendly & Relaxed)")
print("3. Funny (Witty & Sarcastic)")
print("4. Roudy (Bold & Energetic)")
choice = input("Enter number (e.g., 1): ")

personalities = {
    "1": "Professional",
    "2": "Casual",
    "3": "Funny",
    "4": "Roudy"
}
personality = personalities.get(choice, "Professional")

# Save Identity
identity = {"name": name, "personality": personality}
with open("identity.json", "w") as f:
    json.dump(identity, f)

print(f"\n✓ Identity Saved: {name} ({personality})")

print("═══════════════════════════════════════════════════════")
print("Assistant Status")
print("🟢 System Ready")
print("⚪ Mind")
print("⚪ Memory")
print("⚪ Skills")
print("⚪ Documents")
print("⚪ Actions")
print("⚪ Digital Assistant")
print("═══════════════════════════════════════════════════════")
print("MISSION 0 COMPLETE")
print("Next Mission")
print("🧠 MISSION 1 : GIVE YOUR ASSISTANT A MIND")
print("═══════════════════════════════════════════════════════")