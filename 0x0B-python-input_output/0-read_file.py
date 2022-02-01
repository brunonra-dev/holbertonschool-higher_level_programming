#!/usr/bin/python3
"""
read_file module
"""


def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            print(line, end='')
