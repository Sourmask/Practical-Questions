'''
Write a program that inputs a list of 'N' integers and perform the following using separate functions 
 (i) To find the minimum and maximum elements in the list. Function name : Min_Max() 
 (Do not use min() of max() functions) 
 (ii)Function Rotate_right () that shifts the contents of each cell one place to the right, 
 except for the contents of the last cell, which should be moved into the cell with subscript 0. 
 Eg:Given a List with following elements: 5 -8 15 20 -6 10 -25 35 -50 19 
 The resultant List should look like: 19 5 -8 15 20 -6 10 -25 35 -50 
'''

def minmax(L):
    max=min=L[0]
    for i in L:
        if i>max:
            max=i
        elif i<min:
            min=i
    print("MAX ",max)
    print("MIN ",min)


def rotateright(L):
    print(L)
    last=L[len(L)-1]
    for i in range(len(L)-1,0,-1):
        L[i]=L[i-1]
    L[0]=last
    print(L)

L=[1,2,3,4,5,6,7,8,9,10]
rotateright(L)
minmax(L)
