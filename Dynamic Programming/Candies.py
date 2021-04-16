def candies(n, arr):
    numbers_1 = [1 for _ in range(n)]
    numbers_2 = [1 for _ in range(n)]

    for x in range(1, n):
        if arr[x] > arr[x-1]:
            numbers_1[x] = numbers_1[x-1] + 1

    for x in range(n-2, -1, -1):
        if arr[x] > arr[x+1]:
            numbers_2[x] = numbers_2[x+1] + 1

    numbers = [max(numbers_1[k], numbers_2[k]) for k in range(n)]

    return sum(numbers)


if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)
