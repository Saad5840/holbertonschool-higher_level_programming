#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
where the name matches the user input.
It safely handles user input to prevent SQL injection.
"""
import MySQLdb
import sys


def main():
    """
    Main function that connects to the database and executes the query.
    Takes 4 command line arguments:
    - MySQL username
    - MySQL password
    - Database name
    - State name to search for
    """
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        return

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
            db=db_name,
            charset="utf8"
        )

        # Create cursor to execute queries
        cursor = db.cursor()

        # Execute parameterized query to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    main()
