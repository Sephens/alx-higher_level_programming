#!/usr/bin/python3
# Write a function that checks for lowercase character.

# Prototype: def islower(c):
# Returns True if c is lowercase
# Returns False otherwise
# You are not allowed to import any module
# You are not allowed to use str.upper() and str.isupper()
def islower(c):
    return(ord('a') <= ord(c) <= ord('z'))
