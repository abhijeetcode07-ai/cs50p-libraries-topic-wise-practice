# Question 6:
# Take ONE number from the command line using sys.argv.
# Print the square of that number.
#
# Example:
# python square.py 5
# Output:
# Square is: 25
#
# Conditions:
# - Use sys.argv
# - If no argument -> Too few arguments
# - If more than one argument -> Too many arguments
# - Convert the argument to integer before calculation

import sys

if len(sys.argv) < 2 :
    sys.exit("too few arguments")

elif len(sys.argv) > 2 :
    sys.exit("too many arguments")

square = pow(int(sys.argv[1]),2)
print(f"Square is : {square}")