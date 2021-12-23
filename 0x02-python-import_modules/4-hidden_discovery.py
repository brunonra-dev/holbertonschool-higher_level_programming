#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    elements = dir(hidden_4)
    for i in elements:
        if i[:2] != '__':
            print('{}'.format(i))
