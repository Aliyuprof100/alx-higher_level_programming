#!/usr/bin/python3
"""Question 4"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square's side.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
