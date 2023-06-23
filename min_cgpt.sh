#!/bin/bash

file_list=$(ls /home/abi/Documents/minit_mesyuarat_wp/min_out/chunk/*.txt)

for files in $file_list
do
    hd=$(head -1 $files)
    echo "$hd"

    # get chatgpt to summarise text
    TEXT=$(cat $files | tr '\n' ' ') && \
    RS=$(curl -s https://api.openai.com/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "text-davinci-003",
        "prompt": "'"List 3 to 5 main points with a brief description from the text.: $TEXT"'",
        "max_tokens": 355,
        "temperature": 0
      }' | jq -r '.choices[].text' | tr -d '\"' | tr ']' '\n[')
    echo $RS
    echo "Perbincangan:"

    # Translate text to Malay
    sleep 3
    MY=$(echo $RS | tr -d '\"' | tr ']' '\n[') && \
    curl -s https://api.openai.com/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "text-davinci-003",
        "prompt": "'"Suggest title for each points. Translate to Malay.: $MY"'",
        "max_tokens": 355,
        "temperature": 0
      }' | jq -r '.choices[].text' | tr -d '\"' | tr ']' '\n['
    echo ""
done
