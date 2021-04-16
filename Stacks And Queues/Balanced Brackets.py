def isBalanced(s):
    stack = []
    state = "YES"
    for x in s:
        if x == "{" or x == "(" or x == "[":
            stack.append(x)
        else:
            if len(stack) > 0:
                last = stack.pop(-1)
                if x == "}" and last != "{":
                    state = "NO"
                    break
                elif x == ")" and last != "(":
                    state = "NO"
                    break
                elif x == "]" and last != "[":
                    state = "NO"
                    break
            else:
                state = "NO"
                break

    if len(stack) > 0:
        state = "NO"

    return state


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)
