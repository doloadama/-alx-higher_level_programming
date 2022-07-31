#!/usr/bin/python3

"""
Function that divides all elements of a matrix
Each number must be an integer or float
Matrix is a list of lists
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
     if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for k in matrix:
        if type(k) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(k)
        elif size != len(k):
            raise TypeError("Each row of the matrix must have the same size")
        for i in k:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in k] for k in matrix]
