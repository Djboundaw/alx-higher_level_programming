#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Divide alle matrix elements
    Args:
        matrix: must be a matrix or typeError raise
        div: must be a number and different of 0
    """
    if matrix == [] or (not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    matrix = [[round(i / div, 2) for i in ele] for ele in matrix]
    return (matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/2-matrix_divided.txt")
