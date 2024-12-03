#!/usr/bin/python3

""" This is the header file """


def add_integer(a, b=98):
    """
    Adds two integers.
    Parameters:
    a: Must be an integer or float
    b: Must be an integer or float (default: 98)
    Returns:
    The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
