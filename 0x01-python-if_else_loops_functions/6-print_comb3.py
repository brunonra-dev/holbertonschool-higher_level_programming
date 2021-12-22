#!/usr/bin/python3
for i in range(0, 10):
    for n in range(1, 10):
        if i < n and i != n:
            if i <= 7:
                print('{}{}, '.format(i, n), end='')
            else:
                print('{}{}'.format(i, n))
