from llama_cpp import Llama
from openai.types.chat import ChatCompletion, ChatCompletionChunk
import os
from langchain_groq import ChatGroq


class LlamaModelManager():
    def __init__(self):
        model = "Qwen/Qwen2-7B-Instruct-GGUF"
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
    
GROQ_API_KEYS = [os.environ.get("GROQ_API_KEY1"), os.environ.get("GROQ_API_KEY2")]

class GroqModelManager():
    def __init__(self):
        self.query_models = [self.create_model_instance(GROQ_API_KEYS[0], json=True), self.create_model_instance(GROQ_API_KEYS[1], json=True)]
        self.chatbot_models = [self.create_model_instance(GROQ_API_KEYS[0]), self.create_model_instance(GROQ_API_KEYS[1])]
        self.query_turn = 0
        self.chatbot_turn = 0

    def create_model_instance(self, groq_api_key, temperature=0, model="llama3-70b-8192", json=False, model_kwargs={"top_p":0.3}):
        if json:
            model_kwargs = {
                "top_p":0.3,
                "response_format":{"type":"json_object"}
                }
        return ChatGroq(
            temperature=temperature,
            model_name=model,
            groq_api_key=str(groq_api_key),
            model_kwargs=model_kwargs
            )

    def invoke(self, prompt):
        # Alternatively use the two query models
        model = self.query_models[self.query_turn]
        self.query_turn = (self.query_turn + 1) % 2
        return model.invoke(prompt)

    def generate_tokens(self, question):
        model = self.chatbot_models[self.chatbot_turn]
        self.chatbot_turn = (self.chatbot_turn + 1) % 2
        for chunks in model.stream(question):
            yield chunks.content