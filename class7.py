# Functions - def keyword
import os

# x and y are positional arguments
def add(x, y):
    """Method to Add numbers."""
    print('Adding numbers:', x, y)
    _sum = x + y
    return _sum


def substract(x, y):
    """Method for substracting numbers."""
    print('Substracting numbers:', x, y)
    if x > y:
        return x / y
    elif y > x:
        return y / x
    else:
        return 0


def multiply(x, y):
    """Multiply two numbers."""
    print('Multiplying numbers:', x, y)
    return x * y


def division(x, y):
    """Division of numbers.

    Note: If you don't return anything from a function then the function returns None by default
    """
    if (y == 0) or (x != 0):
        print('Cannot divide by Zero')
        return None
    else:
        return x / y
"and - True and True"
'or - True or False'
"or not"

# result = division(9, 1)
# print(result)


# Assignment operator : =
# Conditional check : ==
# print([1,2,3,5] == [1,2,3])  # case sensitive


x = 2
y = 1

if (y == 0) or (x == 1) and (x == y):
    print('Value of y is 0 and Value of x is 1')

"""
x	    y	    AND	    OR
TRUE	TRUE	TRUE	TRUE
FALSE	TRUE	FALSE	TRUE
TRUE	FALSE	FALSE	TRUE
FALSE	FALSE	FALSE	FALSE
"""

