from spellchecker import SpellChecker

# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=False)

# if you have a dictionary...
<<<<<<< HEAD
spell.word_frequency.load_dictionary('/home/abi/minutes/my.json')
=======
spell.word_frequency.load_dictionary('/home/abi/minutes/out/my.json')
>>>>>>> a23fe19d5f8932229be916e239d756acd9353423

# or... if you have text
# spell.word_frequency.load_text_file('malay.txt')

# export it out for later use!
spell.export('/home/abi/minutes/my.gz', gzipped=True)
