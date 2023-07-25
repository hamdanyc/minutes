import os

def tokenize_text(text):
    # Split the text into individual tokens (words and punctuation)
    return text.split()


def split_file(input_file_path, output_path, max_tokens_per_file=1000):
    with open(input_file_path, 'r') as input_file:
        current_dept = None
        current_counter = 1
        sub_counter = ord('a')
        token_count = 0
        output_file = None

        for line in input_file:
            if line.strip().startswith('Dept:'):
                dept = line.strip().split('Dept:')[1].strip()
                if current_dept != dept:
                    current_dept = dept
                    current_counter += 1
                    sub_counter = ord('a')
                    token_count = 0
                    if output_file:
                        output_file.close()
                if token_count >= max_tokens_per_file:
                    output_file.close()
                    if sub_counter > ord('a'):
                        os.rename(
                            os.path.join(output_path, f"{current_counter}_{chr(sub_counter-1)}.txt"),
                            os.path.join(output_path, f"{current_counter}.txt")
                        )
                    sub_counter = ord('a')
                    token_count = 0
                if sub_counter == ord('a'):
                    output_file = open(os.path.join(output_path, f"{current_counter}.txt"), 'a')
                else:
                    output_file = open(os.path.join(output_path, f"{current_counter}_{chr(sub_counter)}.txt"), 'a')
                output_file.write(line)
                token_count += len(tokenize_text(line))
            else:
                if output_file:
                    output_file.write(line)
                    token_count += len(tokenize_text(line))

        if output_file:
            output_file.close()


def remove_files_in_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


input_file_path = "out/out.txt"
output_path = "shred/"  # Set your desired output directory here

# Remove all files in the output directory before separating the text file
remove_files_in_directory(output_path)

# Separate the text file into multiple output files
split_file(input_file_path, output_path)
