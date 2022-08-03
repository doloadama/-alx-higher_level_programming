#!/usr/bin/python3
"""1-write_file.py"""

""" a function that writes a string to a text file (UTF8)
    and returns the number of characters written.
"""

def write_file(filename="", text=""):
    """Writes a string to a text file in UTF-8.
       Args:
           filename: a text file
           text (str): The text to write to the file.
       Returns: the number of characters written.
    """
    with open(filename, 'w', encoding="UTF-8") as f:
       count =  f.write(text)    
    return count
