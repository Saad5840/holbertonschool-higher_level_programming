#!/usr/bin/python3
"""
This script safely lists all states from the database hbtn_0e_0_usa
where the name matches the user input. It uses parameterized queries
to prevent SQL injection vulnerabilities.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main execution block that connects to the database and executes
    a safe parameterized query to find matching states.
    """
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        cur = db.cursor()

        # Safe parameterized query
        query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
