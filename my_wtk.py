import json
import re

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

def write_json(word_counts, filename):
    with open(filename, "w") as f:
        json.dump(word_counts, f)
        # Add a line break after each record
        f.write("\n")

if __name__ == "__main__":
    input_file = "out/news.txt"
    with open(input_file, "r") as f:
        text = f.read()
    filtered_text = filter_numbers_and_dates(text)
    tokens = tokenize_text(filtered_text)
    word_counts = get_word_frequency(tokens)
    write_json(word_counts, "out/my.json")

