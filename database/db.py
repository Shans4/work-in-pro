import sqlite3


def connect(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor  # (connection, cursor)
