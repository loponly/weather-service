"""
Author: Enkhbat E
Date: 2024-09-09
Description: Weather service for fetching weather data from external API.
"""

import aiohttp
import logging

API_KEY = "69e872460b94787eac8b476c4b7f9177"  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

logger = logging.getLogger(__name__)

async def fetch_weather_data(city: str) -> dict:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(BASE_URL, params={"q": city, "appid": API_KEY}) as response:
                if response.status != 200:
                    logger.error(f"Failed to fetch weather data for city {city}: {await response.text()}")
                    raise Exception(f"Failed to fetch weather data: {await response.text()}")
                return await response.json()
    except Exception as e:
        logger.error(f"Exception occurred while fetching weather data for city {city}: {e}", exc_info=True)
        raise
