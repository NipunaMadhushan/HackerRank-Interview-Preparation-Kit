from itertools import permutations
from collections import defaultdict


def reverseShuffleMerge(s):
    char_freq = defaultdict(int)

    for i in s:
        char_freq[i] += 1

    used_chars = defaultdict(int)
    remain_chars = dict(char_freq)

    def can_use(char):
        return (char_freq[char] // 2 - used_chars[char]) > 0

    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars

    word = []
    for char in reversed(s):
        if can_use(char):
            while word and word[-1] > char and can_pop(word[-1]):
                removed_char = word.pop()
                used_chars[removed_char] -= 1

            used_chars[char] += 1
            word.append(char)

        remain_chars[char] -= 1

    return "".join(word)


if __name__ == '__main__':
    s = input()

    result = reverseShuffleMerge(s)
    print(result)
