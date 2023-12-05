# min_prep_exco.py
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
   outfile.write("MESYUARAT AGUNG TAHUNAN RAFOC\n")
   outfile.write("Tarikh: 8 Okt 2023")

   outfile.write("\n")

def pr_sect(line, pat_sect, seen, outfile):
    for pattern, section in pat_sect.items():
        if re.search(pattern, line, re.IGNORECASE):
            outfile.write("\nItem: " + section.upper() + "\n")
            seen.add(section)
            break

def pr_dept(line, pat_dept, seen, outfile):
    for pattern, department in pat_dept.items():
        title = ""
        if re.search(pattern, line, re.IGNORECASE) and department not in seen:
            outfile.write("\nDept: " + department.upper() + "\n")
            seen.add(department)
            break

# Main code
if len(sys.argv) < 2:
    outfile.write("Please provide the input file as a command-line argument.")
    sys.exit(1)

input_file = sys.argv[1]

# Determine section for item
pat_sect = {
    r'item-1': "Pendahuluan Pengerusi",
    r'item-2': "Laporan Tahunan",
    r'item-3': "Laporan Kewangan",
    r'item-4': "Usul Pindaan",
    r'item-5': "Perkara-perkara Daripada Ahli",
    r'item-6': "Penutup"
}

# Determine section for department
pat_dept = {
    r'^fo\b|deluxe room|\b1\.[1-9]': "front office",
    r'^hr\b|interview|temuduga|2\.[1-9]': "hr",
    r'^f&b\s|revenue|RV|DMP|3\.[1-9]': "f&b",
    r'kitchen|cef|4\.[1-9]': "kitchen",
    r'steward|5\.[1-9]': "steward",
    r'security|CCTV|6\.[1-9]': "security",
    r'purchasing|7\.[1-9]': "purchasing",
    r'maint|8\.[1-9]': "maintenance",
    r'asset|9\.[1-9]': "asset",
    r'^it\s|10\.[1-9]': "it",
    r'housekeeping|freshner|11\.[1-9]': "housekeeping",
    r'sales|profit|revenue|12\.[1-9]': "sales",
    r'finance|invoice|invois|13\.[1-9]': "finance",
    r'operation|14\.[1-9]': "operation",
    r'pengurus': "pengurus"
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

        # Find and write department headers based on pat_dept
        # pr_dept(line, pat_dept, seen_sections, outfile)

        # Write the cleaned line to the output file if it's not empty
        if line != "" and line not in seen_line:
            outfile.write(line + "\n")
            seen_line.add(line)
