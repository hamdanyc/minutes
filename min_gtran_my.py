from googletrans import Translator
import os

# Input and output folder paths
input_folder = 'res/'
output_folder = 'my/'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize the translator
translator = Translator()

# Iterate through the text files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith('.txt'):
        with open(os.path.join(input_folder, file_name), 'r') as file:
            text = file.read()
            # Translate the text to Malay
            translated = translator.translate(text, src='en', dest='ms')
            # Write the translated text to a new file in the output folder
            with open(os.path.join(output_folder, file_name), 'w') as output_file:
                output_file.write(translated.text)