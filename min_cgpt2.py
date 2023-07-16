import os
import sys
import openai

# Get the OpenAI API key from the environment
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Check if the API key is set
if openai.api_key is None:
    print("OpenAI API key not found. Make sure to set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

# Define the initial prompt to initiate the conversation
init_prompt = """
You are a secretary in a departmental meeting. Your objective is to write concise, clear and brief meeting notes, highlighting important discussions, facts and decisions while avoiding trivial issues. Present facts and figure in a table. Please take the minutes.
"""
# Generate the conversation with ChatGPT
conversation = [init_prompt]

# Set the directory containing the text files
directory = '/home/abi/minit_mesyuarat_wp/out/chunk'

# Set the directory containing the text files
file_list = os.listdir(directory)

# Iterate over each file in the list
for filename in file_list:
    file_path = os.path.join(directory, filename)

    with open(file_path, 'r') as file:
        # Read the first line of the file
        hd = file.readline().strip()
        print(hd)

        # Get the text from the file and format it
        text = ' '.join(file.read().splitlines())

        # Request summarization from ChatGPT
        prompt = [f"Write minutes from the text. List main points with title. At least 2 paragraph each: {text}"]
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt='\n'.join(conversation + prompt),
            max_tokens=555,
            temperature=0.7
        )
        rs = response.choices[0].text.strip()
        print(rs)
        print("")
        print("Ringkasan Minit:")

        # Translate the response to Malay
        prompt = f"Translate to Malay.: {rs}"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=555,
            temperature=0
        )
        my = response.choices[0].text.strip()
        print(my)

    print("")

