#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout
Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""

def read_file(filename=""):
    """
    reads a text file and prints it to stdout
    """
    with open('filename', 'r', encoding="utf-8") as f:
        for ligne in f:
            print(ligne, end="")
    
