#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """A function that finds all multiples of 2 in a list."""
    mult = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)

    return (mult)

