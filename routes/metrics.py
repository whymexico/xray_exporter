from fastapi import APIRouter
from utils import get_metrics, process_metrics

router = APIRouter(prefix="/metrics")

@router.get("/")
async def metrics_wrapper():
    data = await get_metrics()
    data = process_metrics(data)
    
    return data

