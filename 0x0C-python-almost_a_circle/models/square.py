#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square extends from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor for square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str representation of square"""
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """set width and height with the same value, value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)
