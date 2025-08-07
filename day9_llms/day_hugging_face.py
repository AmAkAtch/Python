import requests
import json
from dotenv import load_dotenv
import os


#loading the environment variables
load_dotenv()
API_KEY=os.getenv("HUGGING_FACE_API_KEY")

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization":f'Bearer {API_KEY}',
    "Content-Type":"application/json"
}

#call the huggingface with api and prompt
def call_huggingface(prompt:str)->str:
    """this function takes in prompt as a string and will call the hugging face url with authorization header and get a response for the prompt"""

    payload = {
        "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "model": "meta-llama/Llama-3.1-8B-Instruct:novita"
    }

    response = requests.post(API_URL,headers=HEADERS,json=payload)
    if response.status_code != 200:
        raise RuntimeError(f"Error {response.status_code} {response.reason}")
    
    result = response.json()
    generated_text = result["choices"][0]["message"]
    return generated_text

output = call_huggingface("Once upon a time, in a land far away")
print(output)

