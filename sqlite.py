import sqlite3
## connect the sqlite
connection=sqlite3.connect("Student.db")
cursor=connection.cursor()

## create the table
table_info="""
    create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)


## insert records into table
cursor.execute('''Insert Into STUDENT values('krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ram','Data Science','A',80)''')
cursor.execute('''Insert Into STUDENT values('Ganesh','Data Science','A',35)''')
cursor.execute('''Insert Into STUDENT values('Shankar','Devops','A',60)''')
cursor.execute('''Insert Into STUDENT values('Lakshmi','Devops','A',20)''')
cursor.execute('''Insert Into STUDENT values('Radha','Devops','A',45)''')

## display all records
print("the inserted records are: ")
data=cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

## commit changes
connection.commit()
connection.close()