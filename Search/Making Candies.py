import sys
import math


def make_candies(m, w, p, n):
    candy = 0
    invest = 0
    spend = sys.maxsize
    while candy < n:
        passes = (p - candy) // (m * w)
        if passes <= 0:
            mw = (candy // p) + m + w
            half = math.ceil(mw / 2)
            if m > w:
                m = max(m, half)
                w = mw - m
            else:
                w = max(w, half)
                m = mw - w
            candy %= p
            passes = 1
        candy += passes * m * w
        invest += passes
        spend = min(spend, invest + math.ceil((n - candy) / (m * w)))

    return min(invest, spend)


if __name__ == '__main__':
    m, w, p, n = map(int, input().strip().split())

    ans = make_candies(m, w, p, n)
    print(ans)
