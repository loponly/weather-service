"""
Author: Enkhbat E
Date: 2024-09-09
Description: Main application entry point.
"""

from fastapi import FastAPI, HTTPException, Query
from .weather_service import fetch_weather_data
from .storage import store_weather_data
from .database import log_event
from .cache import get_cached_data, cache_weather_data
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/weather")
async def get_weather(city: str = Query(...)):
    logger.info(f"Received request for weather data in city: {city}")
    
    try:
        # Check for cached data first
        cached_data = await get_cached_data(city)
        if cached_data:
            logger.info(f"Cache hit for city: {city}")
            return cached_data
        
        # Fetch weather data from external API
        weather_data = await fetch_weather_data(city)
        
        # Store weather data in local storage
        timestamp = int(time.time())
        file_path = await store_weather_data(city, weather_data, timestamp)
        
        # Log the event to the database
        await log_event(city, timestamp, file_path)
        
        # Cache the data
        await cache_weather_data(city, weather_data, timestamp)
        
        logger.info(f"Successfully processed weather data request for city: {city}")
        return weather_data

    except Exception as e:
        logger.error(f"Error processing request for city {city}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
