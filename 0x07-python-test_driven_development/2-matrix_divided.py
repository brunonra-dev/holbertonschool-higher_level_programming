#!/usr/bin/python3
"""
This is the 2-matrix_divided.py module
"""

def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Raises:
        TypeError:
            - If list of lists is not integers or floats.
            - If row of the matrix are not the same size.
            - If div is not a number.
        ZeroDivisionError:
            - If div is 0.

    Return:
        New matrix
    """
    row_len = len(matrix[0])
    e = "matrix must be a matrix (list of lists) of integers/floats"
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for i in matrix:
        if len(i) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            if type(matrix[row][i]) != int and type(matrix[row][i]) != float:
                raise TypeError(e)

    new = [[round(item/div, 2) for item in row] for row in matrix]
    return new
