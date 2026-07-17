#!/usr/bin/python3
"""Prime Game: determine the overall winner across several rounds."""


def isWinner(x, nums):
    """Return the player winning the most of x rounds.

    Each round starts with the set 1..n. Players alternately pick a
    prime and remove it and its multiples; the one unable to move loses.
    The winner of a round is decided by the parity of the number of
    primes <= n: odd -> Maria (first player), even -> Ben.
    """
    if x < 1 or not nums:
        return None

    n = max(nums)
    if n < 2:
        return "Ben"

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # prime_count[i] = number of primes <= i
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    maria = 0
    ben = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None
