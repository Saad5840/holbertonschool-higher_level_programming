#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
The function handles type checking and matrix validation before performing division.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (integer or float)

    Returns:
        New matrix with divided values rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not list of lists of numbers,
                  or if rows have different sizes,
                  or if div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
