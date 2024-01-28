# min_gtran.py
# Translate text to Malay
# input: /workspace/minutes/res
# output: /workspace/minutes/out/trans.txt

import os
from googletrans import Translator
from googletrans.constants import LANGUAGES

# Define the input and output language codes
source_language = "en"  # Input text language (e.g., English)
target_language = "ms"  # Output language (e.g., Spanish)

def keyfunc(x):
    return x.rjust(100, '0')

# Get the input files from the input-dir files_sorted = sorted(files, key=keyfunc)
# input_files = sorted(os.listdir("/workspace/minutes/res"), key=keyfunc)
input_files = sorted(os.listdir("/workspace/minutes/res"))

# init /workspace/minutes/out/trans.txt
with open("/workspace/minutes/out/trans.txt", "w"):
    pass

# Loop over the input files sorted(os.listdir(folder_path)):
for input_file in input_files:
    # Get the input text from the file
    with open(f"/workspace/minutes/res/{input_file}", "r") as file:
        text_to_translate = file.read()

        # Initialize the translator
        translator = Translator()

        # Translate the text
        translated_text = translator.translate(text_to_translate, src=source_language, dest=target_language)

        # Print the translation
        # print(f"Source Language ({LANGUAGES[source_language]}): {text_to_translate}")
        # print(f"Artikel ({LANGUAGES[target_language]}): {translated_text.text}")

        # You can also save the translated text to a file if needed
        output_file_path = "/workspace/minutes/out/trans.txt"
        with open(output_file_path, "a", encoding="utf-8") as file:
            file.write(f"/workspace/minutes/res/{input_file}" +"\n\n" + translated_text.text + "\n\n")

print(f"Translation saved to {output_file_path}")
