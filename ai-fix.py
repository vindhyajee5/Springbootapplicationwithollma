import json, subprocess

data=json.load(open("springbootreport.json"))
high=[v for v in data["report"]["vulnerabilities"] if v["severity"]=="HIGH"]

prompt=f"Suggest fixes for these: {high}"
subprocess.run(["ollama","run","llama3",prompt])