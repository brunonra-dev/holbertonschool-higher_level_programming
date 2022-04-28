#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
from sys import argv
import requests


def main():
    """function"""
    if len(argv) > 1:
        variables = {'q': argv[1]}
    else:
        variables = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', variables)
    try:
        r = req.json()
        if not r:
            print("No result")
        else:
            print("[{}] {}".format(r.get('id'), r.get('name')))
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
