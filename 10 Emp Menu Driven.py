'''
3. A binary file "Employee.dat" maintains the details of employees in a company

which has structure [Empno, Empname, Department, Salary]

Write a menu driven program to perform the following
(i) Function AppendRecord() to append Employee's details into the binary file
(ii)Function AvgSalary() which accepts the department as parameter and find the average salary of all employees in that department
'''
import pickle

# To append N number of employees into the file
def AppendRecord():
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

# To search a deptartment and get average
def AvgSalary(dept):                                      
    with open("employee.dat","rb") as f:
        sum=0                                             
        length=0                                          
        while True:                                       
            try:                                     
                data=pickle.load(f)                        
                if data[2]==dept:                         
                    sum+=data[3]
                    length+=1
            except:
                break 
        avg=sum/length                                    
        print(avg)
    menu()                                                

# Main
def menu():
    print("1 - Add Employee Data")
    print("2 - Get Average Salary")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        AppendRecord()
    elif task==2:
        dept=input("Enter Department: ")
        AvgSalary(dept)
menu()
