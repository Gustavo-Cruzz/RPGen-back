# utils/token_required.py

from functools import wraps
from flask import request, jsonify
import jwt

SECRET_KEY = "sua_chave_secreta"  # substitua pela sua chave real

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token é necessário!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data['user_id']
        except Exception as e:
            return jsonify({'message': f'Token inválido: {str(e)}'}), 401

        return f(current_user, *args, **kwargs)
    return decorated
