#!/bin/python3

import math
import os
import random
import re
import sys


def minTime(n, machines, goal):
    lower = math.ceil(goal / n) * min(machines)
    upper = math.ceil(goal / n) * max(machines)

    while lower != upper:
        days = int((lower + upper) / 2)

        total = 0
        for machine in machines:
            total += int(days // machine)

        if total >= goal:
            upper = days
        else:
            lower = days + 1

    return lower


if __name__ == '__main__':
    n, goal = map(int, input().strip().split())
    machines = list(map(int, input().rstrip().split()))

    ans = minTime(n, machines, goal)
    print(ans)
