import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Read authorization token from environment variable
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

def query(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp3"):
            with open(os.path.join(input_dir, filename), "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            transcription = response.json()
            with open(os.path.join(output_dir, f"vtt_{filename}.txt"), "w") as out_file:
                out_file.write(json.dumps(transcription))

input_dir = "/home/abi/nfs/work_space/minutes/audio"
output_dir = "/home/abi/nfs/work_space/minutes/script"

query(input_dir, output_dir)