#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- displays the body of the response
"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, error

    url = argv[1]

    try:
        with request.Request(url) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
