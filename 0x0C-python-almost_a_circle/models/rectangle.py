#!/usr/bin/python3
from models.base import Base


""" Rectangle class module
"""


class Rectangle(Base):
    """ Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Define width property."""
        return self.__width

    @property
    def height(self):
        """Define height property."""
        return self.__height

    @property
    def x(self):
        """Define x property."""
        return self.__x

    @property
    def y(self):
        """Define y property."""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        value (int): the new length of the width.
        """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        value (int): the new length of the height.
        """
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @x.setter
    def x(self, value):
        """Set x.
        value (int): the new x.
        """
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, value):
        """Set y.
        value (int): the new y.
        """
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")