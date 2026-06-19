from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.config import get_settings

settings = get_settings()

engine: AsyncEngine = create_async_engine(
    settings.database_url,
    pool_pre_ping = True,
)

async def check_database_connection() -> bool:
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))
        return result.scalar() == 1