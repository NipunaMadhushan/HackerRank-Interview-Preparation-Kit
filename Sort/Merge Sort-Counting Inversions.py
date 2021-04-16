# Run in PyPy3
def mergeSort(arr):
    count = 0
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        L, count1 = mergeSort(L)
        R, count2 = mergeSort(R)

        i = j = k = 0

        count = count1+count2
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                count += (len(L)-i)
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        """
        if i < len(L):
            arr = arr[:-(len(L) - i)] + L[i:]
        else:
            arr = arr[:-(len(R) - j)] + R[j:]
        """

    return arr, count


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result, count = mergeSort(arr)
        print(count)

