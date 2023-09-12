#!/usr/bin/python3
# 100-matrix_mul.py
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Raises:
        ValueError: If m_a or m_b is empty or cannot be multiplied.
        TypeError: If m_a or m_b is not a list of lists of ints/floats, or if their rows are not of the same size.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both m_a and m_b must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("Both m_a and m_b must be lists of lists")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("All rows of m_a and m_b must have the same size")

    if not all(isinstance(ele, (int, float)) for row in m_a for ele in row) or not all(isinstance(ele, (int, float)) for row in m_b for ele in row):
        raise TypeError("All elements of m_a and m_b must be integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    inverted_b = [[m_b[c][r] for c in range(len(m_b))] for r in range(len(m_b[0]))]

    new_matrix = [[sum(row_a[i] * col_b[i] for i in range(len(inverted_b[0]))) for col_b in inverted_b] for row_a in m_a]

    return new_matrix

