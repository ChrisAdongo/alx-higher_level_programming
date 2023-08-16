#!/usr/bin/python3

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>)"""
    
    if not my_list:
        return (0)

    weighted_sum = sum(x * y for x, y in my_list)
    total_weights = sum(y for _, y in my_list)

    return (weighted_sum / total_weights)
