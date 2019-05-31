"""
multiple thread, single connection
"""
import threading
import mysql.connector

USER_DB = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="users"
    )
USER_CURSOR = USER_DB.cursor()


def read_user_from_db():
    """
    read user info from db
    """
    USER_CURSOR.execute("select * from userinfo")
    return USER_CURSOR.fetchall()


if __name__ == "__main__":
    threads = []
    for i in xrange(1000):
        t = threading.Thread(target=read_user_from_db)
        t.daemon = True
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    