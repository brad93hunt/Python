#!/usr/bin/env python
#
# Level 2 - Question 10
#
# Question:
# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def main():
    # user_input = [sorted(word.split()) for word in raw_input('Please enter a line of words separated by spaces: ')]

    user_input = raw_input('Please enter a line of words separated by spaces: ')
    unique = sorted(set(user_input.split()))

    print unique


if __name__ == '__main__':
    main()
