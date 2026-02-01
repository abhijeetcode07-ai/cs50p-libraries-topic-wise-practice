# Question 5:
# Take TWO numbers from command line arguments using sys.argv.
# Print their sum.
# If too few arguments -> Too few arguments
# If too many arguments -> Too many arguments

import sys

if len(sys.argv) < 3 :
    sys.exit("too few arguments")

elif len(sys.argv) > 3 :
    sys.exit("too many arguments")

print(f"Sum is : {int(sys.argv[1]) + int(sys.argv[2])}")