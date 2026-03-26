import mysql.connector as mycom
mydb=mycom.connect(host="localhost",user="root",password="root",database="Class_db")
db_cursor=mydb.cursor()

#print("Connection Created")

'''db_cursor.execute("create database Class_db")
print("Database Created")'''

'''db_cursor.execute("create table stu(id int,name varchar(20))")
print("Table Created")'''

'''db_cursor.execute("Create table teacher(id int,name varchar(20)) ")
print("Table Created")'''

'''db_cursor.execute("show tables")
for i in db_cursor:
    print(i)'''

'''db_cursor.execute("insert into stu(id,name)values(%s,%s)",(1,"Rahul")) 
print(db_cursor.rowcount,"data inserted")'''

'''db_cursor.execute("insert into teacher(id,name)values(%s,%s)",(1,"Ashish"))
print(db_cursor.rowcount,"data inserted")'''

'''db_insert="insert into stu(id,name)values(%s,%s)"
db_value=[(2,"Rohit"),(3,"Mrunal"),(4,"Jeetu "),(5,"Peter")]
db_cursor.executemany(db_insert,db_value)
mydb.commit()
print(db_cursor.rowcount,"data inserted")'''

'''db_insert="insert into Teacher(id,name)values(%s,%s)"
db_value=[(2,"Radha"),(3,"Rajeev"),(4,"Priya"),(5,"Sekhar")]
db_cursor.executemany(db_insert,db_value)
mydb.commit()
print(db_cursor.rowcount,"data inserted")'''

'''db_cursor.execute("select * from stu")
for i in db_cursor.fetchall():
    print(i)'''
db_cursor.execute("select * from teacher")
for i in db_cursor.fetchall():
    print(i)