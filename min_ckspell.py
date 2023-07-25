import os
from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=False, distance=1)

# if you have a dictionary...
spell.word_frequency.load_dictionary('/home/abi/minutes/my.gz')

def correct_spelling(input_text):
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
input_path = 'hr.txt'
output_path = 'out_mod.txt'

# Read the input text file
with open(input_path, 'r', encoding='utf-8') as file:
    input_text = file.read()

# Perform spelling correction
corrected_text = correct_spelling(input_text)

# Write the corrected text to an output file
with open(output_path, 'w', encoding='utf-8') as file:
   file.write(corrected_text)
