import sys
import re
from spellchecker import SpellChecker

# Function to remove the timestamp from a line
def remove_timestamp(line):
    return re.sub(r'^[0-9]{2}:[0-9]{2}.[0-9]{3} --> [0-9]{2}:[0-9]{2}.[0-9]{3}|^[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}', '', line)

# Function to apply replacements to a line
def rep_with(line, flag=re.IGNORECASE):
    line = re.sub(r'((mon|tues|wed(nes)?|thur(s)?|fri|sat(ur)?|sun)(day)?)\b', r'\g<0>', line)
    line = re.sub(r'^H[ou]\w+ing|\w+keeping', 'Housekeeping', line)
    line = re.sub(r'^[BPF](ina)\w+|[bpf](ina)\w+', 'Finance', line)
    line = re.sub(r'takbisaan', 'Tapisan', line)
    line = re.sub(r'F[NM][NB]|[Pp]embeli\s', 'F&B ', line)
    line = re.sub(r'RBI', 'RV', line)
    line = re.sub(r'EJ Edward', 'discussion', line)
    line = re.sub(r'[A-Z]VIP', 'VVIP', line)
    line = re.sub(r'[Ll]ory', 'lori', line)
    line = re.sub(r'[Tt]oast [Cc]lass', 'toast glass', line)
    line = re.sub(r'[Kk]ursi', 'kerusi', line)
    line = re.sub(r'Siapak', 'setiap', line)
    line = re.sub(r'kepas', 'kipas', line)
    line = re.sub(r'suat', 'surat', line)
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
    line = re.sub(r'pedera', 'saudara', line)
    line = re.sub(r'azap', 'nazak', line)
    line = re.sub(r'permadangan', 'pemasangan', line)
    line = re.sub(r'kemah', 'khemah', line)
    line = re.sub(r'[A-Z][A-Z]C\b', 'PMC', line)
    line = re.sub(r'bisyarat', 'Mesyuarat', line)
    line = re.sub(r'lenscaping', 'landscaping', line)
    line = re.sub(r'Aisyah', 'HR', line)
    line = re.sub(r'tamak', 'semak', line)
    line = re.sub(r'kubis', 'peti', line)
    line = re.sub(r'kopi', 'panas', line)
    line = re.sub(r'Papa', 'apa', line)
    line = re.sub(r'hargana', 'harganya', line)
    line = re.sub(r'kawan', 'mereka', line)
    line = re.sub(r' ,', ',', line)
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

    return line

# Function to perform spell-checking
def spell_check(line):
    spell = SpellChecker()
    words = line.split()
    corrected_words = []

    for word in words:
        if word not in words:
            corrected_word = spell.correction(word)
            if corrected_word is not None:
                corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)

    corrected_line = ' '.join(corrected_words)
    return corrected_line

def print_section(line, pat_sect, seen):
    for pattern, section in pat_sect.items():
        if re.search(section, line, re.IGNORECASE) and section not in seen:
            print("\nItem#", section.upper())
            seen.add(section)
            break

def print_headers(line, pat_dept, seen):
    for pattern, department in pat_dept.items():
        if re.search(pattern, line, re.IGNORECASE) and department not in seen:
            print("\nDept#", department.upper())
            seen.add(department)
            break

# Main code
if len(sys.argv) < 2:
    print("Please provide the input file as a command-line argument.")
    sys.exit(1)

input_file = sys.argv[1]

pat_sect = {
    r'item-1': "Pendahuluan Pengerusi",
    r'item-2': "Perkara-Perkara Berbangkit",
    r'item-3': "Perkara-Perkara Daripada Jabatan",
    r'item-4': "Rumusan dan Penutup"
}

pat_dept = {
    r'^fo\b|deluxe room|\b1.[1-9]\s': "front office",
    r'^hr\b|interview|temuduga|2.[1-9]\s': "hr",
    r'^f&b\s|revenue|RV|DMP|3.[1-9]\s': "f&b",
    r'kitchen|4.[1-9]\s': "kitchen",
    r'steward|Cef|Chef|5.[1-9]\s': "steward",
    r'security|CCTV|6.[1-9]\s': "security",
    r'purchasing|7.[1-9]\s': "purchasing",
    r'maint|8.[1-9]\s': "maintenance",
    r'asset|9.[1-9]\s': "asset",
    r'^it\s|10.[1-9]\s': "it",
    r'housekeeping|freshner|11.[1-9]\s': "housekeeping",
    r'sales|12.[1-9]\s': "sales",
    r'finance|invoice|invois|13.[1-9]\s': "finance",
    r'operation|14.[1-9]\s': "operation",
    r'pengurus': "pengurus"
}

seen_departments = set()
seen_sections = set()
seen_lines = set()  # To store unique lines

try:
    with open(input_file, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found:", input_file)
    sys.exit(1)

# Print headers and unique lines
for line in lines:
    line = line.strip()
    line = remove_timestamp(line)
    line = rep_with(line)
    line = spell_check(line)

    # Find and print section headers based on pat_sect
    print_headers(line, pat_sect, seen_sections)

    # Find and print headers based on pat_dept
    print_headers(line, pat_dept, seen_departments)

    # Add the line to seen_lines set only if it's not empty
    if line != "":
    	print(line)

