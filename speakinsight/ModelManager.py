from llama_cpp import Llama
from openai.types.chat import ChatCompletion, ChatCompletionChunk

class ModelManager():
    def __init__(self):
        model = "Qwen/Qwen2-0.5B-Instruct-GGUF"
        self.query_model = self.create_model_instance()

    def create_model_instance(self, model="Qwen/Qwen2-7B-Instruct-GGUF"):
        return Llama.from_pretrained(
            repo_id=model,
            filename="*q8_0.gguf",
            verbose=False,
            n_ctx=4096,
            n_threads=8,
            n_gpu_layers=33
        )

    def invoke(self, prompt):
        return self.query_model.create_chat_completion(prompt, max_tokens=None, response_format={"type": "json_object"})["choices"][0]["message"]["content"].strip()

    def stream(self, prompt):
        return self.query_model.create_chat_completion(
            prompt,
            max_tokens=None,
            response_format={"type": "json_object"},
            stream=True,
            )