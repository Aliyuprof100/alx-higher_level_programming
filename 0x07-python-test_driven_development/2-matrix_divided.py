#!/usr/bin/python3

""" This is the header file """


def matrix_divided(matrix, div):
    """    Divides all elements of a matrix by a given divisor. 
    Parameters:
    matrix (list of lists): A list of lists of integers or floats.
    div (int or float): The divisor.
    Returns:
    list of lists: A new matrix with each element divided by div and rounded to 2 decimal places.
    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats, or if rows are not of the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance (row, list)for row in matrix):
        raise("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(elemetn (int, integer)for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not instance(matrix[row]()):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div (int, integer)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
