# min_repl_rct.py
# Chat completion from replicate
# input: /workspace/minutes/shred
# output: /workspace/res/

import replicate
import os

# Get the current system prompt
system_prompt = "You are a secretary to a seminar. Your task is to write a summary of the presentation that highlighting important discussions, and facts. The summary should include the presentor name, title and discussion."

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

# Get the input files from the input-dir
input_files = os.listdir("/workspace/minutes/shred")

# Remove existing files from the output directory
output_directory = "/workspace/minutes/res"
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    os.remove(file_path)

# Loop over the input files
for input_file in input_files:
    # Get the input text from the file
    with open(f"/workspace/minutes/shred/{input_file}", "r") as f:
        input_text = f.read()

    # Save the response text to output_directory
    with open(f"/workspace/minutes/res/{input_file}", "w", encoding="utf-8") as file:
        # Run the Llama model
        for item in replicate.run(
            "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
            input={"prompt": f"{system_prompt} {input_text}",
                    "temperature": 0.2,
                    "max_new_token":900}
        ):
            # print(item, end="")
            file.write(item)
