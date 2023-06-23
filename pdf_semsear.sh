#!/bin/bash

# Set the API key
# export OPENAI_API_KEY="YOUR_API_KEY"

# Set the directory path to your PDF files
PDF_DIRECTORY="/home/abi/Documents/pdf/nimitz"
OUTPUT_FILE="/home/abi/Documents/pdf/nimitz/text/search_results.txt"

# Set the maximum token limit for API calls
MAX_TOKENS=4096

# Set the search query
echo "Query?"
read QUERY

# Function to split text into chunks based on token limit
split_text() {
    local text="$1"
    local max_tokens="$2"
    declare -a chunks

    while [[ ${#text} -gt $max_tokens ]]; do
        local chunk="${text:0:$max_tokens}"
        chunks+=("$chunk")
        text="${text:$max_tokens}"
    done

    if [[ -n $text ]]; then
        chunks+=("$text")
    fi

    printf '%s\n' "${chunks[@]}"
}

# Iterate over each PDF file in the directory
for file in "$PDF_DIRECTORY"/*.pdf; do
    echo "Processing file: $file"

    # Extract text from PDF using a tool like pdftotext
    text=$(pdftotext "$file" -)

    # Split the text into chunks to fit within token limits
    chunks=$(split_text "$text" "$MAX_TOKENS")

    # Iterate over each chunk and process it
    for chunk in "${chunks[@]}"; do
        echo "Processing chunk: $chunk"
        openai tools semantic-search -f "$chunk" --query "$QUERY" --temperature 0.8 >> "$OUTPUT_FILE"
        # response=$(openai tools semantic-search -f "$chunk" --query "$QUERY" --temperature 0.8)
        # echo "$response" >> "$OUTPUT_FILE"
        # Add a separator between search results for each chunk
        echo "-------------------" >> "$OUTPUT_FILE"
    done
done


