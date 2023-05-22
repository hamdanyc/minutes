#!/bin/awk
BEGIN {
  max_tokens = 256;
  FS="\n";
}

{
  prompt = $0;
}

{
   for (line_no=1; line_no<=NF; line_no++) {
      prompt=prompt $line_no
   }
}

END {
   #curl=$(curl)
   curl "https://api.openai.com/v1/completions" -X POST
	-H "Content-Type: application/json"
	-H "Authorization: Bearer $OPENAI_API_KEY"
	# -d '{\"prompt\": \"" $prompt "\", \"max_tokens\": "$max_tokens\"}'"
	-d '{
	    "model": "text-davinci-003",
	    "prompt": "'"Summarise: $prompt"'",
	    "max_tokens": $max_tokens,
	    "temperature": 0
	 }
   echo $rs
   echo $(echo $result)
   echo $(echo $result | jq -r '.choices[0].text')
   }
