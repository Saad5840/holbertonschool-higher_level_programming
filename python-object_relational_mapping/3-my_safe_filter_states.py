#!/usr/bin/python3
"""
This script takes 4 arguments: mysql username, mysql password,
database name, and a state name to search for in the `states` table.
It connects to the MySQL database using MySQLdb, safely queries for
states with the given name using parameterized queries to prevent SQL injection,
and prints the results sorted by states.id in ascending order.
"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
