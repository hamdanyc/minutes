#!/usr/bin/awk -f

BEGIN {
    # Set the OpenAI API endpoint and access key
    endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
    access_key = "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"

    # Read the article content from the file
    file_path = "jupiter.txt"

    # Read the contents of the file into the variable 'file'
    article = ""
    while ((getline line < file_path) > 0) {
        article = article line "\n"
    }

    # Close the file
    close(file_path)

    # Print the contents of the file
    print "File contents:"
    print article

    # Set the request payload
    payload = "{\"prompt\":\"Summarize the following article: " article "\",\"max_tokens\":50}"
    # payload = "{\"model\": \"text-davinci-003\",\"prompt\":\"Summarize the following article: " article "\",\"max_tokens\":50""\"}"

    # Make the API call and get the response

    # Parse the response and extract the summary
    split(response, response_arr, "\"text\":")
    split(response_arr[2], summary_arr, "\"")
    summary = summary_arr[2]

    # Display the summary
    print "Summary:"
    print summary
}

#curl https://api.openai.com/v1/completions \
#  -H "Content-Type: application/json" \
#  -H "Authorization: Bearer $OPENAI_API_KEY" \
#  -d '{
#    "model": "text-davinci-003",
#    "prompt": "Say this is a test",
#    "max_tokens": 7,
#    "temperature": 0
#  }'
