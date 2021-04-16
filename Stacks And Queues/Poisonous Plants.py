def poisonousPlants(plants):
    stack = []
    max_days = 0

    for plant in plants:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)

        if not stack:
            days = 0

        max_days = max(max_days, days)
        stack.append((plant, days))

    return max_days


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)
    print(result)
