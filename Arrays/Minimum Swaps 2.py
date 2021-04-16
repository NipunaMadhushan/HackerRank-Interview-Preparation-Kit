# 100% correct
def minimumSwaps(n, arr):
    swaps = 0
    arr_pos = [*enumerate(arr)]
    arr_pos.sort(key=lambda it: it[1])
    print(arr_pos)
    visited = {k: False for k in range(n)}
    for i in range(n-1):
        pos = arr_pos[i][0]
        if not visited[i] and pos != i:
            while pos != i:
                visited[pos] = True
                pos = arr_pos[pos][0]
                swaps += 1

    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(n, arr)
    print(res)
