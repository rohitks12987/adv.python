import mysql.connector as myconn
from mysql.connector import Error

HOST = "localhost"
USER = "root"
PASSWORD = "root"
DATABASE = "mydb"


def create_database_if_missing():
    setup_conn = myconn.connect(host=HOST, user=USER, password=PASSWORD)
    setup_cursor = setup_conn.cursor()
    setup_cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DATABASE}`")
    setup_cursor.close()
    setup_conn.close()


def main():
    mydb = None
    db_cursor = None
    try:
        create_database_if_missing()
        mydb = myconn.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
        print("Connection successful!")

        db_cursor = mydb.cursor()
        db_cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))"
        )
        print("Table created successfully!")

        name = input("Enter name: ")
        email = input("Enter email: ")
        db_cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mydb.commit()
        print("Data inserted successfully!")

        db_cursor.execute("SELECT * FROM users")
        rows = db_cursor.fetchall()
        for row in rows:
            print(row)
            print(row[1])
            print(row[2])
            print(row[0])
    except Error as err:
        print(f"MySQL error: {err}")
    finally:
        if db_cursor is not None:
            db_cursor.close()
        if mydb is not None and mydb.is_connected():
            mydb.close()


if __name__ == "__main__":
    main()

