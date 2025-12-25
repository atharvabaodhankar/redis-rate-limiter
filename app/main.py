from fastapi import FastAPI, Request, HTTPException
from limiter import is_allowed

app = FastAPI()


@app.get("/")
def home(request: Request):
    client_ip = request.client.host

    if not is_allowed(client_ip):
        raise HTTPException(status_code=429, detail="Too many requests")

    return {"message": "Request successful"}
