#!/bin/python3

import math


def jump_search(arr, element):
    if element < arr[0] or element > arr[-1]:
        return False
    else:
        n = len(arr)
        step = int(math.sqrt(n))

        start = ((n-1) // step) * step
        for i in range(step, n, step):
            if element < arr[i]:
                start = i - step
                break

        state = False
        for j in range(start, min(start + step, n)):
            if element == arr[j]:
                state = True
                break
            elif element < arr[j]:
                break

        return state


def whatFlavors(costs, money):
    costs_set = dict()
    for i, cost in enumerate(costs):
        costs_set[cost] = costs_set.get(cost, []) + [i]

    keys = list(costs_set.keys())
    keys.sort()
    keys = [k for k in keys if k < money]

    index_1, index_2 = 0, 0
    if len(keys) > 1000:
        for key in keys:
            remain = money - key
            if jump_search(keys, remain):
                if key == remain:
                    index_1 = costs_set[key][0]
                    index_2 = costs_set[remain][1]
                else:
                    index_1 = costs_set[key][0]
                    index_2 = costs_set[remain][0]
                break
    else:
        state = True
        value1, value2 = 0, 0
        for key in keys:
            remain = money - key
            if state:
                for key2 in keys:
                    if key2 < remain:
                        continue
                    elif key2 == remain:
                        value1 = key
                        value2 = key2
                        state = False
                        break
                    else:
                        break
            else:
                break

        if value1 == value2:
            index_1 = costs_set[value1][0]
            index_2 = costs_set[value2][1]
        else:
            index_1 = costs_set[value1][0]
            index_2 = costs_set[value2][0]

    return [index_1 + 1, index_2 + 1]


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())
        n = int(input())
        costs = list(map(int, input().rstrip().split()))

        indexes = whatFlavors(costs, money)
        indexes.sort()
        print(indexes[0], indexes[1])
