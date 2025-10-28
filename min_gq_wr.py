import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
client = Groq()

def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def write_to_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"Error writing to file: {file_path} - {str(e)}")

def process_file(input_file_path):
    user_content = read_from_file(input_file_path)
    if user_content is not None:
        messages = [
            {
                "role": "system",
                "content": "You are a secretary to a departmental meeting. Your task is to write a discussion\
                    notes that highlighting important discussions, facts and decision as a list\
                    Tabulate facts and figure where necessary.",
            },
            {
                "role": "user",
                "content": user_content
            }
        ]

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=messages, 
            max_tokens=750,
        )

        output = completion.choices[0].message.content
        return output
    else:
        return None

def main():
    input_folder = 'out/'
    output_folder = 'groq/'

    # Remove existing files from the output directory
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            output = process_file(input_file_path)
            if output is not None:
                write_to_file(output_file_path, output)
                print(f"Processed file: {filename}")
            else:
                print(f"Error processing file: {filename}")

if __name__ == "__main__":
    main()