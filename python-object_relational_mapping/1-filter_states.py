#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.

Uses MySQLdb to connect to a MySQL database and execute the query.
"""

import MySQLdb
import sys


def filter_states_starting_with_N(username, password, dbname):
    """
    Connects to the MySQL database and lists all states starting with 'N'.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        dbname (str): MySQL database name
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=dbname
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states_starting_with_N(sys.argv[1], sys.argv[2], sys.argv[3])
