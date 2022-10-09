#!/usr/bin/python3

"""takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ = '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], port=3306,
                         password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cmd = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name=%s
          ORDER BY cities.id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    allcities = cur.fetchall()
    print(", ".join[city[0] for city in allcities]))

    cur.close()
    db.close()
    
