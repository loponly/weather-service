import aiosqlite
import logging

DATABASE = "events.db"
logger = logging.getLogger(__name__)

async def init_db():
    try:
        async with aiosqlite.connect(DATABASE) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS weather_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    timestamp INTEGER,
                    file_path TEXT
                )
            """)
            await db.commit()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}", exc_info=True)
        raise

async def log_event(city: str, timestamp: int, file_path: str):
    try:
        await init_db()
        async with aiosqlite.connect(DATABASE) as db:
            await db.execute("""
                INSERT INTO weather_events (city, timestamp, file_path)
                VALUES (?, ?, ?)
            """, (city, timestamp, file_path))
            await db.commit()
        logger.info(f"Logged event for city {city} at timestamp {timestamp} with file {file_path}")
    except Exception as e:
        logger.error(f"Error logging event for city {city}: {e}", exc_info=True)
        raise
