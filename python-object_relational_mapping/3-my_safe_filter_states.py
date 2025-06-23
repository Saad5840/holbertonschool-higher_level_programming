#!/usr/bin/python3
"""
This module connects to a MySQL database and safely lists all states
from the 'states' table where the name matches the given user input.

It prevents SQL injection by using parameterized queries.

Usage:
    ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>

Results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def list_states_safe(username, password, database, state_name):
    """
    Connects to the MySQL database and prints all states
    with the specified name safely using parameterized queries.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_safe(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
