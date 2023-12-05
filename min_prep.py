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

# Function to apply replacements to a line
def rep_with(line,flag=re.IGNORECASE):
    line = re.sub(r'((mon|tues|wed(nes)?|thur(s)?|fri|sat(ur)?|sun)(day)?)\b', r'\g<0>', line)
    line = re.sub(r'takbisaan', 'Tapisan', line)
    line = re.sub(r'F[NM][NB]|[Pp]embeli\s', 'F&B ', line)
    line = re.sub(r'RBI', 'RV', line)
    line = re.sub(r'4 hour|4 hr', 'for hour', line)
    line = re.sub(r'EJ Edward', 'discussion', line)
    line = re.sub(r'syibetang', 'syif petang', line)
    line = re.sub(r'syipagi', 'syif pagi', line)
    line = re.sub(r'syimalang', 'syif malam', line)
    line = re.sub(r'[A-Z]VIP', 'VVIP', line)
    line = re.sub(r'[Ll]ory', 'lori', line)
    line = re.sub(r'[Tt]oast [Cc]lass', 'toast glass', line)
    line = re.sub(r'[Kk]ursi', 'kerusi', line)
    line = re.sub(r'Siapak', 'setiap', line)
    line = re.sub(r'kepas', 'kipas', line)
    line = re.sub(r'suat', 'surat', line)
    line = re.sub(r'soh|soy', 'so', line)
    line = re.sub(r'soh', 'so', line)
    line = re.sub(r'tua', 'tu', line)
    line = re.sub(r'torque clutch', 'torch light', line)
    line = re.sub(r'Miss Nine', 'mess-night', line)
    line = re.sub(r'kandidat', 'calon', line)
    line = re.sub(r'bunyi bicara', 'budi bicara', line)
    line = re.sub(r'arlari', 'almari', line)
    line = re.sub(r'Licking', 'leaking', line)
    line = re.sub(r'Cik', 'En.', line)
    line = re.sub(r'pensi', 'occupancy', line)
    line = re.sub(r'[Pp]ergawain', 'pegawai', line)
    line = re.sub(r'Rahim', 'Ibrahim', line)
    line = re.sub(r'Ingwars|Ingos|Imboss', 'invois', line)
    line = re.sub(r'Penhouse', 'Penthouse', line)
    line = re.sub(r'dina', 'dinner', line)
    line = re.sub(r'baby', 'bulan', line)
    line = re.sub(r'generaza', 'kol Razak', line)
    line = re.sub(r'pedera', 'saudara', line)
    line = re.sub(r'azap', 'nazak', line)
    line = re.sub(r'anak perempuan', 'tuan-tuan dan puan-puan', line)
    line = re.sub(r'permadangan', 'pemasangan', line)
    line = re.sub(r'kemah', 'khemah', line)
    line = re.sub(r'[A-Z][A-Z]C\b', 'PMC', line)
    line = re.sub(r'bisyarat|misha', 'Mesyuarat', line)
    line = re.sub(r'lenscaping', 'landscaping', line)
    line = re.sub(r'Aisyah', 'HR', line)
    line = re.sub(r'tamak', 'semak', line)
    line = re.sub(r'kubis', 'peti', line)
    line = re.sub(r'kopi', 'panas', line)
    line = re.sub(r'Papa', 'apa', line)
    line = re.sub(r'hargana', 'harganya', line)
    line = re.sub(r'kawan', 'mereka', line)
    line = re.sub(r'ok,', 'ok', line)
    line = re.sub(r'^ok, ', '^ok', line)
    line = re.sub(r'kata,\s', 'kata', line)
    line = re.sub(r'telefon kecil', 'telefon kitchen', line)
    line = re.sub(r'kejawatan,', 'perjawatan', line)
    line = re.sub(r'^[Aa]\w+[ae]t', 'Asset', line)
    line = re.sub(r'^[CK]\w+en\b|\b[CK]\w+en\b|ofisier', 'Kitchen', line)
    line = re.sub(r'^Ste\+ ', 'Steward', line)
    line = re.sub(r'Rupiah|^Rp|Rp\s','RM', line)
    line = re.sub(r'racing', 'Purchasing', line)
    line = re.sub(r'mantau' ,' Tim Pemantau', line)
    line = re.sub(r'Mas[sk]','Mas', line)
    line = re.sub(r'Rafiqah','RAFOC', line)
    line = re.sub(r'[az]eribadi','peribadi', line)
    line = re.sub(r'saikan','syarikat', line)
    line = re.sub(r'[Cc]aptain','Kapt.', line)
    line = re.sub(r'4 year|boyer','foyer', line)
    line = re.sub(r'labat','lambat', line)
    line = re.sub(r'\b[Mm][ea][ps]\b','Mes', line)
    line = re.sub(r'Ali Jauh Tak Kuasa','AJK', line)
    line = re.sub(r'Bismarck Boira','Wisma Perwira', line)
    line = re.sub(r'[Ll][a-z]ndr[iy]','laundri', line)
    line = re.sub(r'[Rr]osak|kong\b|kaput','rosak', line)
    line = re.sub(r'[bB]orum|ball\w+ ','Ballroom', line)
    line = re.sub(r'\bMPK','DMPK', line)
    line = re.sub(r'ranai','Lanai', line)
    line = re.sub(r'mf night|mesnit','mess-night', line)
    line = re.sub(r'Rehesel','raptai', line)
    line = re.sub(r'Exact level','Exec level', line)
    line = re.sub(r'major VIP','meja VIP', line)
    line = re.sub(r'bambang','barang', line)
    line = re.sub(r'pengguru|pengguru\w+','pengurus', line)
    line = re.sub(r'Jumaat Pengurus','jumpa Pengurus', line)
    line = re.sub(r'Jumaat PMC','jumpa PMC', line)
    line = re.sub(r'pending','tertangguh', line)
    line = re.sub(r'pendari','Bendahari', line)
    line = re.sub(r'Sunday Pyramid','Sunway Pyramid', line)
    line = re.sub(r'\?','', line)
    return line

