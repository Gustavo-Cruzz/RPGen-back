from flask import Flask, request, jsonify
from api.text_generation import Text_Gen
from api.image_generation import Image_Gen
from dotenv import load_dotenv
import os

app = Flask(__name__)

text_generator = Text_Gen()
image_generator = Image_Gen()

load_dotenv()
api_key = os.getenv("API_KEY")

@app.route('/api/gerar-texto', methods=['POST'])
def gerar_texto():
    try:
        data = request.get_json()
        prompt = data['prompt']

        texto_gerado = text_generator.generate_text(prompt, api_key)

        if texto_gerado:
            return jsonify({'texto_gerado': texto_gerado})
        else:
            return jsonify({'erro': 'Falha ao gerar o texto.'}), 500
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/gerar-imagem', methods=['POST'])
def gerar_imagem():
    try:
        data = request.get_json()
        prompt = data['prompt']

        imagem_base64 = image_generator.generate_image(prompt, api_key)

        if imagem_base64:
            return jsonify({'imagem_base64': imagem_base64})
        else:
            return jsonify({'erro': 'Falha ao gerar a imagem.'}), 500
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
