def anagrams(string):
    n = len(string)
    total = 0
    for i in range(1, n+1):
        sets = []
        counts = []
        for x in range(n+1-i):
            set_x = list(string[x:x+i])
            set_x.sort()
            try:
                index = sets.index(set_x)
                counts[index] += 1
            except:
                sets.append(set_x)
                counts.append(1)

        for count in counts:
            if count > 1:
                total += int(count*(count-1)/2)

    return total


if __name__ == '__main__':
    T = int(input().strip())

    for t in range(T):
        string = input().strip()

        res = anagrams(string)
        print(res)
