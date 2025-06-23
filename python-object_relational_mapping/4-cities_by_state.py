#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
with their corresponding state name.

Takes 3 arguments: mysql username, mysql password, database name.
Connects to localhost MySQL server on port 3306,
queries cities joined with states, sorted by cities.id ascending,
and prints each city as (city_id, city_name, state_name).
"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        return

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name, charset="utf8")
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
