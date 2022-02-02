#!/usr/bin/python3
"""
pascal_triangle module
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    tri = []
    tmp = [1]
    if n == 0:
        return tri

    for i in range(n):
        tmp = [1]
        for j in range(i):
            tmp.append(i)
        tmp[-1] = 1
        tri.append(tmp)

    return tri
