#!/usr/bin/python3
"""class Rectangle inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle instance using # character"""
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)
