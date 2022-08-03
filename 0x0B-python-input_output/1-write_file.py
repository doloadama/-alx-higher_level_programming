#!/usr/bin/python3
"""1-write_file.py"""


def write_file(filename="", text=""):
    """Writes a string to a text file in UTF-8
    Args:
           filename: a text file
           text (str): The text to write to the file
    Return: the number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as f:
       count =  f.write(text)    
    return count
