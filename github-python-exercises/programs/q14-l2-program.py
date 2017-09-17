#!/usr/bin/env python
# coding: utf-8
#
# Question 14 - Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def main():
    user_input = input('Please enter a sentence: ')

    counters_dict = {'Upper':0, 'Lower':0}

    for c in user_input:
        if c.isupper():
            counters_dict['Upper'] += 1
        elif c.islower():
            counters_dict['Lower'] += 1
        else:
            pass

    print ('Upper: ', counters_dict['Upper'])
    print ('Lower: ', counters_dict['Lower'])

if __name__ == '__main__':
    main()
