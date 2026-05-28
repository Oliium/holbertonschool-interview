#!/usr/bin/python3
"""Compute the fewest Copy All / Paste steps to reach n H characters."""


def minOperations(n):
    """Return the minimum number of steps to obtain n H characters.

    The minimum is the sum of the prime factors of n.
    Returns 0 if n is impossible to achieve (n <= 1).
    """
    if n <= 1:
        return 0

    steps = 0
    diviseur = 2

    while n > 1:
        while n % diviseur == 0:
            steps += diviseur
            n = n // diviseur
        diviseur += 1
    return steps
