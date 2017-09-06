#!/usr/bin/python
#
# Level 1 - Question 2
#
# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def main():
    print 'This program will take an input number and calculate the factorial of that number.\n'
    # Prompt user to enter a number
    factorial = int(raw_input('Please enter a number: '))

    # Generate a range beginning with 1 and ending in the factorial
    f_range = range(factorial - 1, 0, -1)

    for num in f_range:
        factorial = factorial * num

    print 'Factorial result: ', factorial

if __name__ == '__main__':
    main()
