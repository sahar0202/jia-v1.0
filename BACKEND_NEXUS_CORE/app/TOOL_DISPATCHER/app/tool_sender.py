from fastapi import FastAPI

app = FastAPI(title="Tool Dispatcher (Demon Hand)")

@app.get("/health")
def health():
    return {"status":"ok","service":"Demon Hand aktif"}

@app.post("/send_email")
def send_email(data: dict):
    print(f"Send Email Tool: {data}")
    return {"status":"email_sent","recipient":"placeholder","message":"Email terkirim via Demon Hand"}
