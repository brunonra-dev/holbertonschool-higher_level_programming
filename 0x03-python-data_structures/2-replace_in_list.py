#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if idx == i:
            my_list[i] = element
            return my_list
    return my_list
