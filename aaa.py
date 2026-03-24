import mysql.connector as myconn
mydb = myconn.connect(host="localhost", user="root", password="root")
print("Connection established")
db_cursor = mydb.cursor()

#step1:create connection
   #print("Connection established")

#step2:create database
'''db_cursor.execute("CREATE DATABASE mydb")
print("Database created")'''

#step3:create table
'''db_cursor.execute("CREATE TABLE mydb.student (id INT, name VARCHAR(20), age INT)")
print("Table created")'''

#step4:show tables
'''db_cursor.execute("SHOW TABLES")
for x in db_cursor:
    print(x)'''


#step5:insert data
sql = "INSERT INTO mydb.student (id, name, age) VALUES (%s, %s, %s)"
val = (1, "John", 22)
db_cursor.execute(sql, val)
mydb.commit()
print("Data inserted")

#step6:read data inside table
db_cursor.execute("SELECT * FROM mydb.student")
myresult = db_cursor.fetchall()
for x in myresult:
    print(x)