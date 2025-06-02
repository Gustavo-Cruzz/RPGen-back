from flask import Blueprint, jsonify, request
from services.auth_service import (
    register_user,
    authenticate_user,
    get_user_by_id
)
from utils.token_required import token_required  # certifique-se de que esse arquivo existe e está correto

auth_bp = Blueprint('auth', __name__)

# 🔐 Rota de Registro
@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Registro de novo usuário.
    ---
    tags:
      - Autenticação
    parameters:
      - in: body
        name: corpo
        required: true
        schema:
          type: object
          properties:
            username: # Changed from 'name' to 'username' based on your Swagger example
              type: string
              example: "yasmin"
            email:
              type: string
              example: "yasmin@example.com"
            password:
              type: string
              example: "senha123"
    responses:
      201:
        description: Usuário criado com sucesso
    """
    data = request.get_json()

    # Validação dos dados recebidos
    required_fields = ['username', 'email', 'password'] # **Changed 'name' to 'username' here**
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Campo obrigatório ausente: {field}'}), 400

    user_id, error = register_user(data)
    if error:
        return jsonify({'error': error}), 400

    return jsonify({
        'message': 'Usuário registrado com sucesso!',
        'user_id': user_id
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são obrigatórios.'}), 400

    # Catch all three return values from authenticate_user
    token, user_info, error = authenticate_user(data)
    if error:
        # Use a consistent generic message for security
        return jsonify({'error': 'Credenciais inválidas.'}), 401

    return jsonify({
        'message': 'Usuário logado com sucesso', # Added message field
        'token': token,
        'user': user_info # Use the user_info returned from authenticate_user
    }), 200

# 👤 Rota de perfil do usuário logado
@auth_bp.route('/me', methods=['GET'])
@token_required
def me(current_user, *args, **kwargs):
    user = get_user_by_id(current_user)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'Usuário não encontrado'}), 404