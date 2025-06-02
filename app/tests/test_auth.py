import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_user(async_client):
    user_data = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "newpassword"
    }
    response = await async_client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    assert "username" in response.json()
    assert response.json()["username"] == "newuser"

@pytest.mark.asyncio
async def test_login_user(async_client, test_user):
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = await async_client.post("/auth/register", json=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_get_current_user(async_client, auth_headers):
    response = await async_client.get("/auth/me", headers=auth_headers)
    assert response.status_code == 200
    assert "username" in response.json()