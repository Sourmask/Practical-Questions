'''
Write a program that input a list of 'n' integers and using separate user defined 
functions to perform the following operations based on this list.
 ● Traverse the content of the list and push the odd numbers into a stack.
 ● Pop and display the content of the stack.

'''

# AI GENERATED (i was too lazy)

stack = []
L=[]

def push_odd_numbers(lst,stack):
    for num in lst:
        if num%2!=0:
            stack.append(num)

def pop_and_display(stack):
    while len(stack)>0:
        print(stack.pop())

list_limit=int(input())
for i in range(list_limit):
    list_item=input()
    L.append(list_item)
push_odd_numbers(L, stack)
pop_and_display(stack)
