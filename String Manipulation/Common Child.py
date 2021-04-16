def common_child(s1, s2):
    n = len(s1)

    matrix = [[0 for k1 in range(n+1)] for k2 in range(n+1)]

    for x in range(n):
        for y in range(n):
            if s1[x] == s2[y]:
                matrix[x+1][y+1] = matrix[x][y] + 1
            else:
                matrix[x+1][y+1] = max(matrix[x+1][y], matrix[x][y+1])

    return matrix[n][n]


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    result = common_child(s1, s2)
    print(result)
