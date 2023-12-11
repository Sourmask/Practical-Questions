'''
Write a python program to perform the following in MySql using python Interface.
Using separate functions (Username : root, Password :1234Database name :School)
 
 (i) CreateStudent() -To create a table Student with Rollno (integer), Name(varchar(20), 
 class char(5),Marks decimal(7,2), DOB (date) are various columns of the table.

 (ii) AddRecord() -To insert the details of a student into the table Student
 (22, 'Kiran Raj','XII', 88.5, '2004-12-20')
'''
import mysql.connector as sql
SQLconnection=sql.connect(host='localhost',user='root',passwd="1234",database="School")
cr=SQLconnection.cursor()

def CreateStudent():
    try:
        cr.execute("CREATE TABLE Student(Rollno INT,Name VARCHAR(20),Class CHAR(5),Marks DECIMAL(7,2),DOB DATE)")
    except:
        print("Table already exists")

def AddRecord(): # Instructions Unclear
    data=(22, 'Kiran Raj','XII', 88.5, '2004-12-20')
    cr.execute(f"INSERT INTO STUDENT VALUES {data}")
    