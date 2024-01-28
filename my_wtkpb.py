import json
import re
import tqdm

def tokenize_text(text):
    tokens = re.split(r"\W+", text)
    return tokens

def filter_numbers_and_dates(text):
    pattern = r"\d+|\d{4}-\d{2}-\d{2}"
    filtered_text = re.sub(pattern, "", text)
    return filtered_text

def get_word_frequency(tokens):
    word_counts = {}
    for token in tokens:
        if token in word_counts:
            word_counts[token] += 1
        else:
            word_counts[token] = 1
    return word_counts

#  sed -i 's/,/,\n/g' my.json
def write_json(word_counts, filename):
    with open(filename, "w") as f:
        json.dump(word_counts, f, indent=2)

# input: head -7000 news.txt > news.tmp
if __name__ == "__main__":
    input_file = "/workspace/minutes/out/news.tmp"
    with open(input_file, "r") as f:
        text = f.read()
    filtered_text = filter_numbers_and_dates(text)
    tokens = tokenize_text(filtered_text)
    word_counts = get_word_frequency(tokens)

    with tqdm.tqdm(total=len(tokens),leave=True) as pbar:
        for token in tokens:
            pbar.update()
    write_json(word_counts, "/workspace/minutes/out/my.json")

