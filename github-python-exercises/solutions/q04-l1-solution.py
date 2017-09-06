#!/usr/bin/python
#
# Level 1 - Question 4
#
# Write a program which accepts a sequence of comma-separated numbers from console
# and generate a list and a tuple which contains every number.
#
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def main():
    # Prompt user for input
    user_input = raw_input("Please enter a list of numbers: ")

    # Split user_input string by comma and put into list
    user_list = user_input.split(',')

    # Store list as a tuple in new variable
    user_tuple = tuple(user_list)

    # Print list and tuple
    print user_list, '\n', user_tuple

if __name__ == '__main__':
    main()
