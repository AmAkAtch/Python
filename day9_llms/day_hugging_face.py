from huggingface_hub import InferenceClient

client = InferenceClient(provider="hf-inference")


response = client.chat.completions.create(
    model="HuggingFaceTB/SmolLM3-3B",
    messages=[
        {"role": "user", "content": "What is the weather in New York? write only in one sentence"}
    ]
)

print(response.choices[0].message)