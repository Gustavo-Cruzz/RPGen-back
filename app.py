from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from flasgger import Swagger
import os
import logging

from api.text_generation import Text_Gen
from api.image_generation import Image_Gen
from routes.auth_routes import auth_bp
from routes.character_routes import character_bp

load_dotenv()

app = Flask(__name__)
CORS(app, resources={
    # This will cover routes like /api/gerar-texto, /api/gerar-imagem
    r"/api/*": {
        "origins": ["https://rp-gen.vercel.app", "http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    },
    # This is CRITICAL to cover your auth_bp routes which are prefixed with /auth
    r"/auth/*": {
        "origins": ["https://rp-gen.vercel.app", "http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
    # If you have other blueprints or routes that don't start with /api or /auth
    # you might need a general rule or specific ones for them.
    # r"/*": { ... } might be too broad if you want fine-grained control
})
# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', 'https://rp-gen.vercel.app')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# Configuração do Swagger
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # documenta todas as rotas
            "model_filter": lambda tag: True
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "RPGen API",
        "description": "Documentação da API do RPGen com Swagger",
        "version": "1.0.0"
    },
    "basePath": "/",  # prefixo base
}

Swagger(app, config=swagger_config, template=swagger_template)

logging.basicConfig(level=logging.INFO)

text_generator = Text_Gen()
image_generator = Image_Gen()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(character_bp, url_prefix='/my-characters')

@app.route('/')
def home():
    return {'message': 'API está online!'}

@app.route('/api/gerar-texto', methods=['POST'])
def gerar_texto():
    """
    Gera um texto com base no prompt fornecido.
    ---
    tags:
      - Geração de Texto
    parameters:
      - in: body
        name: prompt
        required: true
        schema:
          type: object
          properties:
            prompt:
              type: string
              example: "Um guerreiro encontra um dragão em uma caverna"
    responses:
      200:
        description: Texto gerado com sucesso
    """
    data = request.get_json()
    prompt = data.get('prompt')
    texto_gerado = text_generator.generate_text(prompt)
    return jsonify({'generated_text': texto_gerado})

@app.route('/api/gerar-imagem', methods=['POST'])
def gerar_imagem():
    """
    Gera uma imagem com base no prompt fornecido.
    ---
    tags:
      - Geração de Imagem
    parameters:
      - in: body
        name: prompt
        required: true
        schema:
          type: object
          properties:
            prompt:
              type: string
              example: "Um mago lançando um feitiço"
    responses:
      200:
        description: Imagem gerada com sucesso
    """
    data = request.get_json()
    prompt = data.get('prompt')
    imagem_base64 = image_generator.generate_image(prompt)
    return jsonify({'imagem_base64': imagem_base64})

if __name__ == '__main__':
    app.run(debug=True)
