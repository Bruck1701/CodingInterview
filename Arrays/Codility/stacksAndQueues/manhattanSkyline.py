# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(H):
    # write your code in Python 3.6

    if len(H) == 1:
        return 1

    stack = []
    # stack.append(H[0])
    counter = 0

    for el in H:
        if not stack:
            stack.append(el)
        else:
            block = stack.pop()

            if el < block:
                while el < block:
                    counter += 1
                    if len(stack) > 0:
                        block = stack.pop()
                    else:
                        break
                if el > block:
                    stack.append(block)
                stack.append(el)
            elif el > block:
                stack.append(block)
                stack.append(el)
            elif el == block:
                stack.append(block)

    return len(stack)+counter


print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
