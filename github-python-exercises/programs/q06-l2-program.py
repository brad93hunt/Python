#!/usr/bin/env python
#
# Level 2 - Question 6
#
# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math

def main():
    C = 50
    H = 30

    # Read in user input
    user_input = raw_input('Please enter three comma-separated numbers: ')

    user_input_list = user_input.split(',')

    calc_result = []

    for num in user_input_list:
        D = int(num)
        Q = round(math.sqrt([(2 * C * float(D)/H)]))
        calc_result.append(Q)

    print calc_result


if __name__ == '__main__':
    main()
