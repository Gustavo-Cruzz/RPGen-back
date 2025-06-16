import os
import logging
from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from dotenv import load_dotenv

# Import configurations
from config.swagger import swagger_config, swagger_template

def create_app():
    """
    Application Factory: Creates and configures the Flask application.
    """
    load_dotenv()

    app = Flask(__name__)

    # Configure Logging
    logging.basicConfig(level=logging.INFO)

    # Configure CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": ["https://rp-gen.vercel.app", "http://localhost:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        },
        r"/auth/*": {
            "origins": ["https://rp-gen.vercel.app", "http://localhost:3000"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        },
        r"/my-characters/*": { # Add this for your character routes
            "origins": ["https://rp-gen.vercel.app", "http://localhost:3000"],
            "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })

    # Initialize Swagger
    Swagger(app, config=swagger_config, template=swagger_template)

    # Import and register blueprints
    from routes.auth_routes import auth_bp
    from routes.character_routes import character_bp
    from routes.api_routes import api_bp # New API blueprint

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(character_bp, url_prefix='/my-characters')
    app.register_blueprint(api_bp, url_prefix='/api') # Register the new blueprint

    # A simple health-check route
    @app.route('/')
    def home():
        return {'message': 'API está online!'}

    return app

app = create_app()
