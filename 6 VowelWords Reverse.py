'''
Write a program that inputs a paragraph of text and store it into a text file “notes1.txt” , and perform 
the following using separate functions
 (i) vowelwords(), that reads the file and display all the words that are starting with a lowercase vowel 
 (i.e. 'a', 'e', 'i', 'o','u'). 
 (ii) Reverse(), To read from the file and display all the words in reverse order.
'''
str=input()
with open("notes1.txt","w") as f:
    f.write(str)

def vowelwords():
    with open("notes1.txt","r") as f:
        data=f.read()
        data=data.split()
        for i in data:
            if i[0] in ('a', 'e', 'i', 'o','u'):
                print(i)

def Reverse():
    with open("notes1.txt","r") as f:
        data=f.read()
        data=data.split()
        for i in range(len(data)-1,-1,-1):
            print(data[i])

Reverse()
        