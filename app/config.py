from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    MONGODB_ATLAS_URI: str
    MONGODB_DATABASE_NAME: str = "rpgen"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    CORS_ORIGINS: List[str] = ["https://rp-gen.vercel.app"]
    
    class Config:
        env_file = ".env"

settings = Settings()
