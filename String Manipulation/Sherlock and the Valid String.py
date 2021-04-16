def valid_string(s):
    set_s = set(s)
    counts = [s.count(k) for k in set_s]
    set_counts = set(counts)
    if len(set_counts) == 1:
        return "YES"
    elif len(set_counts) == 2:
        minimum = min(set_counts)
        maximum = max(set_counts)
        if counts.count(maximum) == 1 and maximum == minimum + 1:
            return "YES"
        elif counts.count(minimum) == 1 and minimum == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    s = input().strip()

    res = valid_string(s)
    print(res)
