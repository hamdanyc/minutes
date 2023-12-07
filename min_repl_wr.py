# min_repl.py
# Chat completion from replicate
# input: /home/abi/minutes/shred
# output: /home/abi/res/

import replicate
import os

# Get the current system prompt
system_prompt = "You are a secretary to a departmental meeting. Your task is to write a discussion notes that highlighting important discussions, facts and decision. Tabulate facts and figure for references."

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

# Get the input files from the input-dir
input_files = os.listdir("/home/abi/minutes/shred")

# Remove existing files from the output directory
output_directory = "/home/abi/minutes/res"
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    os.remove(file_path)

# Loop over the input files
for input_file in input_files:
    # Get the input text from the file
    with open(f"/home/abi/minutes/shred/{input_file}", "r") as f:
        input_text = f.read()

    # Save the response text to output_directory
    with open(f"/home/abi/minutes/res/{input_file}", "w", encoding="utf-8") as file:
        # Run the Llama model
        for item in replicate.run(
            "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
            input={"prompt": f"{system_prompt} {input_text}",
                "temperature": 0.75,
                "max_new_tokens": 500,
                "min_new_tokens": -1
                }
        ):
            # print(item, end="")
            file.write(item)
