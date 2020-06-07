
def solution(A):
    # write your code in Python 3.6
    if len(A) <= 1:
        return 0

    B = []
    # in order to use Kadane's algorithm, we need negative numbers in the array
    for idx in range(1, len(A)):
        B.append(A[idx]-A[idx-1])

    globalMax = B[0]
    localMax = B[0]

    for el in B[1:]:
        localMax = max(el, localMax+el)
        globalMax = max(globalMax, localMax)

    return max(0, globalMax)


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
