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
        "description": data.get("description", ""),
        "owner_id": ObjectId(owner_id),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    return character_collection.insert_one(character)
