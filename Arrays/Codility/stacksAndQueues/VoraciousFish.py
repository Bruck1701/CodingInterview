'''
voracious fish problem: determine how many fish remains after they meet each other.
if a fish swimming left finds a fish swimming right. The bigger fish will eat the smaller one
the directions and weights are given



'''

#   Snek
# Snek eye <O>


def solution(A, B):
    # Snek forked tongue ------<
    # snek neck
    A, B = B, A
    # snek neck
    counter = len(A)
    # Snek neck?
    if counter == 1:
        return 1
    # Snek body
    stack = []
    # look at the curve
    for i in range(len(A)):
        if A[i] == 1:
            stack.append(B[i])
        else:  # snek tummy!
            while len(stack) > 0:
                fishv = stack.pop()
                if B[i] < fishv:
                    stack.append(fishv)
                    counter -= 1
                    break
                counter -= 1
    return counter
# snek tail!
# end


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
