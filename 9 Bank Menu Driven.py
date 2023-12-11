'''
Write a menu driven program to perform the operations of n customers in a Bank using binary
file "BANK.dat". 

Details of customers are to be stored in a list which contains
AccNo : Store account number of a customer
AccName: Store name of account holder
BalanceAmt : Balance amount in Bank

Write following functions
(i) StoreData(): To append a Customer's details into the binary file (N customers)
(ii) SearchName(): A function to search for a customer based on a given customer name
'''

import pickle

# To append N number of customers into the file
def StoreData():
    N=int(input("Enter no. of customers to enter: ")) 
    with open("bank.dat","ab") as f:                  
        for i in range(N):                            
            AccNo=int(input("AccNo: ")) 
            AccName=input("AccName: ")
            BalanceAmt=int(input("BalanceAmt: "))
            data=[AccNo,AccName,BalanceAmt]           
            pickle.dump(data,f)                       
    print("-- Success --")
    menu()                                            

# To search a customer from the file and display all data of that person.
def SearchName():
    AccName=int(input("AccName: "))                   
    with open("bank.dat","rb") as f:                  
        while True:                                   
            data=pickle.load(f)                       
            if data[1]==AccName:                      
                print(data)                           
                break                                 
    menu()                                            

# Main
def menu():
    print("1 - Add Data")
    print("2 - Search Data")
    print("3 - Exit")
    task=int(input("Enter task no. to perform"))
    if task==1:
        StoreData()
    elif task==2:
        SearchName()
menu()