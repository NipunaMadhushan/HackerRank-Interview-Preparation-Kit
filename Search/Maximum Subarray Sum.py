def max_subarr_sum(arr, m):
    freq = []
    cur = 0
    for i in arr:
        cur = (cur + i) % m
        freq.append(cur)

    freq = list(enumerate(freq))
    freq.sort(key=lambda x: x[1])

    maximum = 0
    for num1 in freq:
        maximum = max(maximum, num1[1])

    for x in range(len(freq)-1):
        if freq[x][0] > freq[x+1][0]:
            maximum = max(maximum, (m+freq[x][1]-freq[x+1][1]) % m)

    return maximum


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        n, m = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))

        ans = max_subarr_sum(arr, m)
        print(ans)
