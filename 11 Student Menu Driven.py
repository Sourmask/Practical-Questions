'''
A CSV file student.csv maintains the details of students (Name, class, Year, Percent). Write 
 functions to perform the following using separate functions
 (i) Append() -To input the details of students and store it into the csv file
 (ii)To search and display the record of a given name of student from the csv file 
'''

import csv

def append(N):
    with open("student.csv","w",newline="") as f:
        csvv=csv.writer(f,delimiter=",")    
        for i in range(N):
            name=input()
            classs=input()
            year=input()
            percent=input()
            data=[name,classs,year,percent]
            csvv.writerow(data)
    menu()  

def search():
    name=input
    with open("student.csv","r") as f:
        csvv=csv.reader(f,delimiter=",")
        for i in csvv:
            if i[0]==name:
                print(i)
    menu()  

# Main
def menu():
    print("1 - Add Data")
    print("2 - Search Data")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        N=int(input())
        append(N)
    elif task==2:
        search()
menu()  