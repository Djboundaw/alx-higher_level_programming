#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [[x**2 for x in new_matrix[i]] for i in range(len(new_matrix))]
    return (new_matrix)
