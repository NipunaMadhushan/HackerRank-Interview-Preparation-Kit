#!/bin/python3

import math
import os
import random
import re
import sys


def twice_median(counts, d, state):
    if state:
        freq = 0
        mid = d // 2 + 1
        median = 0
        for a in range(201):
            freq += counts[a]
            if mid <= freq:
                median = a
                break

        return median * 2
    else:
        freq = 0
        mid1 = d // 2
        mid2 = mid1 + 1
        median1, median2 = 0, 0
        last = 0
        for a in range(201):
            freq += counts[a]
            if mid1 <= freq:
                median1 = a
                last = a
                freq -= counts[a]
                break
        for b in range(last, 201):
            freq += counts[b]
            if mid2 <= freq:
                median2 = b
                break

        return median1 + median2


def activityNotifications(expenditure, n, d):
    counts = [0 for _ in range(201)]
    for x1 in range(d):
        counts[expenditure[x1]] += 1

    if d % 2 == 0:
        state = False
    else:
        state = True

    alerts = 0
    for x2 in range(d, n):
        t_med = twice_median(counts, d, state)
        if expenditure[x2] >= t_med:
            alerts += 1

        counts[expenditure[x2]] += 1
        counts[expenditure[x2-d]] -= 1

    return alerts


if __name__ == '__main__':
    n, d = map(int, input().split())

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, n, d)
    print(result)
