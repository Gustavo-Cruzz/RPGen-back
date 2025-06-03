from flask import jsonify, request
from services.character_service import (
    create_character, get_characters, get_character_by_id,
    update_character, delete_character
)

def create(current_user):
    data = request.get_json()
    character_id = create_character(current_user, data)
    return jsonify({'message': 'Personagem criado!', 'character_id': character_id}), 201

def read_all(current_user):
    """
    Lista todos os personagens do usuário autenticado.
    ---
    tags:
      - Personagens
    security:
      - Bearer: []
    responses:
      200:
        description: Lista de personagens
    """
    characters = get_characters(current_user)
    return jsonify(characters)

def read_one(current_user, character_id):
    character = get_character_by_id(current_user, character_id)
    if character:
        return jsonify(character)
    return jsonify({'error': 'Personagem não encontrado'}), 404

def update(current_user, character_id):
    """
    Atualiza completamente um personagem pelo ID.
    ---
    tags:
      - Personagens
    parameters:
      - in: path
        name: character_id
        required: true
        type: string
      - in: body
        name: dados
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            level:
              type: integer
    responses:
      200:
        description: Personagem atualizado com sucesso
      404:
        description: Personagem não encontrado
    """
    data = request.get_json()
    if update_character(current_user, character_id, data):
        return jsonify({'message': 'Personagem atualizado!'})
    return jsonify({'error': 'Personagem não encontrado'}), 404

def delete(current_user, character_id):
    if delete_character(current_user, character_id):
        return jsonify({'message': 'Personagem deletado!'})
    return jsonify({'error': 'Personagem não encontrado'}), 404
