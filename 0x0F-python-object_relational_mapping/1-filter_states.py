#!/usr/bin/python3
""" Lists all states with a name starting with N from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()

        
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()

        
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
