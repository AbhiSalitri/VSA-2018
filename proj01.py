# Name:
# Date:
#
# proj01: A Simple Program
#
# Part I:
# This program asks the user for his/her name and grade.
# Then, it prints out a sentence that says the number of years until they graduate.
#
# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday
#
#
# If you complete extensions, describe your extensions her

print "Hi, my name is Abhi."
name = raw_input("What is your name?")
name = name[0].upper() + name[1:].lower()
grade = str(raw_input("What grade are you in? (use the number)"))
time = 12 - int(grade)
print name,",you will graduate from high school in " + str(time) + " years."

current_month = 6
current_day = 12

month = raw_input("What month were you born in?")
month = month[0].upper() + month[1:].lower()
day = raw_input("What day were you born on?")
if month == "January":
    month = 1
elif month == "February":
    month = 2
elif month == "March":
    month = 3
elif month == "April":
    month = 4
elif month == "May":
    month = 5
elif month == "June":
    month = 6
elif month == "July":
    month = 7
elif month == "August":
    month = 8
elif month == "September":
    month = 9
elif month == "October":
    month = 10
elif month == "November":
    month = 11
else:
    month = int(12)
if int(month) >= current_month:
   month1 = (int(month) - int(current_month))

else:
    month1 = int(12 - (int(current_month) - int(month)))
if int(day) >= current_day:
    day1 = (int(day) - int(current_day))
else:
    day1 = int(30 - (int(current_day) - int(day)))
    if month1 == 0:
        month1 = 11
    else:
        month1 = month1 - 1
print str(name) + ",your birthday will be in " + str(month1) + " months and " + str(day1) + " days."