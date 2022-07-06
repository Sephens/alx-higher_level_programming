#!/usr/bin/python3
# 2-uniq_add.py
# Write a function that adds all unique integers in a list (only once for each integer).

def uniq_add(my_list=[]):
    # Add all unique integers in a list (once for each integer).
    result = 0
    for x in set(my_list):
        result += x
    return (result)
