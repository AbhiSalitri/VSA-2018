# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions her

# print "Hi, my name is Abhi."
# name = raw_input("What is your name?")
# name = name[0].upper() + name[1:].lower()
# grade = str(raw_input("What grade are you in?"))
# grade = grade[0]
# time = 12 - int(grade)
# print name, "you will graduate from high school in " + str(time) + " years."

current_month = 6
current_day = 11

month = raw_input("What month were you born in? (use the number)")
day = raw_input("What day were you born on?")

if month >= current_month:

   month1 = 12 -(month - current_month)
else:
    day >= current_day
    day1 = 12 -(day - current_day)
