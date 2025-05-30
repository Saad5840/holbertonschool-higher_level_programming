#!/usr/bin/python3
"""
This module provides a function to divide all elements
of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (integer or float)

    Returns:
        New matrix with divided values rounded to 2 decimal places

    Raises:
        TypeError: If arguments are invalid
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Special case for infinity
    if div == float('inf'):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(num / div, 2) for num in row] for row in matrix]
