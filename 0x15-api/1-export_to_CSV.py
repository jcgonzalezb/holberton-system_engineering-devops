#!/usr/bin/python3
"""  Python script to export data in the CSV format. """
import requests
from sys import argv


def export_to_csv():
    """
    Function that exports data in CSV format:
    Requirements:
    Records all tasks that are owned by this employee.
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
    File name must be: USER_ID.csv.
    """
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            USER_ID = (u.get('id'))
            USERNAME = (u.get('username'))
            break
    TASK_COMPLETED_STATUS = []
    TASK_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_COMPLETED_STATUS.append(t.get('completed'))
            TASK_TITLE.append(t.get('title'))
    print("{}, {}, {}, {}".format(USER_ID, USERNAME,
          TASK_COMPLETED_STATUS, TASK_TITLE))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    export_to_csv()
