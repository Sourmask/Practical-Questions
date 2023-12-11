'''
Write a program that inputs a list of 'n' integers perform the following using separate functions. 
 (i) Function FindSum(L) that finds and return the sum of all elements in the even index of the given list.
 (ii)Function INDEX_LIST(L) returns another list named 'indexList' that stores the indices of all Non-Zero 
 elements of L. 
 For example: If L contains [12,4,0,11,0,56] 
The indexList will have - [0,1,3,5] 
'''
L=[12,4,0,11,0,56]
indexList=[]

def FindSum(L):
    sum=0
    for i in L:
        if i%2==0:
            sum+=i
    return sum

def INDEX_LIST(L):
    global indexList
    for i in range(len(L)):
        if L[i]!=0:
            indexList.append(i)
