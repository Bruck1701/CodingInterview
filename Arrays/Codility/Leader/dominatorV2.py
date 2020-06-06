def solution(A):
    # write your code in Python 3.6. O(N) as well, but only returns the first occurrence of the leader.

    if len(A) == 0:
        return -1

    if len(A) == 1:
        return 0

    candidate = -1
    count = 0

    for i in range(len(A)):
        el = A[i]
        if count == 0:
            candidate = el
            count = 1
        else:
            if el != candidate:
                count -= 1
            else:
                count += 1
    count = 0
    for el in A:
        if el == candidate:
            count += 1

    if count > len(A)/2:
        return A.index(candidate)
    else:
        return -1


print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
