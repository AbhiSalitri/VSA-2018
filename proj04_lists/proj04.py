# coding=utf-8
# Name:
# Date:

"""
proj04

practice with lists

"""

#Part I
#Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

random_list = [1,5,7,2,4,11,13,10,9]

#for item in random_list:
    #if item < 5:
        #print item




#Part II
# Take two lists, say for example these two:
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that creates and prints a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

#for numbers in c:
    #if numbers == numbers in b:
        #print numbers





#Part III
# Take a list, say for example this one:

d = ["b", "a", "f", "y", "a", "t", "_", "p", "a", "R"]
# and write a program that replaces all “a” with “*”.

#counter = 0
#for numbers in d:
    #old_name = "a"
    #new_name = "*"
    #if  numbers == old_name:
        #d[counter] = new_name
    #counter = counter + 1
#print d







#Part IV
#Ask the user for a string, and print out whether this string is a palindrome or not.

empty_list = []
string = raw_input("Type a string in the space provided, to determine wheather or not it is a palindrome.")
for letters in string:
    empty_list.append(letters)
if string[0] == string[-1]:
    print "Your string is a palindrome!"
if string[0] != string[-1]:
    print "Your string is not a palindrome."










