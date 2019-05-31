"""
multiple thread, multiple connections
"""
import threading
import mysql.connector
from random import uniform
from time import sleep


def read_user_from_db():
    """
    read user info from db
    """
    sleep(uniform(0, 1))
    user_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="users"
    )
    user_cursor = user_db.cursor()
    user_cursor.execute("select * from userinfo")
    return user_cursor.fetchall()


if __name__ == "__main__":
    threads = []
    for i in xrange(1000):
        t = threading.Thread(target=read_user_from_db)
        t.daemon = True
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    