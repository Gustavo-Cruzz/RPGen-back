from flask import Flask, request, jsonify
from api.text_generation import Text_Gen
from api.image_generation import Image_Gen
from flask_cors import CORS
import os

app = Flask(__name__)

text_generator = Text_Gen()
image_generator = Image_Gen()
frontend_url = os.environ.get("VERCEL_FRONTEND_URL")

if frontend_url:
    CORS(app, origins=[frontend_url])
else:
    print("Warning: VERCEL_FRONTEND_URL environment variable not set. CORS might be open.")
    CORS(app) 

@app.route('/api/gerar-texto', methods=['POST'])
def gerar_texto(prompt):
    try:
        data = request.get_json()
        prompt = data['prompt']

        texto_gerado = text_generator.generate_text(prompt)

        if texto_gerado:
            return jsonify({'Generated Text': texto_gerado})
        else:
            return jsonify({'error': 'Error during text generation'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/gerar-imagem', methods=['POST'])
def gerar_imagem(prompt):
    try:
        data = request.get_json()
        prompt = data['prompt']

        imagem_base64 = image_generator.generate_image(prompt)

        if imagem_base64:
            return jsonify({'imagem_base64': imagem_base64})
        else:
            return jsonify({'error': 'Error during image generation'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
