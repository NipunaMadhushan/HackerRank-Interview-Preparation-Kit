#!/bin/python3

import math
import os
import random
import re
import sys


def maxSubsetSum(arr):
    freq = [arr[0], max(arr[0], arr[1])]

    for i, num in enumerate(arr[2:]):
        freq.append(max(freq[-1], freq[-2]+num, freq[-2], num))

    return freq[-1]


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
    print(res)
