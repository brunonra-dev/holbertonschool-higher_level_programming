#!/usr/bin/python3
"""
    Module sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            if res is not None:
                idreq = res.getheader('X-Request-Id')
            print(idreq)
    except Exception:
        pass
