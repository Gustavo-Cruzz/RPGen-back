from flask import Blueprint, jsonify, request
from services.auth_service import (
    register_user,
    authenticate_user,
    get_user_by_id
)
from utils.token_required import token_required  # certifique-se de que esse arquivo existe e está correto

auth_bp = Blueprint('auth', __name__)

# 🔐 Rota de Registro
def register():
    data = request.get_json()

    # Validação dos dados recebidos
    required_fields = ['name', 'email', 'password']
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


# 🔑 Rota de Login
def login():
    data = request.get_json()

    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são obrigatórios.'}), 400

    token, error = authenticate_user(data)
    if error:
        return jsonify({'error': error}), 401

    return jsonify({'token': token}), 200


# 👤 Rota de perfil do usuário logado
@auth_bp.route('/me', methods=['GET'])
@token_required
def me(current_user, *args, **kwargs):
    user = get_user_by_id(current_user)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'Usuário não encontrado'}), 404