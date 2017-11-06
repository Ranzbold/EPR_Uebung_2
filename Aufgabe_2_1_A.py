__author__ = "6611082: Cedric Reuter"
import string


def is_pangram(expression):
    included = True
    expression += expression.lower()
    alphabet = string.ascii_lowercase
    letters = ""
    for x in expression:
        if(x in alphabet):
            letters += x
    for b in alphabet:
        if b not in expression:
            included = False
            break

    if (included):
        print('Juhu, ein Pangramm.')
    else:
        print('Leider kein Pangramm.')

phrase = (input("--> "))
is_pangram(phrase)
