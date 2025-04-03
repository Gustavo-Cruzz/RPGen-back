import requests

class Text_Gen():
    def gerar_texto_com_gemini(self, prompt, api_key):
        """
        Envia um prompt para a API do Gemini e retorna o texto gerado.

        Args:
            prompt (str): O prompt de texto a ser enviado para o modelo.
            api_key (str): Sua chave de API do Gemini.

        Returns:
            str: O texto gerado pelo modelo, ou None em caso de erro.
        """

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
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
            response.raise_for_status()  # Lança uma exceção para status de erro (4xx ou 5xx)
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
        except (KeyError, IndexError, TypeError) as e:
            print(f"Erro ao processar a resposta: {e}")
            return None