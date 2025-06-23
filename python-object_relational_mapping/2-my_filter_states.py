#!/usr/bin/python3
"""
This script takes in 4 arguments (mysql username, password, database name,
and state name searched), connects to the MySQL database,
queries the states table for states matching the provided name,
and prints all matching states sorted by states.id.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Grab arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server on localhost
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password,
                         db=db_name, charset="utf8")

    cursor = db.cursor()

    # Use format() to build the query (vulnerable to injection, per task instruction)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
