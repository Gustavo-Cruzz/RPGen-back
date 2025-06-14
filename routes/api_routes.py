# routes/api_routes.py

from flask import Blueprint, request, jsonify
from api.text_generation import Text_Gen
from api.image_generation import Image_Gen

api_bp = Blueprint('api_bp', __name__)

text_generator = Text_Gen()
image_generator = Image_Gen()

@api_bp.route('/gerar-texto', methods=['POST'])
def gerar_texto():
    """
    Generates text based on the provided prompt.
    ---
    tags:
      - API
    parameters:
      - in: body
        name: prompt
        required: true
        schema:
          type: object
          properties:
            prompt:
              type: string
              example: "A warrior finds a dragon in a cave"
    responses:
      200:
        description: Text generated successfully
    """
    data = request.get_json()
    prompt = data.get('prompt')
    texto_gerado = text_generator.generate_text(prompt)
    return jsonify({'generated_text': texto_gerado})

@api_bp.route('/gerar-imagem', methods=['POST'])
def gerar_imagem():
    """
    Generates an image based on the provided prompt.
    ---
    tags:
      - API
    parameters:
      - in: body
        name: prompt
        required: true
        schema:
          type: object
          properties:
            prompt:
              type: string
              example: "A wizard casting a spell"
    responses:
      200:
        description: Image generated successfully
    """
    data = request.get_json()
    prompt = data.get('prompt')
    imagem_base64 = image_generator.generate_image(prompt)
    return jsonify({'imagem_base64': imagem_base64})