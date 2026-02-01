# Question:
# Take a name from the command line using sys.argv.
# Print "Hello, <name>".
# If no argument -> Too few arguments
# If more than one -> Too many arguments

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print(f"Hello, {sys.argv[1]}")
