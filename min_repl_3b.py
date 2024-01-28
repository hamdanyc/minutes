# min_repl.py
# Chat completion from replicate
# input: /workspace/minutes/shred
# output: /workspace/res/

import replicate
import os

# Get the current system prompt
system_prompt = "You are a secretary to a departmental meeting. Your task is to write a discussion notes that highlighting important discussions, facts and decision. Tabulate facts and figure for references."

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
            "meta/llama-2-7b-chat:13c3cdee13ee059ab779f0291d29054dab00a47dad8261375654de5540165fb0",
            input={
                   "debug": False,
                    "top_k": -1,
                    "top_p": 1,
                    "prompt": f"{system_prompt} {input_text}",
                    "max_new_tokens": 800,
                    "temperature": 0.3,
                    "min_new_tokens": -1,
                    "repetition_penalty": 1
                   }
        ):

            # print(item, end="")
            file.write(item)
