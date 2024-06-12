#!/usr/bin/python3
""" This Module Contains Some Script that exports User Data using a Format """
from sys import argv
import json
import requests

if __name__ == "__main__":
    """
        This Section Of Code is Only Runnable when Not inported
        into another Module
    """
    uri = "https://jsonplaceholder.typicode.com/"
    user = requests.get(uri + "users/{}".format(argv[1])).json()
    todos = requests.get(uri + "todos", params={"userId": argv[1]}).json()
    json_my = {argv[1]: []}
    for todo in todos:
        use = {"task": todo["title"], "completed": todo["completed"],
               "username": user["username"]}
        json_my[argv[1]].append(use)
    with open(argv[1] + ".json", 'w') as json_file:
        json_file.write(json.dumps(json_my))
