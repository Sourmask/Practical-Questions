'''
Write a menu driven program to perform the operations in a stack containing integer values 
(Write separate functions for PUSH), POP() and DISPLAY()
'''

# AI GENERATED (i was too lazy)

stack=[]

def push():
    if len(stack)==n:
        print("Stack is full!")
    else:
        element=int(input("Enter the element:"))
        stack.append(element)
        print(stack)

def pop():
    if len(stack)==0:
        print("Stack is empty!")
    else:
        e=stack.pop()
        print("Removed element:",e)
        print(stack)

def display():
    print(stack)

n=int(input("Enter the size of the stack"))
while True:
    print("Select the operation 1.push 2.pop 3.display 4.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct operation")