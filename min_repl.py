import replicate
import os

# Get the current system prompt
system_prompt = "You are a secretary to a departmental meeting. Your task is to write a concise meeting notes that highlighting important discussions, facts and decision. Tabulate facts and figure for references."

REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")

# Get the input files from the input-dir
input_files = os.listdir("/home/abi/minutes/shred")

# Loop over the input files
for input_file in input_files:
    # Get the input text from the file
    with open(f"/home/abi/minutes/shred/{input_file}", "r") as f:
        input_text = f.read()

    # Run the Llama model
    for item in replicate.run(
        "meta/llama-2-70b-chat:2c1608e18606fad2812020dc541930f2d0495ce32eee50074220b87300bc16e1",
        input={"prompt": f"{system_prompt} {input_text}"},
    ):
        print(item, end="")

