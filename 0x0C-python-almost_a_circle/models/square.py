#!/usr/bin/python3

"""square.py"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A class that inherits the rectangle class"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                               self.size)

    @property
    def size(self):
        """retrieve size"""
        return self.size

    @size.setter
    def size(self, value):
        """set width and height with the same value, value"""
        self.width = value
        self.height = value
        
