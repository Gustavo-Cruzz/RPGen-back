
from models.user_model import user_collection
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
from bson import ObjectId


def register_user(data):
    if user_collection.find_one({'email': data['email']}):
        return None, 'Usuário já existe.'

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    user = {
        'username': data['username'],
        'email': data['email'],
        'password': hashed_password
    }

    result = user_collection.insert_one(user)
    return str(result.inserted_id), None


def authenticate_user(data):
    user = user_collection.find_one({'email': data['email']})
    if not user:
        return None, None, 'Credenciais inválidas.' # Return token, user, error

    if check_password_hash(user['password'], data['password']):
        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, os.getenv('SECRET_KEY'), algorithm="HS256")

        # Convert ObjectId to string for JSON serialization
        user_data_to_return = {
            "username": user.get('username') or user.get('name'), # Handle both 'username' or 'name'
            "email": user['email']
        }
        if '_id' in user_data_to_return:
             del user_data_to_return['_id'] 

        # Now return token, user_data_to_return, and None for error
        return token, user_data_to_return, None

    return None, None, 'Erro de senha.' # Return token, user, error


def get_user_by_id(user_id):
    user = user_collection.find_one({'_id': ObjectId(user_id)}, {'password': 0})
    if user:
        user['_id'] = str(user['_id'])
    return user
