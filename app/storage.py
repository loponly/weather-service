import aiofiles
import json
import os
import logging

STORAGE_DIR = "weather_data"
logger = logging.getLogger(__name__)

os.makedirs(STORAGE_DIR, exist_ok=True)

async def store_weather_data(city: str, data: dict, timestamp: int) -> str:
    try:
        filename = f"{city}_{timestamp}.json"
        file_path = os.path.join(STORAGE_DIR, filename)
        
        async with aiofiles.open(file_path, 'w') as f:
            await f.write(json.dumps(data))
        
        logger.info(f"Weather data stored for city {city} in file {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Error storing weather data for city {city}: {e}", exc_info=True)
        raise
