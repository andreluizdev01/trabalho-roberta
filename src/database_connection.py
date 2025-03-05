import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="oficinamecanica2"
    )
    return conn
