#!/bin/bash

# Set the OpenAI API endpoint and access key
endpoint="https://api.openai.com/v1/engines/whisper/beta/completions"
access_key=$OPENAI_API_KEY

# Set the path to the audio file
audio_file="../audio/aud_out/min_27_3_23.mp3"
# Encode the audio file to base64
audio_base64=$(base64 -w 0 "$audio_file")

# Set the request payload
payload=$(cat <<EOF
{
  "prompt": "<s>Transcribe the following audio:</s><speak><audio>$audio_base64</audio></speak>",
  "max_tokens": 4096,
  "temperature": 0,
  "top_p": 1.0,
  "n": 1,
  "stop": "</s>"
}
EOF
)

# Make the API call and get the response
# response=$(curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $access_key" -d "$payload" "$endpoint")
response=$(curl https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F model="whisper-1" \
  -F file="@../audio/aud_out/min_11_5_23.wav" \
  -F response_format=vtt)

# Parse the response and extract the transcript
transcript=$(echo "$response" | jq -r '.choices[0].text' | sed -e 's/^<s>//g' -e 's/<\/s>$//g')

# Generate the VTT file
echo "WEBVTT" > output.vtt
echo "" >> output.vtt
echo "1" >> output.vtt
echo "00:00:00.000 --> 00:00:01.000" >> output.vtt
echo "$transcript" >> output.vtt

echo "Transcription saved to output.vtt"
