#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given total."""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet total.

    Args:
        coins: list of the values of the coins in your possession.
        total: the amount to make up.

    Returns:
        The fewest number of coins needed to meet total, 0 if total is
        0 or less, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # dp[i] = fewest coins needed to make amount i float('inf') if unreachable
    dp = [0] + [float('inf')] * total
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
