from database.mongo import db
from bson import ObjectId
from datetime import datetime

character_collection = db['characters']

def create_character(data, owner_id):
    character = {
        "name": data["name"],
        "race": data["race"],
        "class": data["class"],
        "level": data["level"], 
        "gender": data.get("gender"), 
        "age": data.get("age"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "eyeColor": data.get("eyeColor"),
        "skinColor": data.get("skinColor"),
        "hairColor": data.get("hairColor"),
        "description": data.get("description", ""),
        "allies": data.get("allies", ""), 
        "notes": data.get("notes", ""),
        "traits": data.get("traits", ""),
        "equipment": data.get("equipment", ""),
        "history": data.get("history", ""),
        "owner_id": ObjectId(owner_id),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    return character_collection.insert_one(character)