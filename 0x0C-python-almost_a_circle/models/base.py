#!/usr/bin/python3

"""Define Base class"""
from os import path
import json


class Base(object):
    """Base: Class define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ initialized constructor
        Args:
            id (int): Defaults 2 None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: dict):
        """list to json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
