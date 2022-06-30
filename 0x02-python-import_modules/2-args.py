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
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
