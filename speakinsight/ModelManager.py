from llama_cpp import Llama

class ModelManager():
    def __init__(self):
        self.query_model = self.create_model_instance()

    def create_model_instance(self):
        return Llama.from_pretrained(
            repo_id="Qwen/Qwen2-0.5B-Instruct-GGUF",
            filename="*q8_0.gguf",
            verbose=False,
        )

    def invoke(self, prompt):
        return self.query_model.create_chat_completion(prompt, max_tokens=None, response_format={"type": "json_object",})["choices"][0]["message"]["content"].strip()
