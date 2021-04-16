def alt_characters(s):
    last = s[0]
    count = 0
    for c in s[1:]:
        if last == c:
            count += 1
        else:
            last = c

    return count


if __name__ == '__main__':
    T = int(input().strip())
    for t in range(T):
        s = input().strip()

        res = alt_characters(s)
        print(res)
