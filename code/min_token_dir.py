import os

input_directory = '/home/app/script'
total_words = 0

# Iterate over files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_directory, filename)
        number_of_words = 0
        fs = round(os.stat(file_path).st_size/1024,1) 

        # Read the text file
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Tokenize the text
        words = text.split()
        number_of_words += len(words)
        total_words += number_of_words
        
        print(f"Number of tokens in {filename}: {number_of_words} - {fs} Kb")

print(f"Total number of tokens in all files in the input directory: {total_words}")