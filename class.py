import mysql.connector as mycom
mydb=mycom.connect(host="localhost",user="root",password="root",database="Class_db")
db_cursor=mydb.cursor()

#print("Connection Created")

'''db_cursor.execute("create database Class_db")
print("Database Created")'''

'''db_cursor.execute("create table stu(id int,name varchar(20))")
print("Table Created")'''

'''db_cursor.execute("Create table teacher(id int,name varchar(20))")
print("Table created")'''

db_cursor.execute("show tables")
