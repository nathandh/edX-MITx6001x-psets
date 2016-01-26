# Problem Set1 #2 MITx 6.00.1x offered on edX.org
# @nathandh - Implemented 01.25.2016
'''
COUNTING BOBS  (15/15 points)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print:

    Number of times bob occurs is: 2

For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.
'''

# Remove 's' declaration before submitting for testing
s='azcbobobegghakl'

count = 0
length = len(s)
find_text = "bob"
index = 0

while index != length:
    match_index = s.find(find_text, index, length)
    if match_index != -1:
        count += 1
        index = match_index + 1

    index += 1

print "Number of times bob occurs is: ", count
