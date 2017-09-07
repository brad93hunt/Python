#!/usr/bin/env python
#
# Question 12 - Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def main():
    # Print number for each number in the range of 1000 - 3000 if num % 2 == 0
    print [i for i in range(1000,3001) if i % 2 == 0]

if __name__ == '__name__':
    main()
