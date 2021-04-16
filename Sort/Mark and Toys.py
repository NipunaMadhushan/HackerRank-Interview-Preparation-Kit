#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()

    count = 0
    total = 0
    for price in prices:
        total += price
        if total <= k:
            count += 1
        else:
            break

    return count


if __name__ == '__main__':
    n, k = map(int, input().split())

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
