#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
The function handles type checking, matrix validation, and division operations.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix: List of lists containing integers or floats
        div: Number to divide by (must be integer or float)

    Returns:
        New matrix with elements divided by div and rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                  or if rows have different sizes,
                  or if div is not a number
        ZeroDivisionError: If div is zero
    """
    # Validate matrix is a non-empty list of lists
    if (not isinstance(matrix, list) or not matrix or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all elements are numbers
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate uniform row sizes
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    return [[round(x / div, 2) for x in row] for row in matrix]
