#!/usr/bin/python3
import csv
from sys import argv
import requests
import json
"""
"""

if __name__ == "__main__":
    """ """
    uri = "https://jsonplaceholder.typicode.com/"
    data = requests.get(uri + "users/{}".format(argv[1])).json()
    print(data)
