#!/usr/bin/python3
# 0-square_matrix_simple.py
# Steven Odhiambo
# Write a function that computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    # Compute the square value of all integers of a matrix.
    return ([list(map(lambda x: x * x, row)) for row in matrix])
