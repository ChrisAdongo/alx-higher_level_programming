#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: A new matrix representing the multiplication of m_a by m_b.
    """
    return np.matmul(m_a, m_b)

