def sub_seq(string_1, string_2):
    set_1 = set(string_1)
    set_2 = set(string_2)

    com = set_1.intersection(set_2)

    if len(com) > 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    T = int(input().strip())

    for t in range(T):
        string_1 = input().strip()
        string_2 = input().strip()

        res = sub_seq(string_1, string_2)
        print(res)
