import replicate
import os

system_prompt = "You are an English to Malay translator. Translate the to Malay. Keep the context as in the original text."

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Get the input from the file
with open("out/rmk12.txt", "r") as f:
    input_text = f.read()

# Run the Llama model
for item in replicate.run(
    "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
    input={"prompt": f"{system_prompt} {input_text}"},
):
    print(item, end="")


