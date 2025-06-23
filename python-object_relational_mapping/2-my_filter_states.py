#!/usr/bin/python3
"""
Lists all states with a name matching the user input from the database hbtn_0e_0_usa.
This script uses MySQLdb and a formatted SQL query.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Escape single quotes in the input to avoid syntax errors
    user_input = sys.argv[4].replace("'", "''")

    # Create query using format as required (NOT recommended in real-world apps)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(user_input)

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Cleanup
    cursor.close()
    db.close()
