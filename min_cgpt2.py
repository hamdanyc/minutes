

import os
import sys
import openai

# Get the OpenAI API key from the environment
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Check if the API key is set
if openai.api_key is None:
    print("OpenAI API key not found. Make sure to set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

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
        prompt = f"List 3 to 5 main points with a brief description from the text.: {text}"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=355,
            temperature=0
        )
        rs = response.choices[0].text.strip()
        print(rs)

        print("Ringkasan:")

        # Translate the response to Malay
        prompt = f"Suggest title for each points. Translate to Malay.: {rs}"
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=355,
            temperature=0
        )
        my = response.choices[0].text.strip()
        print(my)

    print("")

