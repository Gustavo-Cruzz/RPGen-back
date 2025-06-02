from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routes import auth, characters, docs, ai  
from .middlewares.error_handler import ErrorHandler
from .utils.logger import setup_logging

app = FastAPI(
    title="RPG Character Manager API",
    description="API para gerenciamento de personagens de RPG",
    version="1.0.0"
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add error handler middleware
app.add_middleware(ErrorHandler)

# Setup logging
setup_logging()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(characters.router, prefix="/my-characters", tags=["Characters"])
app.include_router(ai.router, prefix="/api", tags=["AI Services"])
app.include_router(docs.router, tags=["Documentation"])