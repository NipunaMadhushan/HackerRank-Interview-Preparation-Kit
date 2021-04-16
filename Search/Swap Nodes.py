#!/bin/python3

import os
import sys


class node:
    def __init__(self, num, left, right, depth):
        self.num = num
        self.left = left
        self.right = right
        self.depth = depth

    def swap(self):
        temp = self.left
        self.left = self.right
        self.right = temp


def print_binary_tree(nodes):
    List = [1]
    output = [1]
    while len(List) > 0:
        num = List.pop(0)
        index = output.index(num)
        x = nodes[num]
        left = x.left
        right = x.right
        if right != -1:
            List.append(right)
            output.insert(index+1, right)
        if left != -1:
            List.append(left)
            output.insert(index, left)

    print(*output)


def swapNodes(nodes, queries):
    for k in queries:
        for x in nodes:
            if nodes[x].depth % k == 0:
                nodes[x].swap()

        print_binary_tree(nodes)


if __name__ == '__main__':
    N = int(input())

    nodes = {1: node(1, -1, -1, 1)}
    for n in range(1, N+1):
        left, right = map(int, input().strip().split())
        nodes[n].left = left
        nodes[n].right = right
        nodes[left] = node(left, -1, -1, nodes[n].depth + 1)
        nodes[right] = node(right, -1, -1, nodes[n].depth + 1)

    depths = [{}]
    for a in nodes:
        depth = nodes[a].depth
        if depth > len(depths):
            depths.append({nodes[a].num: nodes[a]})
        else:
            depths[depth-1][nodes[a].num] = nodes[a]

    queries_count = int(input())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    swapNodes(nodes, queries)
