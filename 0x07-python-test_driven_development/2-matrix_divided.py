#!/usr/bin/python3
# 2-matrix_divided.py
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of numbers (int or float).
        TypeError: If the matrix rows have different sizes.
        TypeError: If div is not a number (int or float).
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: A new matrix representing the result of the division, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a list of lists of numbers (int or float)")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (int or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
