# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""

previous_number = 0
current_number = 1
next_number = 1

x = int(raw_input("How many Fibonacci numbers would you like to generate?"))
for number in range (0, x):
    print current_number
    next_number = previous_number + current_number
    previous_number = current_number
    current_number = next_number
