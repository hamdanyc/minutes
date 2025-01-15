import requests
import os
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
    response = requests.post(API_URL, headers=headers, data=data, params={"return_timestamp": True})
    text = response.json().get("text")
    return text

output = query("/home/abi/nfs/work_space/minutes/audio/mmmr-post-2-01.mp3")
print(output)