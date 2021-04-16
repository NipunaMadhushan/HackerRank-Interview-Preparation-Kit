def minimumBribes(arr):
    bribes = 0
    arr = [k-1 for k in arr]

    for i, p in enumerate(arr):
        if p-i > 2:
            bribes = "Too chaotic"
            break

        for j in range(max(p-1, 0), i):
            if arr[j] > p:
                bribes += 1

    return bribes


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        res = minimumBribes(arr)
        print(res)
