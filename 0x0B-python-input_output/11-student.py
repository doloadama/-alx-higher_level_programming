#!/usr/bin/python3
"""11-student.py"""

class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary represt"""
        if attrs is None:
            return self.__dict__
        dictionnaire = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionnaire[key] = value
                return dictionnaire

    def reload_from_json(self, json):
         """Replace all attributes of the Student.
         Args:
            json (dict): The key/value pairs to replace attributes with.
         """
         for key, value in json.items():
             setattr(self, key, value)
