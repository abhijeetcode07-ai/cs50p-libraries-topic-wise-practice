# Question 7 — Password Attempts Limiter (sys + loops)
#
# Create a Python program that:
#
# 1. Stores a correct password inside the program.
# 2. Asks the user to enter the password continuously.
# 3. If the password is correct:
#       → print "Access granted"
#       → stop the program
# 4. If the password is wrong:
#       → increase attempt counter
# 5. If the user enters wrong password 3 times:
#       → exit the program using sys.exit()
#       → print "Too many attempts"
#
# Rules:
# - Use while loop
# - Use sys.exit()
# - Use attempt counter variable
# - Do NOT allow more than 3 tries

import sys

Correct_Password = "python123"
attempt = 0
while True :
    
    password = input("enter the password :  ")

    if password == Correct_Password :
        print("Access granted")
        break
    else :
        attempt += 1
        if attempt == 3 :
            sys.exit("too many attempt")

    
