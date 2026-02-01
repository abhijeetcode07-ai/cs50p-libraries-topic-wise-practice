 # -------------------------------------------
# Question 10 – Current Time Formatter ⏰
# -------------------------------------------
#
# Write a Python program that:
#
# 1. Imports the datetime module
# 2. Gets the current date and time
# 3. Prints the current time in this format:
#
# Current time: 01-02-2026 14:35:20
#
# Requirements:
# - Use datetime.datetime.now()
# - Use strftime() to format the output
# - Format must be: DD-MM-YYYY HH:MM:SS
# - Use 24-hour time
# - Leading zeros must appear (05 not 5)
# - Do NOT hardcode anything
#
# Example output:
# Current time: 05-01-2026 09:03:07
# -------------------------------------------


import datetime

current_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print("CUURENT TIME : ",current_time)