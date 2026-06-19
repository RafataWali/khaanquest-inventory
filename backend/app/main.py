from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.database import check_database_connection

app = FastAPI(
    title = "KhaanQuest Inventory API",
    version = "0.1.0",
)


@app.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "khaanquest-inventory-api",
    }

@app.get("/health/database", tags=["System"])
async def database_health_check() -> dict[str, str]:
    try:
        connected = await check_database_connection()

        if connected:
            return {
                "status": "ok",
                "database": "connected",
            }
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code = 503,
            detail = "Database unavailable",
        ) from error
    
    raise HTTPException(
        status_code = 503,
        detail = "Database unavailable",
    )