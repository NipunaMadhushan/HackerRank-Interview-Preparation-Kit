def largestRectangle(n, heights):
    area = 0
    blocks = [heights]
    while len(blocks) > 0:
        new_blocks = []
        for block in blocks:
            min_h = min(block)
            area = max(area, len(block) * min_h)
            indexes = [-1]
            for i in range(len(block)):
                if block[i] == min_h:
                    indexes.append(i)
            indexes.append(len(block))

            for x in range(1, len(indexes)):
                if indexes[x-1] + 1 != indexes[x]:
                    new_blocks.append(block[indexes[x-1]+1:indexes[x]])

        blocks = new_blocks.copy()

    return area


if __name__ == '__main__':
    n = int(input())
    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(n, h)
    print(result)
