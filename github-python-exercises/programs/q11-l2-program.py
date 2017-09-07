#!/usr/bin/env python
#
# Question 11 - Level 2
#
# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

def main():
    # Prompt user for input
    #user_input = raw_input('Please enter a series of comma separated binary numbers: ').split(',')

    # Print result of test if i % 5 == 0
    #print [i for i in user_input if int(i,2) % 5 == 0]

    print [i for i in raw_input('Please enter a series of comma separated binary numbers: ').split(',') if int(i,2) % 5 == 0]

if __name__ == '__main__':
    main()
