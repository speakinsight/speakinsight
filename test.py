from speakinsight.ModelManager import GroqModelManager

model = GroqModelManager()
messages=[
    {
        "role": "user",
        "content": "Explain the importance of fast language models in json format",
    }
]
print(model.invoke(messages).content) # Expected output: "I'm good, how are you?"