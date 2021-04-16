#!/bin/python3

import math
import os
import random
import re
import sys


def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):
        if i*r in dictPairs:
                count += dictPairs[i*r]
        if i*r in dict:
                dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]

        dict[i] = dict.get(i, 0) + 1

    return count


if __name__ == '__main__':
    n, r = map(int, input().strip().split())

    arr = list(map(int, input().strip().split()))

    ans = countTriplets(arr, r)
    print(ans)
