#!/usr/bin/python3
""" This Module Gets User Data from an API and stores it in aa csv file"""
import csv
from sys import argv
import json
import requests

if __name__ == "__main__":
    """ This Part of the Module will run"""
    uri = "https://jsonplaceholder.typicode.com/"
    with open(argv[1] + '.csv', 'w', newline='') as csvfile:
        writing = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        data = requests.get(uri + "users/{}".format(argv[1])).json()
        todos = requests.get(uri + "todos/", params={"userId": argv[1]}).json()
        user_id = data["id"]
        name = data["username"]
        for todo in todos:
            status = todo["completed"]
            title = todo["title"]
            writing.writerow([user_id, name, status, title])
