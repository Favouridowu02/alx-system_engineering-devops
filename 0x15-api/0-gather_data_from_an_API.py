#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
from sys import argv

if __name__ == "__main__":
    """This is a Module that prints a Format"""
    uri = "https://jsonplaceholder.typicode.com/"
    user = requests.get(uri + "users/{}".format(argv[1])).json()
    todos = requests.get(uri + "todos", params={"userId": argv[1]}).json()

   completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
