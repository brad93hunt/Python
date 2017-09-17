#!/usr/bin/env python
# coding: utf-8
#
# Question 15 - Level 2
#
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def main():
    user_input = int(input('Please enter a number: '))

    print (user_input + (user_input * 11) + (user_input * 111) + (user_input * 1111))

if __name__ == '__main__':
    main()
