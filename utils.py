import os
import json
import httpx
import logging

from typing import List
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger()

SERVER_IP = os.getenv("SERVER_IP")

async def get_metrics() -> str:
    """Get metric from current endpoint"""
    async with httpx.AsyncClient() as client:
        r = await client.get(
            url=f"http://{SERVER_IP}/debug/vars"
        )
        if r.status_code != 200:
            logger.warning(f"Status Code: {r.status_code}")
            return ""
        
        return r.text

async def process_metrics(metrics: str) -> str:
    """Format: <metric_name>{<label>=<value>} <value>"""
    try:
        metrics = json.loads(metrics)
    except Exception as e:
        print(e)
        return ""
    
    prometheus_downlink: List[str] = [
        "# HELP xray_user_downlink Downlink sum in bytes", 
        "# TYPE xray_user_downlink gauge"
    ]
    prometheus_uplink: List[str] = [
        "# HELP xray_user_uplink Uplink sum in bytes",
        "# TYPE xray_user_uplink gauge"
    ]
    
    metrics = metrics.get("stats", {}).get("user", {})
    
    for k, v in metrics.items():
        downlink = v.get("downlink", 0)
        uplink = v.get("uplink", 0)
        
        prometheus_downlink.append(
            f"xray_user_downlink{{user=\"{k}\"}} {downlink}"
        )
        prometheus_uplink.append(
            f"xray_user_uplink{{user=\"{k}\"}} {uplink}"
        )
    
    return '\n'.join(prometheus_downlink) + "\n" + '\n'.join(prometheus_uplink)
