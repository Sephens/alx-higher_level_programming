#!/usr/bin/python3


def uppercase(str):
    new_string = ""
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            new_string = new_string + chr((ord(letter) - 32))
        else:
            new_string = new_string + letter

    print("{}".format(new_string), end=', ')
