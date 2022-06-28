#!/usr/bin/python3
for letter in range(97, 123):
    letter = chr(letter)
    if letter not in "qe":
        print("{}".format(letter), end='')
