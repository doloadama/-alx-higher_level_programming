#!/usr/bin/python3
"""9-student Module"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the date
        Args:
            first_name (str): first name
            last_name (str: last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary of a student instance"""
        return self.__dict__
