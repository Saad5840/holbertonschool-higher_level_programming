#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa where name matches the argument,
using parameterized queries to prevent SQL injection.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Create cursor
        cur = db.cursor()

        # Execute parameterized query (safe from SQL injection)
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch and display results
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        # Close connections
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
