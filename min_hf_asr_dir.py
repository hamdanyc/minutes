import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

# Read authorization token from environment variable
HUGGING_FACE_TOKEN = os.getenv('HUGGING_FACE_TOKEN')

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3-turbo"
headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

def query(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".mp3"):
            with open(os.path.join(input_dir, filename), "rb") as f:
                data = f.read()
            response = requests.post(API_URL, headers=headers, data=data)
            transcription = response.json().get("text")
            
            with open(os.path.join(output_dir, f"{filename}.txt"), "w") as out_file:
                out_file.write(json.dumps(transcription))
                if out_file is not None:
                    print(f"Processed file: {filename}")
                else:
                    print(f"Error processing file: {filename}")

def main():

    input_dir = "/home/app/audio"
    output_dir = "/home/app/script"

    # Remove existing files from the output directory
    for filename in os.listdir(output_dir):
        file_path = os.path.join(output_dir, filename)
        os.remove(file_path)

    query(input_dir, output_dir)

if __name__ == "__main__":
    main()
