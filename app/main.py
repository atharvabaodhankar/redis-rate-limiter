from fastapi import FastAPI, Request, HTTPException, Response
from .limiter import check_rate_limit

app = FastAPI()


@app.get("/")
def home(request: Request, response: Response):
    api_key = request.headers.get("X-API-Key")

    if not api_key:
        raise HTTPException(status_code=401, detail="Missing API key")

    result = check_rate_limit(api_key)

    # Set rate-limit headers
    response.headers["X-RateLimit-Limit"] = str(result["limit"])
    response.headers["X-RateLimit-Remaining"] = str(result["remaining"])
    response.headers["X-RateLimit-Reset"] = str(result["reset"])

    if not result["allowed"]:
        raise HTTPException(status_code=429, detail="Too many requests")

    return {"message": "Request successful"}
