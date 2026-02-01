# -------------------------------------------
# Question 11 – Age Calculator
# -------------------------------------------
#
# Write a Python program that:
#
# 1. Takes user's birth year as input (integer)
# 2. Calculates the current age based on the current year
# 3. Prints the age in this format:
#
# You are 18 years old
#
# Requirements:
# - Use datetime module to get current year
# - No hardcoding of current year
# - Program should work correctly for any birth year input
#
# Hint:
# - Use datetime.datetime.now().year
#
# Example:
# Input: 2005
# Output: You are 18 years old
# -------------------------------------------


import datetime
import sys

try :
    birth_year = int(input("ENTER YOUR BIRTH YEAR : "))
except ValueError :
    sys.exit("INVALID INPUT, PLEASE TRY AGAIN")

current_year = datetime.datetime.now().year

print(f"YOUR AGE : {current_year-birth_year}")