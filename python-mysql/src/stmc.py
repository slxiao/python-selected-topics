"""
single thread, multiple connections
"""
import mysql.connector


def read_user_from_db():
    """
    read user info from db
    """
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
    for i in xrange(1000):
        read_user_from_db()
