# min_repl.py
# Chat completion from replicate
# input: shred/
# output: res/

from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
import os

context = ""
# Get the current system prompt
messages = [
    (
        "system", "You are a secretary to a departmental meeting. Your task is to write a discussion\
             notes that highlighting important discussions, facts and decision.\
             Tabulate facts and figure for references.",
    ),
    ("human", "{context}"),
]

# Create Ollama language model - Gemma 2
local_llm = 'gemma2:2b'

llm = ChatOllama(model=local_llm,
                 keep_alive="3h", 
                 max_tokens=1500,  
                 temperature=0.3)

# Get the input files from the input-dir
input_files = os.listdir("shred")

# Remove existing files from the output directory
output_directory = "res_ollama"
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    os.remove(file_path)

# Loop over the input files
for input_file in input_files:
    # Get the input text from the file
    with open(f"shred/{input_file}", "r") as f:
        input_text = f.read()

    # Save the response text to output_directory
    with open(f"{output_directory}/{input_file}", "w", encoding="utf-8") as file:
        # Run the Llama model
        ai_msg = llm.invoke([(
            "system", "You are a secretary to a departmental meeting. Your task is to write a discussion\
                notes that highlighting important discussions, facts and decision.\
                Tabulate facts and figure where possible.",
                ),
                ("human", input_text),
            ])
        file.write(ai_msg.content)
