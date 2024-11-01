from typing import List, Dict, Union
import requests

from ..model.api.types._model_types import MODELS_TYPE


class ClaudeEngine:
    def __init__(
        self,
        model: MODELS_TYPE = "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
        api_url: str = "http://localhost:11435"
    ):
        self.model = model
        self.api_url = api_url.rstrip('/')

    def __call__(
        self,
        messages: Union[List[Dict[str, str]], str],
        model:MODELS_TYPE = None,
        conversation: str = False,
        websearch: bool = False,
        stream: bool = False
    ) -> str:
        """
        Send a request to the API and get the response.

        Args:
            messages: Either a string prompt or a list of message dictionaries

        Returns:
            String response from the API
        """
        payload = {
                "prompt": messages,
                "model": model if model is not None else self.model,
                "conversation": conversation,
                "stream": stream,
                "websearch": websearch,
            }

        response = requests.post(
            f"{self.api_url}/v1/generate",
            json=payload
        )
        response.raise_for_status()
        return response.json()["message"]["content"]