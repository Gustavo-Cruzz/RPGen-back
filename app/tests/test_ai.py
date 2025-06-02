import pytest
from httpx import AsyncClient
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_generate_text(async_client, auth_headers):
    test_prompt = "Generate a story about a brave knight"
    mock_response = MagicMock()
    mock_response.text = "Once upon a time..."
    
    with patch('app.services.ai_service.genai.Client') as mock_client:
        mock_client.return_value.models.generate_content.return_value = mock_response
        
        response = await async_client.post(
            "/api/gerar-texto",
            json={"prompt": test_prompt},
            headers=auth_headers
        )
        
        assert response.status_code == 200
        assert "Generated Text" in response.json()

@pytest.mark.asyncio
async def test_generate_image(async_client, auth_headers):
    test_prompt = "Generate an image of a castle"
    mock_response = MagicMock()
    mock_response.image_data = "base64imagedata..."
    
    with patch('app.services.ai_service.genai.Client') as mock_client:
        mock_client.return_value.models.generate_content.return_value = mock_response
        
        response = await async_client.post(
            "/api/gerar-imagem",
            json={"prompt": test_prompt},
            headers=auth_headers
        )
        
        assert response.status_code == 200
        assert "image_data" in response.json()