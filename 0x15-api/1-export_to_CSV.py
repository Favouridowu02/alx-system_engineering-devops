#!/usr/bin/python
"""
    This Module Gets User Data from an API and stores it in aa csv file
"""
import
from sys import argv
import json
import requests

if __name__ == "__main__":
    """ This Part of the Module will run"""
    uri = "https://jsonplaceholder.typicode.com/"
    with open(argv[1] + '.csv', 'w', newline='') as csvfile:
        writing = csv.writer(csvfile, delimiter=',', quotechar='"')
        data = requests.get(uri + "users/{}".format(argv[1])).json()
        todos = requests.get(uri + "todos/", params={"userId": argv[1]}).json()
        for todo in todos:
            user_id = str(data["id"]) + ""
            name = str(data["name"]) + ""
            status = str(todo["completed"]) + ""
            title = str(todo["title"]) + ""
            writing.writerow([user_id, name, status, title])
