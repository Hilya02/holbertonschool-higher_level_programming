#!/usr/bin/python3
"""
BaseGeometry class module.

Define BaseGeometry class.
"""


class BaseGeometry:
    """Define a BaseGeometry."""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
