from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=False)

# if you have a dictionary...
spell.word_frequency.load_dictionary('../out/my.json')

# or... if you have text
# spell.word_frequency.load_text_file('malay.txt')

# export it out for later use!
spell.export('../py/my.gz', gzipped=True)
