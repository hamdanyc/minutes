# min_repl.py
# Chat completion from replicate
# input: /home/abi/minutes/shred
# output: /home/abi/res/

import replicate
import os

# Get the current system prompt
<<<<<<< HEAD
system_prompt = "You are a secretary to a departmental meeting. Your task is to write a concise meeting notes that highlighting important discussions, facts,  decision and action to be done. The minutes should include the title, brief discussion, action needed and person(s) responsibles for the action. Write discussion and action items within a paragraph. End with a tabulated facts and figure for references where necessary "
=======
system_prompt = "You are a secretary to a departmental meeting. Your task is to write a concise meeting notes that highlighting important discussions, facts and decision. Tabulate facts and figure for references."
>>>>>>> 626d4ef40581f9da95d9bb8557df68a1f67a0808

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
            "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
<<<<<<< HEAD
            input={"prompt": f"{system_prompt} {input_text}",
                    "temperature": 0.2,
                    "max_new_token":900}
=======
            input={"prompt": f"{system_prompt} {input_text}"},
>>>>>>> 626d4ef40581f9da95d9bb8557df68a1f67a0808
        ):
            # print(item, end="")
            file.write(item)
