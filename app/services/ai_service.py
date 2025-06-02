from google import genai
from dotenv import load_dotenv
import os
from ..utils.logger import logger

load_dotenv()

class AIService:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.error("GEMINI_API_KEY not found in environment variables")
            raise ValueError("GEMINI_API_KEY is required")

    def generate_text(self, prompt: str) -> str:
        """Generate text using Gemini API"""
        try:
            client = genai.Client(api_key=self.api_key)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt]
            )
            if response.text:
                logger.info(f"Text generated successfully for prompt: {prompt[:50]}...")
                return response.text
            return None
        except Exception as e:
            logger.error(f"Error during text generation: {str(e)}")
            raise

    def generate_image(self, prompt: str) -> str:
        """Generate image using Gemini API"""
        try:
            client = genai.Client(api_key=self.api_key)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt]
            )
            # Assuming the response contains image data - adjust based on actual API response
            if hasattr(response, 'image_data'):
                logger.info(f"Image generated successfully for prompt: {prompt[:50]}...")
                return response.image_data
            return None
        except Exception as e:
            logger.error(f"Error during image generation: {str(e)}")
            raise