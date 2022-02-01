#!/usr/bin/python3
""" Python script to export data in the JSON format. """
import json
import requests


def all_to_json():
    """Records all tasks that are owned by this employee.
       Special format. File name must be: todo_all_employees.json"""
    USERS = []
    userss = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in userss.json():
        USERS.append((u.get('id'), u.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        TASK_STATUS_TITLE.append((t.get('userId'),
                                  t.get('completed'),
                                  t.get('title')))


if __name__ == "__main__":
    all_to_json()