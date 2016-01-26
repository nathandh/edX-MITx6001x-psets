# Problem Set1 #3
# - Part of the MITx 6.00.1x course offered on edX.org for Free!
# @nathandh - implemented 01/25/2016
#
''' 
PROBLEM 3: COUNTING AND GROUPING  (15/15 points)
A catering company has hired you to help with organizing and preparing customer's orders. You are given a list of each customer's desired items, and must write a program that will count the number of each items needed for the chefs to prepare. The items that a customer can order are: salad, hamburger, and water.

Write a function called item_order that takes as input a string named order. The string contains only words for the items the customer can order separated by one space. The function returns a string that counts the number of each item and consolidates them in the following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

If an order does not contain an item, then the count for that item is 0. Notice that each item is formatted as [name of the item][a colon symbol][count of the item] and all item groups are separated by a space.

For example:

If order = "salad water hamburger salad hamburger" then the function returns "salad:2 hamburger:2 water:1"
If order = "hamburger water hamburger" then the function returns "salad:0 hamburger:2 water:1"
'''

# Remove order definition before testing submission
order = "salad water hamburger salad hamburger"

def item_order(order):
    num_salads = 0
    num_hamburgers = 0
    num_waters = 0
    
    words = order.split()
    for word in words:
        if word == 'salad':
            num_salads += 1
        elif word == 'hamburger':
            num_hamburgers += 1
        elif word == 'water':
            num_waters += 1
        
    return "salad:"+str(num_salads)+" "+"hamburger:"+str(num_hamburgers)+ \
            " "+"water:"+str(num_waters)
    
output = item_order(order)
print output
