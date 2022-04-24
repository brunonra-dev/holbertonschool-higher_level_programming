#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL and displays
    the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            if res is not None:
                html = res.read()
                print(html.decode('utf-8'))
    except urllib.error.HTTPError as fail:
        print('Error code: {}'.format(fail.code))
