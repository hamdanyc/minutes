import os
import re

def remove_duplicates(input_file):
    lines_seen = set()  # Set to store unique lines
    cleaned_lines = []

    with open(input_file, 'r') as file:
        for line in file:
            if line not in lines_seen:
                cleaned_lines.append(line)
                lines_seen.add(line)

    return cleaned_lines

def write_to_file(output_file, line):
    with open(output_file, 'a') as file:
        file.write(line)

def process_file(input_file, output_directory):
    cleaned_lines = remove_duplicates(input_file)
    group_counts = {}
    current_group = None
    current_tokens = 0

    for line in cleaned_lines:
        match = re.search(r'(dept:|item:|speaker:)', line)
        if match:
            if current_group is not None:
                current_group_count = group_counts[current_group]
                file_suffix = chr(97 + (current_tokens - 1) // 1000) if current_tokens <= 5000 else 'e'
                output_file = os.path.join(output_directory, f'{current_group_count}{file_suffix}.txt')
                write_to_file(output_file, line)

            current_group = match.group().strip()
            group_counts[current_group] = group_counts.get(current_group, 0) + 1
            current_tokens = 0
        else:
            if current_group is not None:
                current_tokens += len(line.split())
                if current_group in group_counts:
                    current_group_count = group_counts[current_group]
                    file_suffix = chr(97 + (current_tokens - 1) // 1000) if current_tokens <= 5000 else 'e'
                    output_file = os.path.join(output_directory, f'{current_group_count}{file_suffix}.txt')
                    write_to_file(output_file, line)

    # Write the remaining lines of the last group
    if current_group is not None:
        current_group_count = group_counts[current_group]
        file_suffix = chr(97 + (current_tokens - 1) // 1000) if current_tokens <= 5000 else 'e'
        output_file = os.path.join(output_directory, f'{current_group_count}{file_suffix}.txt')
        for line in cleaned_lines:
            write_to_file(output_file, line)

# Declare the input file path and the output directory
input_file_path = 'out/out.txt'
output_directory = 'shred/'

# Remove existing files from the output directory
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    os.remove(file_path)

# Process the file
process_file(input_file_path, output_directory)