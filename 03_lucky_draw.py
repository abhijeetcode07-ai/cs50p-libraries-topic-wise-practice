# Question:
# Take comma-separated names from the user.
# Randomly select TWO different winners (no duplicates allowed).
# Use random.sample().

import random 


list = input("Enter the names you want seperated by the comma : ").split(",") 

winner1,winner2 = random.sample(list,2) 

print(f"Winner 1 is : {winner1}") 
print(f"Winner 2 is : {winner2}")