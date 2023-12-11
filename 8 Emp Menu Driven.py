'''
Write a menu driven program to perform Employee related operations performed in a company 
 using a binary file “Employee.dat”. (Details of employees are represented in a LIST which 
 contains Empno, Empname, Department, Salary) 
 Write following functions 
(i) Append an Employee's details into the binary file 
(ii) To search an employee for a given employee number 
'''

import pickle

# To append N number of employees into the file
def append():
    N=int(input("Enter no. of employees to enter: ")) 
    with open("employee.dat","ab") as f:                  
        for i in range(N):                                
            empno=int(input("Empno: ")) 
            empname=input("Empname: ")
            dept=input("Department: ")
            sal=int(input("Salary: "))
            data=[empno,empname,dept,sal]                 
            pickle.dump(data,f)                           
    print("-- Success --")
    menu()                                                

# To search an employee from the file and display all data of that person.
def search():
    empno=int(input("Empno: "))                           
    with open("employee.dat","rb") as f:                  
        while True:                                       
            data=pickle.load(f)                           
            if data[0]==empno:                            
                print(data)                               
                break                                     
    menu()                                                

# Main
def menu():
    print("1 - Add Employee Data")
    print("2 - Search Employee Data")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        append()
    elif task==2:
        search()
menu()