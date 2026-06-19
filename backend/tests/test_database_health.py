from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

from app.main import app

client = TestClient(app)


def test_database_health_check_success(monkeypatch) -> None:
    async def fake_database_check() -> bool:
        return True

    monkeypatch.setattr(
        "app.main.check_database_connection",
        fake_database_check,
    )

    response = client.get("/health/database")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "database": "connected",
    }


def test_database_health_check_failure(monkeypatch) -> None:
    async def fake_database_check() -> bool:
        raise SQLAlchemyError("Database unavailable")

    monkeypatch.setattr(
        "app.main.check_database_connection",
        fake_database_check,
    )

    response = client.get("/health/database")

    assert response.status_code == 503
    assert response.json() == {
        "detail": "Database unavailable",
    }