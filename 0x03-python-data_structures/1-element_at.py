#!/usr/bin/python3
def element_at(my_list, idx):
    x = 0
    for i in my_list:
        if idx == x:
            return i
        x += 1;
