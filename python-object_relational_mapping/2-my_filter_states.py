#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the user input.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cur = db.cursor()

    # Create SQL query using format (as required)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute query
    cur.execute(query)

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connection
    cur.close()
    db.close()
