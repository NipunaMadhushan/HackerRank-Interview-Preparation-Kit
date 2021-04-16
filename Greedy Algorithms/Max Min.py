def maxMin(k, arr):
    arr.sort()

    min_diff = arr[-1] - arr[0]
    for i in range(len(arr)-k+1):
        diff = arr[i+k-1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


if __name__ == '__main__':
    n = int(input())
    k = int(input())

    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
