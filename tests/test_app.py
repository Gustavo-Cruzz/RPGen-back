import sys
import os
import pytest

# Garante que a raiz do projeto está no sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run import app
from routes.api_routes import text_generator, image_generator

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'API está online!'}

def test_gerar_texto(client, mocker):
    mocker.patch.object(text_generator, 'generate_text', return_value="Texto gerado de exemplo")
    response = client.post('/api/gerar-texto', json={"prompt": "teste"})
    assert response.status_code == 200
    assert 'generated_text' in response.get_json()

def test_gerar_imagem(client, mocker):
    mocker.patch.object(image_generator, 'generate_image', return_value="imagem_em_base64_fake")
    response = client.post('/api/gerar-imagem', json={"prompt": "teste"})
    assert response.status_code == 200
    assert 'imagem_base64' in response.get_json()
