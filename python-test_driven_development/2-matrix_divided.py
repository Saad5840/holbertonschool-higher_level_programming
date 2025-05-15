#!/usr/bin/python3
"""
Matrix division module.
Provides a function to divide all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding results to 2 decimals.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists of floats: New matrix with divided values.

    Raises:
        TypeError: If matrix elements are not int/float or matrix rows differ in size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2)
    [[0.75, 1.25], [1.75, 2.25]]
    >>> matrix_divided([[1, 2], [3]], 2)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    >>> matrix_divided([[1, 2], ['3', 4]], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2], [3, 4]], "2")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not matrix or
        not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
