import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_character(async_client, auth_headers):
    character_data = {
        "name": "Test Character",
        "class_": "Warrior",
        "race": "Human",
        "gender": "Male",
        "age": "30",
        "height": "1.80",
        "weight": "80",
        "eye_color": "Blue",
        "skin_color": "White",
        "hair_color": "Brown",
        "description": "Test description",
        "allies": "Test allies",
        "notes": "Test notes",
        "traits": "Test traits",
        "history": "Test history",
        "equipment": "Test equipment"
    }
    response = await async_client.post(
        "/my-characters",
        json=character_data,
        headers=auth_headers
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test Character"

@pytest.mark.asyncio
async def test_list_characters(async_client, auth_headers):
    response = await async_client.get("/my-characters", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_generate_text(async_client, auth_headers):
    prompt = "Name: Test Character\nDescription: A brave warrior"
    response = await async_client.post(
        "/my-characters/api/gerar-texto",
        json={"prompt": prompt},
        headers=auth_headers
    )
    assert response.status_code == 200
    assert "Generated Text" in response.json()