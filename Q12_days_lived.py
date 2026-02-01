# -------------------------------------------
# Question 12 – Days Lived Calculator
# -------------------------------------------
#
# Write a Python program that:
#
# 1. Takes user's date of birth as input in this format:
#    DD-MM-YYYY
#
# 2. Calculates how many days the user has lived till today
#
# 3. Prints output like:
#
# You have lived 6574 days
#
# Requirements:
# - Use datetime module
# - Use datetime.datetime.strptime() to parse input
# - Use datetime.datetime.now() to get current date
# - Subtract two dates to get difference
# - Handle invalid input using try/except
#
# Example:
# Input: 01-01-2005
# Output: You have lived 7500 days
#
# Hint:
# - datetime difference gives timedelta
# - Use .days
# -------------------------------------------


import datetime
import sys

try :
    b_date = input("ENTER YOUR BIRTH DATE IN THIS FORMAT(DD-MM-YYYY) :  ")
    dob = datetime.datetime.strptime(b_date, "%d-%m-%Y")

except ValueError :
    sys.exit("INVALID FORMAT! PLEASE USE DD-MM-YYYY")

current_time = datetime.datetime.now()

diff = current_time - dob
print(F"YOU LIVED : {diff.days}")
