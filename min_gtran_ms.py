import googletrans

# Get the text from the file
with open("/home/abi/minutes/out/xaa", "r") as f:
    text = f.read()

# Set the source and destination languages
source_language = "en"
target_language = "ms"

# Translate the text
translator = googletrans.Translator()
translated_text = translator.translate(text, dest=target_language, src=source_language)

# Print the translated text
print(translated_text)
