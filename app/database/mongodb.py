from motor.motor_asyncio import AsyncIOMotorClient
from ..config import settings

client = AsyncIOMotorClient(settings.MONGODB_ATLAS_URI)
db = client[settings.MONGODB_DATABASE_NAME]

def get_db():
    return db