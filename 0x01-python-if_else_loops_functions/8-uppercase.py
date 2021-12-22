#!/usr/bin/python3
def uppercase(str):
    upp_str = ''
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            upp_str += chr(ord(str[i]) - 32)
        else:
            upp_str += str[i]
    print('{}'.format(upp_str))
