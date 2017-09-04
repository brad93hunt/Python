#!/usr/bin/python
#
# Level 1 - Question 5
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

def get_string():
    # Prompt user for input
    user_input = raw_input('Please enter a string: ')

    # Return user_input to main()
    return user_input

def print_string(user_input):
    # Print user_input in upper case
    print user_input.upper()

def main():
    # Call get_string function to read in string from user
    user_input = get_string()

    # Call print_string function to print user_input in upper case
    print_string(user_input)

if __name__ == '__main__':
    main()
