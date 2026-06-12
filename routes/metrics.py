from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils import get_metrics, process_metrics

router = APIRouter()

@router.get("/metrics")
async def metrics_wrapper():
    data = await get_metrics()
    data = await process_metrics(data)
    
    return PlainTextResponse(
        content=data,
        status_code=200,
    )

