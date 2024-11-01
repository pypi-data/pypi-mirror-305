# tinyagi/model.py

from llama_cpp import Llama
import os

class ModelLoader:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.load_model()

    def load_model(self):
        model_path = self.config.get('model_path')
        lora_path = self.config.get('lora_path')
        model_params = self.config.get('model_params', {})

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at {model_path}")
        if lora_path and not os.path.exists(lora_path):
            raise FileNotFoundError(f"LoRA adapter file not found at {lora_path}")

        self.model = Llama(
            model_path=model_path,
            lora_base=model_path if lora_path else None,
            lora_path=lora_path,
            **model_params
        )

    def reload_model(self, config):
        self.config = config
        self.load_model()

    def generate(self, prompt, inference_params, stream=False):
        params = {**self.config.get('inference_params', {}), **inference_params}
        return self.model(prompt, stream=stream, **params)

    def embed(self, input_data):
        if isinstance(input_data, list):
            return [self.model.embed(text)['embedding'] for text in input_data]
        else:
            return self.model.embed(input_data)['embedding']
