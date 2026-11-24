from datetime import datetime, timezone

from fastapi import FastAPI, Request

app = FastAPI(title="Lab 1 — HTTP Server")


@app.get("/")
def root():
    return {"message": "Hello! This is lab 1 server."}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/info")
def info(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client_ip": request.client.host,
    }
