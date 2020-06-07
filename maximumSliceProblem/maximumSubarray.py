
def maxCrossingSum(A, begin, mid, end):

    sm = 0
    leftSum = -1*float('inf')
    rightSum = -1*float('inf')

    for i in range(mid, begin-1, -1):
        sm += A[i]
        if sm > leftSum:
            leftSum = sm
    sm = 0
    for j in range(mid+1, end+1):
        sm += A[j]
        if sm > rightSum:
            rightSum = sm

    # leftSum = sum(A[begin:mid])
    # rightSum = sum(A[mid:end])
    return max(leftSum, rightSum, leftSum+rightSum)


def recfunc(A, begin, end):
    if begin == end:
        return A[begin]

    mid = (begin+end)//2

    left = recfunc(A, begin, mid)
    right = recfunc(A, mid+1, end)

    return max(left, right, maxCrossingSum(A, begin, mid, end))


def solution(A):
    # write your code in Python 3.6
    return recfunc(A, 0, len(A)-1)


print(solution([3, 2, -6, 4, 0]))
print(solution([1, 1, -2]))
