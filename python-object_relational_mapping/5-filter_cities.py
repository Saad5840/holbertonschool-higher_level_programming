#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.

Takes 4 arguments: mysql username, mysql password, database name, and state name.
Uses parameterized query to prevent SQL injection.
Results sorted by cities.id in ascending order.
"""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 5:
        return

    user, passwd, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db_name, charset="utf8")
    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    print(", ".join([city[0] for city in results]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
