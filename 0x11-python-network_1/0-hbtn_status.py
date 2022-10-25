#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
req = request.Request(url)
with request.urlopen(req) as response:
    con = response.read()
    print("Body response:", end="$\n")
    print("\t- type: {}".format(type(con)), end="$\n")
    print("\t- content: {}".format(con), end="$\n")
    print("\t- utf8 content: {}".format(con.decode('utf-8')), end="$\n")
