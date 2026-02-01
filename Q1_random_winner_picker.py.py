# Question:
# Take 5 names from the user and randomly select one winner
# using random.choice().

import random

names = []

for _ in range(5):
    name = input("Enter name: ")
    names.append(name)

winner = random.choice(names)

print(f"Winner is: {winner}")
