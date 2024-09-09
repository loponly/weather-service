import aiofiles
import os
import json
import time
import logging

CACHE_DIR = "weather_cache"
CACHE_EXPIRY = 300  # 5 minutes

logger = logging.getLogger(__name__)
os.makedirs(CACHE_DIR, exist_ok=True)

async def get_cached_data(city: str) -> dict:
    try:
        for filename in os.listdir(CACHE_DIR):
            if filename.startswith(city):
                file_path = os.path.join(CACHE_DIR, filename)
                async with aiofiles.open(file_path, 'r') as f:
                    data = await f.read()
                    weather_data = json.loads(data)
                    if time.time() - weather_data["timestamp"] < CACHE_EXPIRY:
                        logger.info(f"Cache hit for city {city}, using cached data")
                        return weather_data
                    else:
                        os.remove(file_path)
                        logger.info(f"Cache expired for city {city}, deleted cache file")
                        return None
    except Exception as e:
        logger.error(f"Error retrieving cached data for city {city}: {e}", exc_info=True)
        return None

async def cache_weather_data(city: str, data: dict, timestamp: int):
    try:
        filename = f"{city}_{timestamp}.json"
        file_path = os.path.join(CACHE_DIR, filename)
        data["timestamp"] = timestamp
        
        async with aiofiles.open(file_path, 'w') as f:
            await f.write(json.dumps(data))
        
        logger.info(f"Cached weather data for city {city} in file {file_path}")
    except Exception as e:
        logger.error(f"Error caching weather data for city {city}: {e}", exc_info=True)
        raise
