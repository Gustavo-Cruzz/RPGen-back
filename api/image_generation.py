import requests
import json
from dotenv import load_dotenv
import os

class Image_Gen():
    def gerar_imagem_com_gemini(self, prompt, api_key):
        """
        Envia um prompt para a API do Gemini e retorna a URL da imagem gerada.

        Args:
            prompt (str): O prompt de texto para a geração da imagem.
            api_key (str): Sua chave de API do Gemini.

        Returns:
            str: A URL da imagem gerada, ou None em caso de erro.
        """

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent" 
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": api_key
        }
        data = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['inlineData']['data']
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        except (KeyError, IndexError, TypeError) as e:
            print(f"Erro ao processar a resposta: {e}")
            return None