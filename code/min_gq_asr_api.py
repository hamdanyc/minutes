import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
# Read authorization token from environment variable
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

def transcribe_audio(input_dir, output_dir):
    # Clean up the output directory
    for file in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, file))

    # Initialize the Groq client
    client = Groq(
        # This is the default and can be omitted
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is an audio file (assuming only audio files are in the input dir)
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            try:
                # Open the audio file
                with open(os.path.join(input_dir, filename), "rb") as file:
                    # Create a transcription of the audio file
                    transcription = client.audio.transcriptions.create(
                        file=file,  # Required audio file
                        model="whisper-large-v3-turbo",  # Required model to use for transcription
                        language="ms",  # Optional
                        temperature=0.0  # Optional
                    )
                    # Write the transcription to a text file in the output directory
                    with open(os.path.join(output_dir, f"{filename}.txt"), "w") as f:
                        f.write(transcription.text)
                    print(f"Process file {filename} ...done")
            except Exception as e:
                print(f"Error processing file {filename}: {str(e)}")

if __name__ == "__main__":
    input_dir = "/home/app/audio"
    output_dir = "/home/app/script"
    transcribe_audio(input_dir, output_dir)
