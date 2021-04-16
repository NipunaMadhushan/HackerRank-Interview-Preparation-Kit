#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    luck = 0
    important = []
    for contest in contests:
        if contest[1] == 1:
            important.append(contest[0])
        else:
            luck += contest[0]

    important.sort()
    important.reverse()

    luck += sum(important[:k])
    luck -= sum(important[k:])

    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
