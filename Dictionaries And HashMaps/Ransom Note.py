#!/bin/python3

import math
import os
import random
import re
import sys


def checkMagazine(magazine, note):
    words = {}
    for word in magazine:
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1

    keywords = words.keys()
    state = "Yes"
    for x in note:
        try:
            if words[x] > 0:
                words[x] -= 1
            else:
                state = "No"
                break
        except KeyError:
            state = "No"
            break

    return state


if __name__ == '__main__':
    m, n = map(int, input().strip().split())

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    res = checkMagazine(magazine, note)
    print(res)
