#!/bin/python3

from collections import defaultdict


def freqQuery(queries):
    results = []
    lookup = dict()
    freqs = defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freqs[value] else 0)

    return results


if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    res = freqQuery(queries)
    for p in res:
        print(p)
