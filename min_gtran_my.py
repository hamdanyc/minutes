from googletrans import Translator
from googletrans.constants import LANGUAGES

# Define the input and output language codes
source_language = "en"  # Input text language (e.g., English)
target_language = "ms"  # Output language (e.g., Spanish)

# Load the text from a file
input_file_path = "/workspace/minutes/out/sampel.txt"  # Replace with the path to your input text file

with open(input_file_path, "r", encoding="utf-8") as file:
    text_to_translate = file.read()

# Initialize the translator
translator = Translator()

# Translate the text
translated_text = translator.translate(text_to_translate, src=source_language, dest=target_language)

# Print the translation
# print(f"Source Language ({LANGUAGES[source_language]}): {text_to_translate}")
print(f"Artikel ({LANGUAGES[target_language]}): {translated_text.text}")

# You can also save the translated text to a file if needed
output_file_path = "/workspace/minutes/out/sampel_output.txt"
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(translated_text.text)

print(f"Translation saved to {output_file_path}")
