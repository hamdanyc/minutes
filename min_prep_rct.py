# min_prep_rct.py
# input jk_siri_#.txt
# output out/out.txt

import sys
import re
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

# Function to remove the timestamp from a line
def remove_timestamp(line):
    return re.sub(r'^[0-9]{2}:[0-9]{2}.[0-9]{3} --> [0-9]{2}:[0-9]{2}.[0-9]{3}|^[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}', '', line)

# Function to find and outfile.write headers based on a pattern

def pr_hd():
   outfile.write("RAFOC COFFEE TALK\n")
   outfile.write("Siri: 11\t\tTahun:2023")

   outfile.write("\n")

def pr_sect(line, pat_sect, seen, outfile):
    for pattern, section in pat_sect.items():
        if re.search(pattern, line, re.IGNORECASE) and section not in seen:
            outfile.write("\nspeaker: " + section.upper() + "\n")
            seen.add(section)
            break

# Main code
if len(sys.argv) < 2:
    outfile.write("Please provide the input file as a command-line argument.")
    sys.exit(1)

input_file = sys.argv[1]

# Determine section for item
pat_sect = {
    r'speaker-1': "Moderator",
    r'speaker-2': "Lt Kol Rahman Wok",
    r'speaker-3': "Laksma Dato Nick Peterson TLDM",
    r'speaker-4': "Lt Kol Abdullah",
    r'speaker-5': "Laksda Dato' Danial",
    r'speaker-6': "Lt Jen Dato' Nawi",
    r'speaker-7': "Mej Dato' Abd Manan",
    r'speaker-8': "Mej Jen Datuk Mohd Halim",
    r'speaker-9': "Lt Kdr Phua",
    r'speaker-10': "Mej Jen Dato' Megat",
    r'speaker-11': "Mej Mior Rosli",
    r'speaker-12': "Brig Jen Dato' Nazari",
    r'speaker-13': "Lt Kol Shahrudin Hanifah ",
    r'speaker-14': "Mej Jen Dato' Termizi",
    r'speaker-15': "Kol Nik Zainin",
    r'speaker-16': "Lt Jen Dato' Sri Aziz"
}

# seen_departments = set()
seen_sections = set()
seen_line = set()

try:
    with open(input_file, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    outfile.write("File not found:", input_file)
    sys.exit(1)

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

        # Find and write section headers based on pat_sect
        pr_sect(line, pat_sect, seen_sections, outfile)

        # Write the cleaned line to the output file if it's not empty
        if line != "" and line not in seen_line:
            outfile.write(line + "\n")
            seen_line.add(line)
