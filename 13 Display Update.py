'''
Write a python program to perform the following in MySql using python Interface.
Using separate functions (Database name :School)
 (i) To display all the records of all the students for the given class.(class is user input)
 
 (ii) To update the table by editing the Marks for the given rollno. (rollno and marks are user input)
'''

import mysql.connector as sql
SQLconnection=sql.connect(host='localhost',user='root',passwd="1234",database="School")
cr=SQLconnection.cursor()

def display():
    classs=input()
    cr.execute(f"SELECT * FROM SCHOOL WHERE CLASS={classs}")
    data=cr.fetchall()
    print(data)

def update():
    roll=int(input())
    marks=float(input())
    cr.execute(f"UPDATE Student SET MARKS={marks} WHERE rollno={roll}")
    