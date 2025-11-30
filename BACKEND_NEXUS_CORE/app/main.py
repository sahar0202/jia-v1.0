import os, requests
from fastapi import FastAPI

JIA_MODE = os.environ.get("JIA_OPERATIONAL_MODE", "LOCAL_MVP")
VAULT_ADDR = os.environ.get("VAULT_ADDR", "http://localhost:8200")
TOOL_DISPATCHER_URL = os.environ.get("TOOL_DISPATCHER_URL", "http://localhost:8001")

app = FastAPI(title=f"JIA Nexus Core - Mode: {JIA_MODE}")

class VectorDB:
    def retrieve(self, query):
        if JIA_MODE == "FULL_CLOUD":
            return f"[MATCHING ENGINE] {query}"
        return f"[CHROMADB] {query}"

class EvolutionAgent:
    def trigger_terraform(self):
        if JIA_MODE == "FULL_CLOUD":
            return {"status":"success","message":"Terraform triggered"}
        return {"status":"VETO_REQUIRED","message":"Manual apply required"}

db = VectorDB()
evo = EvolutionAgent()

@app.get("/status")
def status():
    return {"mode": JIA_MODE, "db": db.retrieve("health")}

@app.post("/command")
def command(cmd: dict):
    text = cmd.get("text","")
    if "buat server" in text.lower():
        return evo.trigger_terraform()
    elif "kirim email" in text.lower():
        try:
            r = requests.post(f"{TOOL_DISPATCHER_URL}/send_email", json={"payload": text})
            return {"status":"success","response":r.json()}
        except:
            return {"status":"error","message":"Dispatcher tidak aktif"}
    return {"status":"success","result":db.retrieve(text)}
