#!/usr/bin/env python
# coding: utf-8
#
# Question 13 - Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def main():
    user_input = raw_input('Please enter a string of letters and numbers: ')

    letters = sum(c.isaplha() for c in user_input)
    numbers = sum(c.isdigit() for c in user_input)

    print 'Letters: ', letters
    print 'Numbers: ', numbers

if __name__ == '__main__':
    main()
