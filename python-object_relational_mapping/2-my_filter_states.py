#!/usr/bin/python3
"""
Lists all states where name matches the user input from the database hbtn_0e_0_usa.

This script uses MySQLdb and receives MySQL credentials and the state name as arguments.
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, dbname, statename):
    """
    Connects to the MySQL database and lists states that match a specific name.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        dbname (str): MySQL database name
        statename (str): Name of the state to match
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=dbname
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(statename)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
