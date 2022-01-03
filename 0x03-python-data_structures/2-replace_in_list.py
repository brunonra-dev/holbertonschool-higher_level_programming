#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    x = 0
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    for i in my_list:
        if i == x:
            my_list[i] = element
            return my_list
        x += 1
