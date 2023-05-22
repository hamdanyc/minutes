#!/bin/awk -f

BEGIN {
  FS="\n"
  RS=""
  prompt="Summarize this for a second-grade student:"

}

{
  # use open ai api to summarise text
  text=$0
  cmd = system("curl -X POST \
                    -H \"Authorization: Bearer $OPENAI_API_KEY\" \
                    -H \"Content-Type: application/json\" \
                    --data-binary \"{\\\"prompt\\\": \\\"$text\\\",\\\"max_tokens\\\":64,\\\"model\\\":\\\"text-davinci-003\\\"}\" \
                    https://api.openai.com/v1/completions")
  cmd | getline response
  close(cmd)
}

#curl https://api.openai.com/v1/completions \
#  -H "Content-Type: application/json" \
#  -H "Authorization: Bearer $OPENAI_API_KEY" \
#  -d '{
#  "model": "text-davinci-003",
#  "prompt": "Summarize this for a second-grade student:\n\nJupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.",
#  "temperature": 0.7,
#  "max_tokens": 64,
#  "top_p": 1.0,
#  "frequency_penalty": 0.0,
#  "presence_penalty": 0.0
#}'

#!/bin/awk

#BEGIN {
#  max_tokens=64
#}
#
#{
#  text=$0
#  summary="curl -X POST -H "Content-Type: application/json" -d '{\"text\": \"$text\", \"max_tokens\": $max_tokens}' https://api.openai.com/v1/engines/davinci/completions"
#  print summary
#}
