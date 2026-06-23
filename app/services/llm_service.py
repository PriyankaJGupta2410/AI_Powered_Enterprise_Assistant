import requests

from app.constants.constants import (
    OLLAMA_URL,
    MODEL_NAME
)


class LLMService:

    @staticmethod
    def generate(prompt):

        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        return response.json()["response"]