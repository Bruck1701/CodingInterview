'''
Problem:  Determine if a string with brackets and parenthesis is properly balanced.
[] OK
{} OK
[(]) NOT BALANCED


'''


def solution(S):
    # write your code in Python 3.6

    if len(S) == 0:
        return 1

    hashmap = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for el in S:
        if el in hashmap:
            stack.append(hashmap[el])
        else:
            if el == "}" or el == "]" or el == ")":
                if len(stack) == 0:
                    return 0
                else:
                    value = stack.pop()
                    if el != value:
                        return 0

    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution('{[()()]}'))
print(solution('([)()]'))
print(solution(''))
print(solution(']'))
print(solution('{(a)[b]}'))
