#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    conn.close()
