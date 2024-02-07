import replicate
import os

# Get the audio file path or URL
path = os.path.join("/workspace/minutes/audio", "Mesyuarat JMM 15-9-02.mp3")
# audio = open(path,"rb")
audio = "https://docs.google.com/uc?export=open&id=1MmoP-fXZadv5B-mVt3KB1TW5f9gqMpEh"
# Set the API token
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

# Create a client
# client = replicate.Client()

# Transcribe the audio
response = replicate.run(
    "openai/whisper:91ee9c0c3df30478510ff8c8a3a545add1ad0259ad3a9f78fba57fbc05ee64f7",
    input={
        "audio": audio,
        "language": "ms",
        "transcription": "vtt"
    }
)

# Print the transcription
f = open("/workspace/minutes/out/jmm-9-2.txt", "w")
f.write(response["transcription"])
f.close()
