def abbreviation(a, b):
    A = [[None for j in range(len(b))] for i in range(len(a))]

    j = 0
    if a[0].upper() == b[0]:
        A[0][0] = True
    upper_encountered = a[0].isupper()

    for i in range(1, len(a)):
        if a[i].isupper() and upper_encountered:
            A[i][j] = False
        elif a[i].isupper() and not upper_encountered and a[i] == b[j]:
            A[i][j] = True
            upper_encountered = True
        elif a[i].isupper() and not upper_encountered and a[i] != b[j]:
            A[i][j] = False
            upper_encountered = True
        elif a[i].islower() and a[i].upper() == b[j] and not upper_encountered:
            A[i][j] = True
        else:
            A[i][j] = A[i-1][j]

    i = 0
    for j in range(1, len(b)):
        A[i][j] = False

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i].upper() == b[j] and a[i].islower():
                A[i][j] = A[i-1][j-1] or A[i-1][j]
            elif a[i].upper() == b[j] and a[i].isupper():
                A[i][j] = A[i-1][j-1]
            elif a[i].upper() != b[j] and a[i].islower():
                A[i][j] = A[i-1][j]
            else:
                A[i][j] = False

    if A[len(a)-1][len(b)-1]:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        a = input().strip()
        b = input().strip()

        result = abbreviation(a, b)
        print(result)
