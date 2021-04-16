#!/bin/python3

import math
import os
import random
import re
import sys


def triplets(a, b, c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    b.sort()
    c.sort()
    len_a = len(a)
    len_c = len(c)

    start_a, start_c = 0, 0
    total = 0
    for q in b:
        count1, count2 = len_a, len_c
        for p in range(start_a, len_a):
            if a[p] > q:
                count1 = p
                start_a = p
                break
        for r in range(start_c, len_c):
            if c[r] > q:
                count2 = r
                start_c = r
                break

        total += count1*count2

    return total


if __name__ == '__main__':
    len_a, len_b, len_c = map(int, input().strip().split())

    arr_a = list(map(int, input().strip().split()))
    arr_b = list(map(int, input().strip().split()))
    arr_c = list(map(int, input().strip().split()))

    ans = triplets(arr_a, arr_b, arr_c)
    print(ans)
