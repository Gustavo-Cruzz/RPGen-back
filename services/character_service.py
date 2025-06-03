from models.character_model import character_collection
from bson import ObjectId

def create_character(user_id, data):
    character = {
        'user_id': user_id,
        'name': data['name'],
        'class': data.get('class', ''),
        'level': data.get('level', 1),
        'description': data.get('description', '')
    }
    result = character_collection.insert_one(character)
    return str(result.inserted_id)

def get_characters(user_id):
    characters = list(character_collection.find({'user_id': user_id}))
    for char in characters:
        char['_id'] = str(char['_id'])
    return characters

def get_character_by_id(user_id, character_id):
    char = character_collection.find_one({'_id': ObjectId(character_id), 'user_id': user_id})
    if char:
        char['_id'] = str(char['_id'])
    return char

def update_character(user_id, character_id, data):
    result = character_collection.update_one(
        {'_id': ObjectId(character_id), 'user_id': user_id},
        {'$set': data}
    )
    return result.modified_count > 0

def delete_character(user_id, character_id):
    result = character_collection.delete_one({'_id': ObjectId(character_id), 'user_id': user_id})
    return result.deleted_count > 0
