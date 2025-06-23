#!/usr/bin/python3
"""
This module connects to a MySQL database and lists all states
from the 'states' table where the name matches the given user input.

Usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>

The results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def list_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL database and prints all states with
    the specified name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database to connect to.
        state_name (str): State name to filter by.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
