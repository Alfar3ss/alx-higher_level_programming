#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add all unique integers in a list (each integer only once)."""
    unique_integers = set()
    
    for num in my_list:
        unique_integers.add(num)
    
    sum_unique = sum(unique_integers)
    
    return sum_unique
