#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    set_a = set(a)
    set_b = set(b)
    set_all = list(set_a.intersection(set_b))
    counts_a = [a.count(k1) for k1 in set_all]
    counts_b = [b.count(k2) for k2 in set_all]
    for x in range(len(counts_a)):
        if counts_a[x] > counts_b[x]:
            counts_a[x] = counts_b[x]

    length = sum(counts_a)

    return len(a) + len(b) - 2*length


if __name__ == '__main__':
    a = input()
    b = input()

    res = makeAnagram(a, b)
    print(res)
