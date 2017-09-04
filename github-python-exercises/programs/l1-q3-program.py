#!/usr/bin/python
#
# Level 1 - Question 3
#
# Question:
# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
#
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def main():
    # Prompt user to enter a number
    user_input = int(raw_input('Pleae enter a number: '))

    # Generate list of range x, where x is user_input
    user_range = range(1, user_input + 1)

    power = []
    # Loop through each num in user_range, find num*num, and store result in power
    for num in user_range:
        power.append(num*num)

    print zip(user_range, power)

if __name__ == '__main__':
    main()
