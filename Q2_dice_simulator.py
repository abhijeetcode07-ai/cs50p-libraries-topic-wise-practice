# Question:
# Create a dice simulator.
# Keep rolling the dice (1–6) when the user presses Enter.
# Stop the program when the user types "q".

import random

while True:
    user = input("Press Enter to roll dice (q to quit): ").lower()

    if user == "q":
        print("Goodbye!")
        break

    elif user == "":
        roll = random.randint(1, 6)
        print(f"You rolled: {roll}")

    else:
        print("Invalid input")
