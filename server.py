import uvicorn

from fastapi import FastAPI
from routes import metrics


app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

app.include_router(metrics.router)

async def run_server():
    config = uvicorn.Config(
        app=app,
        host="0.0.0.0",
        port=9200,
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()