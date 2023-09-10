# min_shred.py 
# input: out/out.txt output: shred/

import os
import re

def write_to_file(lines, output_file):
    with open(output_file, 'a') as file:
        for line in lines:
            file.write(line)

def remove_duplicates(input_file):
    lines_seen = set()  # Set to store unique lines
    cleaned_lines = []

    with open(input_file, 'r') as file:
        for line in file:
            if line not in lines_seen:
                cleaned_lines.append(line)
                lines_seen.add(line)

    return cleaned_lines

def process_file(input_file, output_directory):
    cleaned_lines = remove_duplicates(input_file)

    output_files = {}
    current_group = None
    current_group_count = 0
    current_tokens = 0

    for line in cleaned_lines:
        if re.search(r'(Dept:|Item:)', line):
            current_group = line.strip()
            current_group_count += 1
            current_tokens = 0

            if current_group not in output_files:
                output_files[current_group] = os.path.join(output_directory, f'{current_group_count}.txt')
                write_to_file([line], output_files[current_group])
                continue

        if current_group is not None:
            current_tokens += len(line.split())
            
            if current_group in output_files:
                if current_tokens <= 1000:
                    write_to_file([line], output_files[current_group])
                    
                else:
                    if current_tokens > 1000 and current_tokens <= 2000:
                        new_file = os.path.join(output_directory, f'{current_group_count}a.txt')
                        output_files[current_group] = new_file
                        write_to_file([line], new_file)
                    else:
                        if current_tokens > 2000 and current_tokens <= 3000:
                            new_file = os.path.join(output_directory, f'{current_group_count}b.txt')
                            output_files[current_group] = new_file
                            write_to_file([line], new_file)
                        else:
                            if current_tokens > 3000 and current_tokens <= 4000:
                                new_file = os.path.join(output_directory, f'{current_group_count}c.txt')
                                output_files[current_group] = new_file
                                write_to_file([line], new_file)
                            else:
                                if current_tokens > 4000 and current_tokens <= 5000:
                                    new_file = os.path.join(output_directory, f'{current_group_count}d.txt')
                                    output_files[current_group] = new_file
                                    write_to_file([line], new_file)
            else:
                current_group_count += 1
                current_tokens = len(line.split())
                new_file = os.path.join(output_directory, f'{current_group_count}.txt')
                output_files[current_group] = new_file
                write_to_file([line], new_file)

# Declare the input file path and the output directory
input_file_path = '/home/abi/minutes/out/out.txt'
output_directory = '/home/abi/minutes/shred/'

# Remove existing files from the output directory
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    os.remove(file_path)

# Process the file
process_file(input_file_path, output_directory)