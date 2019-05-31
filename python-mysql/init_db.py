"""
Used to initialize example db and table
"""
import mysql.connector


def init_db():
    """
    create db, table and insert some example
    """
    # connect to db
    local_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456"
    )
    local_cursor = local_db.cursor()
    # create db users
    local_cursor.execute("CREATE DATABASE users")
    # connect to specified db
    user_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database="users"
    )
    user_cursor = user_db.cursor()
    # create table userinfo
    user_cursor.execute("CREATE TABLE userinfo (name VARCHAR(255), address VARCHAR(255))")
    # insert example
    sql = "INSERT INTO userinfo (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    user_cursor.execute(sql, val)
    user_db.commit()


if __name__ == "__main__":
    init_db()
