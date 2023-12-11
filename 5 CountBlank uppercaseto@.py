'''
Write a program that inputs a line of text and store it into a text file “story1.txt”, and perform the 
following using separate functions
(i) Countblanks( )- To read the content from a text file STORY.TXT, count and display the 
number of blank spaces present in it.
 (ii) Display() -To read the content and display the text in such a way that all upper case letters 
 are replaced with a symbol '@'. 
 
 Example: If the file TOPIC.TXT has the following content :
 Education is The Most Powerful Weapon which You can use to Change the World
 Output for Countblanks() : No. of blank spaces : 13
 Output for Display():
 @ducation is @he @ost @owerful @eapon which @ou can use to @hange the @orld
'''

str=input()
with open("story1.txt","w") as f:
    f.write(str)

def Countblanks():
    count=0
    with open("story1.txt","r") as f:
        data=f.readline()
        for i in data:
            if i==" ":
                count+=1
    print(count)

def Display():
    final=""
    with open("story1.txt","r") as f:
        data=f.readline()
        for i in data:
            if i.isupper():
                final+="@"
            else:
                final+=i
    print(final)
