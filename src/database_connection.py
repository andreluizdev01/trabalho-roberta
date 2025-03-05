import mysql.connector

def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Substitua pelo seu usuário do MySQL
        password="",  # Substitua pela sua senha do MySQL
        database="OficinaMecanica2"
    )
    return conn