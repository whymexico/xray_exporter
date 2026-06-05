import asyncio
import logging

from server import run_server

logger = logging.getLogger()

if __name__ == "__main__":
    logger.info(f"Starting..")
    asyncio.run(run_server())
