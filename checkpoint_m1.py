import os
import sys
import json
import requests
from pathlib import Path

# Helper to fix Windows encoding issues
sys.stdout.reconfigure(encoding='utf-8')

def check_file(name): return Path(name).exists()

# Load Identity
if os.path.exists("identity.json"):
    with open("identity.json", "r", encoding='utf-8') as f:
        identity = json.load(f)
else:
    identity = {"name": "JARVIS", "personality": "Funny"}

print("═══════════════════════════════════════════════════════")
print("             AI WEEK – YANTRAX")
print("      MISSION 1 : THE COMMUNICATION BRIDGE")
print("═══════════════════════════════════════════════════════")
print("Workshop Progress")
print("████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 15%")
print(f"Connecting {identity['name']} to the AI Brain...")

# Verification Logic
brain_exists = check_file("brain_m1.py")
try:
    res = requests.get("http://localhost:11434/api/tags")
    ollama_online = True
except:
    ollama_online = False

print(f"{'✓' if brain_exists else '✗'} brain_m1.py created")
print(f"{'✓' if ollama_online else '✗'} AI Brain (Ollama) Online")
print(f"✓ Personality: {identity['personality']}")

print("═══════════════════════════════════════════════════════")
print("Assistant Status")
print("🟢 System Ready")
print("🟢 Mind")
print("⚪ Memory")
print("⚪ Skills")
print("⚪ Documents")
print("⚪ Actions")
print("⚪ Digital Assistant")
print("═══════════════════════════════════════════════════════")

if brain_exists and ollama_online:
    print("MISSION 1 COMPLETE")
    print("Next Mission")
    print("📓 MISSION 2 : GIVE YOUR ASSISTANT A NOTEBOOK")
else:
    print("🔴 MISSION INCOMPLETE: Check the errors above.")
print("═══════════════════════════════════════════════════════")