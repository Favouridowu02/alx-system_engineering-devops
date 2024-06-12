#!/usr/bin/python3
"""
    This Module Contains Some Script that exports All Users Data
    using a Format
"""
import json
import requests

if __name__ == "__main__":
    """
        This Section Of Code is Only Runnable when Not inported
        into another Module
    """
    uri = "https://jsonplaceholder.typicode.com/"
    users = requests.get(uri + "users/").json()
    json_my = {}
    filename = "todo_all_employees.json"
    for user in users:
        todos = requests.get(uri + "todos", params={"userId": user["id"]})
        todos = todos.json()
        json_my[user["id"]] = []
        for todo in todos:
            use = {"username": user["username"], "task": todo["title"],
                   "completed": todo["completed"]}
            json_my[user["id"]].append(use)
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(json_my))
