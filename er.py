import re

text = "This is a test?, question."

# Create a regex that matches the question mark (`?`) and comma (`,`) characters.
regex = re.compile("[?,]")

# Replace all occurrences of the question mark and comma characters with the empty string.
new_text = re.sub(regex, "", text)

print(new_text)

