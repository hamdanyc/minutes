#!/bin/bash
file_list="$(ls ../min_out/outline/*.txt)"

for files in $file_list
do
    # get chatgpt to summarize text
    TEXT="$(cat "$files")" && \
#    TEXT="${TEXT//$'\n'/\\n}" && \
#    TEXT="${TEXT//$'\r'/\\r}" && \
    curl -s https://api.openai.com/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "text-davinci-003",
        "prompt": "'"List 3 to 5 main points and briefly summarize. Suggest a title for each main point: $TEXT"'",
        "max_tokens": 155,
        "temperature": 0
      }' | jq '.choices[].text' | tr -d '\"'
done
