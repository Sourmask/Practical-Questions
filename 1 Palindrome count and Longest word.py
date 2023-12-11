# WAF to count palindrome in a string
# Also WAF to count the longest string

# Defining a funtion to count the palindrome words occuring in the string
def palindromecount(str):
    count=0
    L=str.split() # To split the str word by word and store in a list
    for i in L: # ['Madam', 'and', 'her', 'mom', 'speak', 'Malayalam' .... 
        str_rev='' 
        for j in range(len(i)-1,-1,-1): # To revese the word
            str_rev+=i[j]
        if str_rev==i: # To check in rev is equal to actual
            count+=1
    return count 

# Defining a funtion to find the longest word
def longest(str):
    L=str.split() # To split the str word by word and store in a list
    longest=L[0] # To start off by making the first as longest to later compare with other words
    for i in L:
        if len(i)>len(longest): # To compare the lenght of the string with the longest and likewise
            longest=i 
    return longest

# Main
str="madam and her mom speak Malayalam and they refer to civic related topics"
print("No. of palindrome: ",palindromecount(str))
print("Longest string:",longest(str))