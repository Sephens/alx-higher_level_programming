#!/usr/bin/python3
# Write a program that prints the number of and the list of its arguments.
# The output should be:
# Number of argument(s) followed by
# argument (if number is one) or arguments# (otherwise),
# followed by
# : (or . if no arguments were passed) followed by
# a new line, 
# followed by (if at least one argument),
# one line per argument:
# the position of the argument (starting at 1) followed by :,
# followed by th# e argument value and a new line
# Your code should not be executed when imported
# The number of elements of argv can be retrieved by using: len(argv)
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    print("{:d} {:s}{:s}".format(length-1,"argument", if length <=2 else "arguments", ".", if length ==  1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
