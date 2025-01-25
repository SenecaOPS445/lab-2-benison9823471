#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign command-line arguments to variables
name = sys.argv[1]
age = int(sys.argv[2])

# Print the output in the required format
print(f"Hi {name}, you are {age} years old.")
