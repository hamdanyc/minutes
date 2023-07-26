from spellchecker import SpellChecker

# could add command line arguments to set the parameters of the spell
# check class; setup what type of information to present back, etc.
spell = SpellChecker(language=None, case_sensitive=False)
spell.word_frequency.load_dictionary('/home/abi/minutes/my.gz')
<<<<<<< HEAD
# spell.word_frequency.load_text_file('/home/abi/minutes/my_addterm.txt')
=======
spell.word_frequency.load_text_file('/home/abi/minutes/my_addterm.txt')
>>>>>>> a23fe19d5f8932229be916e239d756acd9353423
print("To exit, hit return without input!")

while True:
    word = input('Input a word to spell check: ')
    if word == '':  # not sure, but need a way to kill the program...
        break
    word = word.lower()
    if word in spell:
        print("'{}' is spelled correctly!".format(word))
    else:
        cor = spell.correction(word)
        print("The best spelling for '{}' is '{}'".format(word, cor))

        print("If that is not enough; here are all possible candidate words:")
        print(spell.candidates(word))
