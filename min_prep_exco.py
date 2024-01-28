# min_prep_exco.py
# input out/min_exco.vtt
# output out/out.txt

import re
from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=False, distance=1)

# if you have a dictionary...
spell.word_frequency.load_dictionary('my.gz')

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

# Function to remove the timestamp from a line
def remove_timestamp(line):
    return re.sub(r'^[0-9]{2}:[0-9]{2}.[0-9]{3} --> [0-9]{2}:[0-9]{2}.[0-9]{3}|^[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}', '', line)

# Function to find and outfile.write headers based on a pattern

def pr_hd():
   outfile.write("MESYUARAT JK RAFOC\n")
   outfile.write("Siri: 3\t\tTahun:2023")

   outfile.write("\n")

def pr_sect(line, pat_sect, seen, outfile):
    for pattern, section in pat_sect.items():
        if re.search(pattern, line, re.IGNORECASE) and section not in seen:
            outfile.write("\nItem: " + section.upper() + "\n")
            seen.add(section)
            break

# Main code
seen_line = set()
input_file = "out/agm23.txt"

# Determine section for item
pat_sect = {
    r'item:1': "Pendahuluan Pengerusi",
    r'item:2': "Mengesah dan Meluluskan Minit Mesyuarat",
    r'item:3': "Perkara-Perkara Berbangkit",
    r'item:4': "Laporan Keahlian",
    r'item:5': "Laporan Kewangan",
    r'item:6': "Perkara-perkara Daripada AJK",
    r'item:7': "Penutup"
}

with open(input_file, 'r') as file:
    lines = file.readlines()

# Output file name
output_file = "out/out.txt"

# Open the output file in write mode
with open(output_file, 'w') as outfile:

    # Write headers to the output file
    pr_hd()

    # Process each line in the input file
    for line in lines:
        line = line.strip()

        # Remove timestamp
        line = remove_timestamp(line)

        # Perform spelling correction
        line = correct_spelling(line)

        # Write the cleaned line to the output file if it's not empty
        if line != "" and line not in seen_line:
            outfile.write(line + "\n")
            seen_line.add(line)
  