#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """Computes the square value of all integers of a matrix using map."""
 
    return [[y**2 for y in x] for x in matrix]
