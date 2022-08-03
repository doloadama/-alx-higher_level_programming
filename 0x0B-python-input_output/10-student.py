#!/usr/bin/python3

"""10-student.py"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
         """Initializes the first_name, last_name, age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """Retrieves a dictionary of a Student instances"""
        if attr is None:
            return self.__dict__
        new_dict = {}

        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception:
                pass
        return new_dict
