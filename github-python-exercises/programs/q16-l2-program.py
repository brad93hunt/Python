#!/usr/bin/env python
#
# Question 16 - Level 2
#
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

def main():
    user_input = input('Please enter a string of comma-separated numbers: ')
    user_input = user_input.split(',')

    square_int = [int(i) * int(i) for i in user_input if int(i) % 2 != 0]

    print (square_int)

if __name__ == '__main__':
    main()
