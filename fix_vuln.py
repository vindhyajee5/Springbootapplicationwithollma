import json
import subprocess

# Load report
with open("springbootreport.json") as f:
    data = json.load(f)

# Extract HIGH
high = [
    v for v in data["report"]["vulnerabilities"]
    if v["severity"] == "HIGH"
]

print("HIGH vulnerabilities:", len(high))

# Prompt
prompt = f"""
You are DevSecOps expert.
Suggest exact fixes for these vulnerabilities.
Give dependency upgrade + docker fix.

{high}
"""

# Call Ollama
subprocess.run(["ollama", "run", "llama3", prompt])