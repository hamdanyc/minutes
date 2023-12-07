# min_gtran.py
# Translate text to Malay
# input: /home/abi/minutes/res
# output: /home/abi/minutes/out/trans.txt

import os
from googletrans import Translator
from googletrans.constants import LANGUAGES

# Define the input and output language codes
source_language = "en"  # Input text language (e.g., English)
target_language = "ms"  # Output language (e.g., Spanish)

# Get the input files from the input-dir
input_dir = "/home/abi/minutes/res"
# input_files = os.listdir("/home/abi/minutes/res")
input_files = sorted(os.listdir(input_dir), key=lambda x: int(''.join(filter(str.isdigit, x))))

# init /home/abi/minutes/out/trans.txt
with open("/home/abi/minutes/out/trans.txt", "w"):
    pass

# Loop over the input files
for input_file in input_files:
    # Get the input text from the file
    with open(f"/home/abi/minutes/res/{input_file}", "r") as file:
        text_to_translate = file.read()

        # Initialize the translator
        translator = Translator()

        # Translate the text
        translated_text = translator.translate(text_to_translate, src=source_language, dest=target_language)

        # Print the translation
        # print(f"Source Language ({LANGUAGES[source_language]}): {text_to_translate}")
        # print(f"Artikel ({LANGUAGES[target_language]}): {translated_text.text}")

        # You can also save the translated text to a file if needed
        output_file_path = "/home/abi/minutes/out/trans.txt"
        with open(output_file_path, "a", encoding="utf-8") as file:
            file.write(f"/home/abi/minutes/res/{input_file}" +"\n\n" + translated_text.text + "\n\n")

print(f"Translation saved to {output_file_path}")
