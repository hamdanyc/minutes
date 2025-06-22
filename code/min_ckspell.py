import os
import re
from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=False, distance=1)

# if you have a dictionary...
spell.word_frequency.load_dictionary('my.gz')

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

def removeDuplicateWords(input_file_path):
    content = read_from_file(input_file_path)
    # Regex to matching repeated words
    regex = r'\b(\w+)(?:\W+\1\b)+'
    output = re.sub(r'Terima kasih kerana menonton', '', content, re.IGNORECASE)
    output = re.sub(regex, r'\1', content, flags=re.IGNORECASE)
    write_to_file(input_file_path, output)

def correct_spelling(input_file_path):
    input_text = read_from_file(input_file_path)
    # write_to_file(input_file_path, input_text)
    lines = input_text.split('\n')
    corrected_lines = []

    for line in lines:
        words = line.split()
        corrected_words = []

        for word in words:
           corrected_word = spell.correction(word)
           if corrected_word is not None:
              corrected_words.append(corrected_word)
           else:
              corrected_words.append(word)

        corrected_line = ' '.join(corrected_words)
        corrected_lines.append(corrected_line)

    corrected_text = '\n'.join(corrected_lines)
    return corrected_text

# Input and output directories
def main():
    input_folder = 'script/'
    output_folder = 'out/'

    # Remove existing files from the output directory
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        os.remove(file_path)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            output = correct_spelling(input_file_path)
            removeDuplicateWords(input_file_path)
            if output is not None:
                write_to_file(output_file_path, output)
                print(f"Processed file: {filename}")
            else:
                print(f"Error processing file: {filename}")

if __name__ == "__main__":
    main()
