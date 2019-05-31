"""
multiple thread, connection pool
"""
import time
from random import uniform
from time import sleep
import threading

import mysql.connector
from mysql.connector.connection import MySQLConnection
from mysql.connector.pooling import MySQLConnectionPool as mcp
from mysql.connector import Error


CON_POOL = mcp(pool_name="mypool", pool_size=32, pool_reset_session=True,
                host='localhost', database='users', user='root', password='123456')


def read_user_from_db():
    """
    read user info from db
    """
    sleep(uniform(0, 1))
    while True:
        try:
            conn = CON_POOL.get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from userinfo")
            res = cursor.fetchall()
            conn.close()
            return
        except Error:
            pass
        

if __name__ == "__main__":
    threads = []
    for i in xrange(1000):
        t = threading.Thread(target=read_user_from_db)
        t.daemon = True
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
