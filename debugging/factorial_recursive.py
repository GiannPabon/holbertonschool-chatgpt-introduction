#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
        n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the input number n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input number from the command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the calculated factorial
print(f)

