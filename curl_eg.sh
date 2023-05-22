#!/bin/bash
file_list=$(ls ../min_out/outline/*.txt)

for files in $file_list
do
    echo cat $files # > Documents/rmd_ver/$files
    # article_outline(files)
done

function article_outline(fi) {
    TEXT=$(cat fi | tr '\n' ' ') && \
    curl -s https://api.openai.com/v1/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $OPENAI_API_KEY" \
      -d '{
        "model": "text-davinci-003",
        "prompt": "'"List 3 to 5 main points: $TEXT"'",
        "max_tokens": 155,
        "temperature": 0
      }' | jq '.choices[].text' | tr -d '\"'
}

