#!/usr/bin/python3
"""
Making change function
"""

from math import *


def makeChange(coins, total):
    coins.sort(reverse=True)
    count = 0
    length = len(coins)
    coins_copy = coins.copy()

    if total <= 0:
        return 0

    for i in range(length):
        if coins[i] <= 0:
            return -1
        while (total >= coins[i]):
            count += floor(total / coins[i])
            total = total % coins[i]
    if total != 0:
        if length != 0:
            if length > 1:
                coins_copy.pop(1)
                return makeChange(coins_copy, total)
            else:
                coins.pop(0)
                return makeChange(coins, total)
        else:
            return -1
    else:
        return floor(count)
