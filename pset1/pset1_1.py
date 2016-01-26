# MITx 6.00.1.x as offered on edX.org
#Problem Set1 #1
# @nathandh - Implemented 01.25.2016
'''
COUNTING VOWELS  (10/10 points)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
'''

# Remove 's' declaration before testing for submission
s = 'azcbobobegghakl'

count = 0
length = len(s)
index = 0

while index != length:
    if s[index] == 'a':
        count += 1
    elif s[index] == 'e':
        count += 1
    elif s[index] == 'i':
        count += 1
    elif s[index] == 'o':
        count += 1
    elif s[index] == 'u':
        count += 1
    else:
        count = count
        
    index += 1

print "Number of vowels: ", count
