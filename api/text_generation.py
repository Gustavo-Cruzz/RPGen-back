from google import genai
from dotenv import load_dotenv
import os

class Text_Gen():
    def generate_text(self, prompt):
        """
        Envia um prompt para a API do Gemini e retorna o texto gerado.

        Args:
            prompt (str): O prompt de texto a ser enviado para o modelo.

        Returns:
            str: O texto gerado pelo modelo, ou None em caso de erro.
        """
        load_dotenv()
        try:
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt]
            )

            if response.text:
                return response.text
            else:
                return None
        except Exception as e:
            print(f"Error during text generation: {e}")
            return None