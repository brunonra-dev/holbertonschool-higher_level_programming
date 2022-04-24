#!/usr/bin/python3
"""
    Takes in a URL and an email, sends a POST request to the passed URL
    with the email as a parameter, and displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    reqq = urllib.request.Request(sys.argv[1], data)

    try:
        with urllib.request.urlopen(reqq) as res:
            if res is not None:
                html = res.read()
                print(html.decode('utf-8'))
    except Exception:
        pass
