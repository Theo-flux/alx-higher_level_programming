#!/usr/bin/env python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests

    re = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type:", type(res.text))
    print("\t- type:", res.text)
