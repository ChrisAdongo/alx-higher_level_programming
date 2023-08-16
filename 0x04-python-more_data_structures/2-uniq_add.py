#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""

    uniq_list = set(my_list)
    k = 0

    for i in uniq_list:
        k += i

    return (k)
