#!/usr/bin/python3
"""

This module contains a function that adds two integers.

"""
def add_integer(a, b=98):
    """Args: a (int): The first number to be added. b (int): The second number to be added.
    Returns: int: The return value. The sum of a and b.
    Raises: TypeError: If either of a or b is not an integer or a float"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
