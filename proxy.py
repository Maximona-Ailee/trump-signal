"""
Single‑port proxy for Hugging Face Spaces.
Requests to /api/* are forwarded to the internal FastAPI (port 8000).
All other requests go to the internal Streamlit (port 8501).
"""

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

STREAMLIT_URL = "http://127.0.0.1:8501"
API_URL = "http://127.0.0.1:8000"


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def proxy(request: Request, path: str):
    # Determine target backend
    if path.startswith("api/"):
        target = f"{API_URL}/{path}"
    else:
        target = f"{STREAMLIT_URL}/{path}"

    # Forward request
    async with httpx.AsyncClient() as client:
        req = client.build_request(
            method=request.method,
            url=target,
            headers={k: v for k, v in request.headers.items() if k.lower() != "host"},
            content=await request.body(),
        )
        resp = await client.send(req, stream=True)
        return StreamingResponse(
            resp.aiter_bytes(),
            status_code=resp.status_code,
            headers={k: v for k, v in resp.headers.items() if k.lower() != "content-length"},
        )