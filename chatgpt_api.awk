#!/usr/bin/awk -f

BEGIN {
    # Set the OpenAI API endpoint and access key
    endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
    access_key = OPENAI_API_KEY

    # Set the text content
    text = "Explain to 5 year old about black hole"

    # Set the request payload
    payload = "{\"prompt\": " text "\",\"max_tokens\":50}"

    # Make the API call and get the response
    command = "curl -s -X POST -H \"Content-Type: application/json\" -H \"Authorization: Bearer " access_key "\" -d '" payload "' " endpoint
    command | getline response
    close(command)

    # Parse the response and extract the summary
    split(response, response_arr, "\"text\":")
    split(response_arr[2], summary_arr, "\"")
    summary = summary_arr[2]

    # Display the summary
    print "Summary:"
    print response
}
