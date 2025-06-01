from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

MONGO_URI = os.getenv("MONGODB_ATLAS_URI")


try:
    client = MongoClient(MONGO_URI)
    db = client.get_database()
    logging.info("✅ Conectado ao MongoDB com sucesso!")
except Exception as e:
    logging.error(f"❌ Erro ao conectar no MongoDB: {e}")
    raise e
