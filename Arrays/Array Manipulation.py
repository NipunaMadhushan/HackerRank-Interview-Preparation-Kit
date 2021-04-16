def generator_queries(m):
    for x in range(m):
        yield map(int, input().strip().split())


def arrayManipulation(n, m):
    arr = [0] * (n+1)
    for a, b, k in generator_queries(m):
        arr[a-1] += k
        arr[b] -= k

    total, maximum = 0, 0
    for x in range(n):
        total += arr[x]
        maximum = max(total, maximum)

    return maximum


if __name__ == '__main__':
    n, m = map(int, input().split())

    result = arrayManipulation(n, m)
    print(result)
