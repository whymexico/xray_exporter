from fastapi import APIRouter
from utils import get_metrics, process_metrics

router = APIRouter()

@router.get("/metrics")
async def metrics_wrapper():
    data = await get_metrics()
    data = await process_metrics(data)
    
    return data

