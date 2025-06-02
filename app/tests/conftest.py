import pytest
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.main import app
from app.models.user import User
from app.models.character import Character
from app.config import settings

@pytest.fixture
async def test_db():
    # Use a test database
    test_db_name = f"{settings.MONGODB_NAME}_test"
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    await init_beanie(database=client[test_db_name], document_models=[User, Character])
    yield client[test_db_name]
    # Cleanup
    await client.drop_database(test_db_name)

@pytest.fixture
async def async_client(test_db):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
async def test_user(async_client):
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = await async_client.post("/auth/register", json=user_data)
    return response.json()

@pytest.fixture
async def auth_headers(async_client, test_user):
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = await async_client.post("/auth/login", data=login_data)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}