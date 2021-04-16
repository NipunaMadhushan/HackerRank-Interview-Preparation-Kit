from functools import cmp_to_key


class Player:
    name = ""
    score = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return "(" + self.name + self.score + ")"

    def comparator(a, b):
        if b.score == a.score:
            str1 = ""
            str2 = ""
            state = False
            for i in range(min(len(a.name), len(b.name))):
                if a.name[i] != b.name[i]:
                    str1 = a.name[i]
                    str2 = b.name[i]
                    state = True
                    break
            if state:
                return ord(str1) - ord(str2)
            else:
                if len(a.name) <= len(b.name):
                    return ord("0") - ord("1")
                else:
                    return ord("1") - ord("0")

        else:
            return b.score - a.score


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
