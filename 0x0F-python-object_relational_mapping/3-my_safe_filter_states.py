#!/usr/bin/python3
"""
a script that lists selected states
"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Establish database connection
    connection = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306
    )

    # Create cursor
    cursor = connection.cursor()

    # Define SQL query with placeholder for state
    query = ("SELECT * FROM states WHERE name LIKE BINARY"
             "%s ORDER BY states.id ASC")

    # Execute SQL query with parameter
    cursor.execute(query, (sys.argv[4],))

    # Fetch
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()
