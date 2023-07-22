from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=False)

# if you have a dictionary...
spell.word_frequency.load_dictionary('/home/abi/minit_mesyuarat_wp/out/my.json')

# or... if you have text
# spell.word_frequency.load_text_file('malay.txt')

# export it out for later use!
spell.export('/home/abi/minit_mesyuarat_wp/py/my.gz', gzipped=True)
