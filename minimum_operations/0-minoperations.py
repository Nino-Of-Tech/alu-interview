#!/usr/bin/python3

"""
Module documentation
"""


def minOperations(n):
    """
    This function calculates the fewest number
    of operations needed to give the result n H characters in the selected file.
    """

    # Assign the variables
    operations = 0   # number of operations performed
    copied = 0       # number of H characters copied
    pasted = 1       # number of H characters in file

    while pasted < n:
        if copied == 0:
            copied = pasted
            operations += 1
        elif pasted == 1:
            pasted += copied
            operations += 1
        else:
            remaining = n - pasted
            if remaining < copied:
                return 0
            if remaining % pasted != 0:
                pasted += copied
                operations += 1
            else:
                copied = pasted
                pasted += copied
                operations += 2

    return operations if pasted == n else 0
