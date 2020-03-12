"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Undefined Answer")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# question 1.
# = A ValueError will occur when a decimal value or any other characters besides numbers are entered

# question 2.
# A  ZeroDivisionError will occur when the program tries to divide the numerator by zero.

# question 3.
# set an if check that will print Undefined if the denominator is equal to zero

