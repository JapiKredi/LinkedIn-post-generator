from llama_cpp import Llama
from typing import Dict
from src.config import MODEL_PATH, MODEL_CONFIG


class LlamaModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LlamaModel, cls).__new__(cls)
            cls._instance.model = Llama(
                model_path=MODEL_PATH,
                n_ctx=MODEL_CONFIG["n_ctx"],
                n_threads=MODEL_CONFIG["n_threads"],
            )
        return cls._instance

    def generate_completion(self, prompt: str) -> str:
        """Generate completion using Llama model."""
        try:
            response = self.model.create_completion(
                prompt,
                max_tokens=MODEL_CONFIG["max_tokens"],
                temperature=MODEL_CONFIG["temperature"],
                stop=["###"],
            )
            return response.choices[0].text
        except Exception as e:
            raise Exception(f"Error generating completion: {str(e)}")