# Function to find and outfile.write headers based on a pattern

def pr_title():
    outfile.write("Title: PROFIT AND LOSS\n")
    outfile.write("Date: November 23\n")
    outfile.write("\n")

def pr_hd():
   outfile.write("Dept: FRONT OFFICE\n")
   outfile.write("Syif pagi ...\n")
   outfile.write("Syif petang ...\n")
   outfile.write("Syif malam ...\n")
   outfile.write("daily room report\n")
   outfile.write("Living-in: 320\n")
   outfile.write("Standard: 279\n")
   outfile.write("Deluxe: 35\n")
   outfile.write("VIP: 6\n")
   outfile.write("Transit: 7\n")
   outfile.write("Standard: 3\n")
   outfile.write("Deluxe: 3\n")
   outfile.write("VIP: 1\n")
   outfile.write("Homestay Perwira: 0\n")
   outfile.write("\n")

def pr_sect(line, pat_sect, seen, outfile):
    for pattern, section in pat_sect.items():
        if re.search(pattern, line, re.IGNORECASE) and section not in seen:
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

# Determine section by item
pat_sect = {
    r'item-1': "Pendahuluan Pengerusi",
    r'item-2': "Perkara-Perkara Berbangkit",
    r'item-3': "Perkara-Perkara Daripada Jabatan",
    r'item-4': "Rumusan dan Penutup"
}

# Determine section for department
pat_dept = {
    r'^fo\b|deluxe room|\b1\.[1-9]': "front office",
    r'^hr\b|interview|temuduga|2\.[1-9]': "hr",
    r'^f&b\s|revenue|RV\b|DMP\b|ban(k|q)uet|\b3\.[1-9]': "f&b",
    r'kitchen|cef|4\.[1-9]': "kitchen",
    r'steward|5\.[1-9]': "steward",
    r'security|CCTV|6\.[1-9]': "security",
    r'purchasing|7\.[1-9]': "purchasing",
    r'maint|8\.[1-9]': "maintenance",
    r'asset|9\.[1-9]': "asset",
    r'software|pc|application|network|device\s|10\.[1-9]': "it",
    r'housekeeping|freshner|11\.[1-9]': "housekeeping",
    r'sales|profit|revenue|12\.[1-9]': "sales",
    r'finance|invoice|invois|13\.[1-9]': "finance",
    r'operation|14\.[1-9]': "operation",
    r'pengurus': "pengurus"
}

seen_departments = set()
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
    pr_title()

    # Process each line in the input file
    for line in lines:
        line = line.strip()

        # Remove timestamp
        line = remove_timestamp(line)

        # Perform spelling correction
        line = correct_spelling(line)

        # Replace unknown words in the line
        line = rep_with(line)

        # Find and write section headers based on pat_sect
        pr_sect(line, pat_sect, seen_sections, outfile)

        # Find and write department headers based on pat_dept
        pr_dept(line, pat_dept, seen_sections, outfile)

        # Write the cleaned line to the output file if it's not empty
        if line != "" and line not in seen_line:
            outfile.write(line + "\n")
            seen_line.add(line)

    # Print the cleaned line if it's not empty
    if line != "" and line not in seen_line:
       with open("/home/abi/minutes/out/out.txt", "w") as f:
           f.write(line)
           seen_line.add(line)

