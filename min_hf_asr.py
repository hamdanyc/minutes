import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()

# Read authorization token from environment variable
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}",
            "Content-Type": "application/json"
}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    encoded_data = base64.b64encode(data).decode('utf-8')
    payload = {"input": encoded_data, "parameters": {"return_timestamp": True}}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query("/home/abi/nfs/work_space/minutes/audio/mmmr-post-2-01.mp3")
print(output)