#!/usr/bin/python3
<<<<<<< HEAD
# 3-infinite_add.py
# Brennan D Baraban <375@holbertonschool.com>
=======
# Write a program that prints the result of the addition of all arguments

# The output should be the result of the addition of all arguments, 
# followed by a new line
# You can cast arguments into integers by using int() 
# (you can assume that all arguments can be casted into integers)
# Your code should not be executed when imported
>>>>>>> 0dde9607da390c5608042f53ce4f9367b4ffe88f

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
