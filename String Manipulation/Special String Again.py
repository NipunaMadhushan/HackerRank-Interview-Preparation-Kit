#!/bin/python3

import math
import os
import random
import re
import sys


def substrCount(n, s):
    count = 0

    last = s[0]
    k = 1
    for i in range(1, n):
        if s[i] == last:
            k += 1
        else:
            count += int(k*(k+1)/2)
            last = s[i]
            k = 1

    count += int(k*(k+1)/2)

    for j in range(1, n-1):
        if s[j-1] == s[j+1]:
            if s[j-1] != s[j]:
                char = s[j-1]
                for x in range(min(j, n-1-j)):
                    if s[j-1-x] == char and s[j+1+x] == char:
                        count += 1
                    else:
                        break

    return count


if __name__ == '__main__':
    n = int(input())
    s = input()

    result = substrCount(n, s)
    print(result)
