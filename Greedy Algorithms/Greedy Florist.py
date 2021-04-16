def getMinimumCost(k, n, c):
    c.sort()
    c.reverse()

    prev_pur = 0
    index = 0
    cost = 0
    while index < n:
        cost += sum(c[index:min(n, index+k)]) * (prev_pur + 1)
        index += k
        prev_pur += 1

    return cost


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, n, c)
    print(minimumCost)
