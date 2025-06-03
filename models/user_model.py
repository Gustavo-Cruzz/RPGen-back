from database.mongo import db
from datetime import datetime

user_collection = db['users']

def create_user(user_data):
    user = {
        "username": user_data["username"],
        "email": user_data["email"],
        "password": user_data["password"],  # armazenar já com hash
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    return user_collection.insert_one(user)