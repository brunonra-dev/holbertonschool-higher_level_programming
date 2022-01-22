#!/usr/bin/python3
"""
This is the 5-text_indentation.py module
"""

def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of 
    these characters: ., ? and :

    Raises:
        TypeError:
            - If text is not str
    """

    nl = 0

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if nl == 1:
            print("\n")
            nl = 0
            continue
        if i == "." or i == "?" or i == ":":
            nl = 1
        print(i, end='')
