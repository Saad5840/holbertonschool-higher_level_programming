#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the given database.

Connects to a MySQL server on localhost at port 3306 using MySQLdb,
fetches states where the name starts with 'N', and prints them sorted
by states.id in ascending order.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N' ordered by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results and print each row
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
