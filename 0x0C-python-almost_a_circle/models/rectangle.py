#!/usr/bin/python3

"""
Class taht inherits from Base
"""
from models.base import Base


class Rectangle:
    """Rectangle implementation
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self) -> int:
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """height setter
        """
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """x setter
        """
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """y setter
        """
        self.check_type_value('y', y, True)
        self.__y = y
