#!/usr/bin/python3                                                                                                                                                                  
def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) or
        len(matrix) == 0 or
        not all(isinstance(row, list) for row in matrix) or
        any(len(row) == 0 for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)) or div != div or div in (float('inf'), float('-inf')):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

