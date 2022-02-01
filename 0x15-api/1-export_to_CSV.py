#!/usr/bin/python3
"""  Python script to export data in the CSV format. """
import csv
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
            USERNAME = (u.get('username'))
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    filename = "{}.csv".format(argv[1])
    with open(filename, mode='w') as csv_file:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                            "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    export_to_csv()
