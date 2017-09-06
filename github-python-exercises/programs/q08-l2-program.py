#!/usr/bin/env python
#
# Level 2 - Question 8
#
# Question:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def main():
    # Prompt user input
    user_input = raw_input('Please enter a set of comma-separated strings: ')

    # Split user_input by comma into a list of strings and sort alphabetically
    user_input = sorted(user_input.split(','))

    # Print user_input
    print ','.join(user_input)

if __name__ == '__main__':
    main()
