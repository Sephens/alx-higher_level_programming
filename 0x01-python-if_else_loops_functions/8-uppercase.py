#!/usr/bin/python3
# Write a function that prints a string in uppercase followed by a new lin.

# Prototype: def uppercase(str):
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()

def uppercase(str):
    new_string = ""
    for letter in str:
        if letter >= 'a' and letter <= 'z':
            new_string = new_string + chr((ord(letter) - 32))
        else:
            new_string = new_string + letter

    print("{}".format(new_string), end=', ')
