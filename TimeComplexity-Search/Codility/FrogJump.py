'''
Frog jump problem
'''


def solution(X, Y, D):
    # IF the frogs X == Y the frog does not need to jump returns 0
    # else we check if we can arrive from X to Y with an exact D.length jumps. that means that the remainder of (Y-X) divided by D must be zero.
    # If it is not zero, then one more jump is necessary.
    # This code is O(1)

    if X == Y:
        return 0

    if (Y-X) % D == 0:
        return int((Y-X)/D)
    else:
        return 1 + int(((Y-X)/D))

# Score: 100%
