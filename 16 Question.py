'''
Write a program that stores the month names and number of days in each month into a dictionary in 
 the form of key value pairs. Program, with separate user defined functions to perform the 
 following operations:
 ● Push the keys (month names) of the dictionary into a stack, where the corresponding value 
 (no of days ) is 30.
 ● Pop and display the content of the stack.

'''

# AI GENERATED (i was too lazy)

months={
    "April":30,
    "June":30,
    "September":30,
    "November":30,
    "January":31
}

stack=[]

def push_to_stack(months,stack):
    for month,days in months.items():
        if days==30:
            stack.append(month)

def pop_and_display(stack):
    while len(stack)>0:
        print(stack.pop())

push_to_stack(months,stack)
pop_and_display(stack)
