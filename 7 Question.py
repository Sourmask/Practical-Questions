'''
Write a program using separate functions to perform the following
(i) To open a file named “apple.txt” and store the following in separate lines
“Boxing rings are square
Actions speak louder than words
Neither apple nor pine are in pineapple
Overlook and oversee are opposites
An alarm goes off by going on.”
(ii)To display all the lines that start with letter A.
(iii)To read the content of the file and display all lines which are more than 5 words in it 
'''


def add():
    lst=["Boxing rings are square",
        "Actions speak louder than words",
        "Neither apple nor pine are in pineapple",
        "Overlook and oversee are opposites",
        "An alarm goes off by going on."]

    with open("apple.txt","w") as f:
        for i in lst:
            f.write(i+'\n')

def startA():
    with open("apple.txt","r") as f:
        para=f.readlines()
        for line in para:
            for word in line:
                if word[0]=="A":
                    print(line)

def plus5():
    with open("apple.txt","r") as f:
        para=f.readlines()
        for line in para:
                original=line
                line=line.split()
                if len(line)>5:
                    print(original)

add()
startA()
print("---------------------")
plus5()