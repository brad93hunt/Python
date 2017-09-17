#!/usr/bin/env python
# Coding: utf-8
#
# Question 17 - Level 2
#
# Question:
# Write a program that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following:
# D 100
# W 200
# ¡­
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def main():
    user_input = input('Enter bank transaction: ')

    trans_list = []

    while user_input:
        trans_dict = tuple(filter(None, user_input.split()))
        trans_list.append(trans_dict)
        user_input = input('Enter bank transaction: ')

    balance = 0

    for trans_type, trans_amount in trans_list:
        if trans_type == 'D':
            balance = balance + int(trans_amount)
        elif trans_type == 'W':
            balance = balance - int(trans_amount)
        else:
            pass

    print ('Balance: ', balance)

if __name__ == '__main__':
    main()
