import replicate
import os

# Get the audio file path
# audio_file_path = os.path.join("/home/abi/minutes/audio", "02label.mp3")

# Set the API token
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

# Create a client
# client = replicate.Client()

# Transcribe the audio
response = replicate.run(
    "openai/whisper:e39e354773466b955265e969568deb7da217804d8e771ea8c9cd0cef6591f8bc",
    input={
        "audio": open("/home/abi/minutes/audio/aud.mp3"),
        "language": "ms",
        "transcription": "vtt",
    }
)

# Print the transcription
print(response["transcription"])
