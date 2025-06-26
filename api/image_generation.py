from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import io
import base64


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
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            response = client.models.generate_content(
                model="imagen-4.0-generate-preview-06-06",
                contents=[prompt],
                generation_config=types.GenerationConfig( 
                    candidate_count=1, 
                )
            )

            # Check if the response contains candidates (generated images)
            if response.candidates:
                if hasattr(response.candidates[0], 'image') and response.candidates[0].image:                    

                    # Assuming response.candidates[0].image is a PIL Image object
                    img_pil = response.candidates[0].image
                    
                    # Save image to a bytes buffer in PNG format 
                    byte_arr = io.BytesIO()
                    img_pil.save(byte_arr, format='PNG')
                    encoded_img = base64.b64encode(byte_arr.getvalue()).decode('ascii')

                    # Return as a data URI
                    return f"data:image/png;base64,{encoded_img}"
                else:
                    print("Resposta da API não contém dados de imagem válidos.")
                    return None
            else:
                print("A API não retornou candidatos de imagem para o prompt fornecido.")
                return None

        except Exception as e: 
            print(f"Erro inesperado durante a geração da imagem: {e}")
            return None