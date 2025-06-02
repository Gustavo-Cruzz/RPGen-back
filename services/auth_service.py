
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
        'name': data['username'],
        'email': data['email'],
        'password': hashed_password
    }

    result = user_collection.insert_one(user)
    return str(result.inserted_id), None


def authenticate_user(data):
    user = user_collection.find_one({'email': data['email']})
    if not user:
        return None, 'Credenciais inválidas.'

    if check_password_hash(user['password'], data['password']):
        token = jwt.encode({
            'user_id': str(user['_id']),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, os.getenv('SECRET_KEY'), algorithm="HS256")

        return token, None

    return None, 'Credenciais inválidas.'


def get_user_by_id(user_id):
    user = user_collection.find_one({'_id': ObjectId(user_id)}, {'password': 0})
    if user:
        user['_id'] = str(user['_id'])
    return user
