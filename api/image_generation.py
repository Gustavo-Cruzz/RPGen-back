import requests
from google import genai
from google.genai import types
from dotenv import load_dotenv
import base64
from PIL import Image

client = genai.Client()
class Image_Gen():
    def generate_image(self, prompt):
        """
        Envia um prompt para a API do Gemini e retorna a URL da imagem gerada.

        Args:
            prompt (str): O prompt de texto para a geração da imagem.
            api_key (str): Sua chave de API do Gemini.

        Returns:
            str: A URL da imagem gerada, ou None em caso de erro.
        """

        load_dotenv()
        try:
            response = client.models.generate_content(
                model="imagen-4.0-generate-preview-06-06",
                contents=[prompt],
                config=types.GenerateImagesConfig(
                number_of_images=   ,
                )
            )
            
            return response
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        except (KeyError, IndexError, TypeError) as e:
            print(f"Erro ao processar a resposta: {e}")
            return None