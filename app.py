from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging

from api.text_generation import Text_Gen
from api.image_generation import Image_Gen
from routes.auth_routes import auth_bp
from routes.character_routes import character_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

text_generator = Text_Gen()
image_generator = Image_Gen()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(character_bp, url_prefix='/characters')

@app.route('/')
def home():
    return {'message': 'API está online!'}

@app.route('/api/gerar-texto', methods=['POST'])
def gerar_texto():
    data = request.get_json()
    prompt = data.get('prompt')
    texto_gerado = text_generator.generate_text(prompt)
    return jsonify({'generated_text': texto_gerado})

@app.route('/api/gerar-imagem', methods=['POST'])
def gerar_imagem():
    data = request.get_json()
    prompt = data.get('prompt')
    imagem_base64 = image_generator.generate_image(prompt)
    return jsonify({'imagem_base64': imagem_base64})

if __name__ == '__main__':
    app.run(debug=True)
