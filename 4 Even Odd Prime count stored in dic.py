# WAP to input list of integers and pass a function along with an empty dictionary
# Function should find no. of prime, no. of odd no. and even no. 
# Output should be in dic()
# Use seperate def to check
L=[]

# Defining a funtion to count the prime no. in list
def prime(L):
    count=0
    for i in L:
        for j in range(2,i+1):
            if i%j==0:
                break
            else:
                count+=1
                break
    return count

# Defining a funtion to count the even no. in list
def even(L):
    count=0
    for i in L:
        if i%2==0:
            count+=1
    return count
    
# Defining a funtion to count the odd no. in list
def odd(L):
    count=0
    for i in L:
        if i%2!=0:
            count+=1
    return count

# Adding items to the list
L=[]
list_limit=int(input("Enter limit:"))
for i in range(list_limit):
    list_item=int(input("Enter item:"))
    L.append(list_item)

# Main
D={}
D["Prime Count"]=prime(L)
D["Even Count"]=even(L)
D["Odd Count"]=odd(L)
print(D)