'''
Intro:

Equilibrium Problem


'''


def solution(A):
    # the idea to solve in O(N) is that you get the first value from the array A[0] and sum all the remaining values with
    # python sum function: which is O(N)
    # then from 1 to N (size of A) we verify if the |left-right| is smaller the smallest difference and increase left and decrease right
    # We get O(N) + O(N) = O(N)

    if len(A) == 2:

        return abs(A[0]-A[1])

    minValue = float("inf")
    leftValue = A[0]
    rightValue = sum(A[1:])

    for i in range(1, len(A)):
        if abs(leftValue - rightValue) < minValue:
            minValue = abs(leftValue-rightValue)
        leftValue += A[i]
        rightValue -= A[i]

    return minValue


# Score of solution: 100%
# time: 10 min
