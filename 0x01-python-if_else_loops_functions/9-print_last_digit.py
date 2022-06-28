#!/usr/bin/python3
def print_last_digit(number):

    # Python abs() function is used to return the absolute value of a number
    # i.e., it will remove the negative sign of the number.
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
