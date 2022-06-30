#!/usr/bin/python3
# Write a program that imports all functions from the file calculator_1.py and handles basic operations.

# Usage: ./100-my_calculator.py a operator b
# If the number of arguments is not 3, your program has to:
# print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
# exit with the value 1
# operator can be:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# If the operator is not one of the above:
# print Unknown operator. Available operators: +, -, * and / followed with a new line
# exit with the value 1
# You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
# The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
# You are not allowed to use * for importing or __import__
# Your code should not be executed when imported

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
