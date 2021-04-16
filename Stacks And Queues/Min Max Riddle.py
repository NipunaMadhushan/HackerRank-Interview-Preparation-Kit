def riddle(n, arr):
    num_lengths = dict()

    List = [arr]
    while len(List) > 0:
        new_list = []
        for sub_arr in List:
            length = len(sub_arr)
            minimum = min(sub_arr)
            num_lengths[length] = max(num_lengths.get(length, 0), minimum)

            indexes = [-1]
            for x in range(length):
                if sub_arr[x] == minimum:
                    indexes.append(x)
            indexes.append(length)

            for x in range(1, len(indexes)):
                if indexes[x-1] + 1 != indexes[x]:
                    new_list.append(sub_arr[indexes[x-1]+1:indexes[x]])

        List = new_list.copy()

    #print(num_lengths)  # Test

    for i in range(n-1, 0, -1):
        num_lengths[i] = max(num_lengths[i+1], num_lengths.get(i, 0))

    #print(num_lengths)  # Test

    win_maxes = []
    for num in range(1, n+1):
        win_maxes.append(num_lengths[num])

    return win_maxes


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    res = riddle(n, arr)
    print(*res)
