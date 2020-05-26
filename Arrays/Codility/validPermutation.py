def solution(A):
    # write your code in Python 3.6

    A = [x-1 for x in A]

    A.sort()

    for idx in range(len(A)):
        if idx != A[idx]:
            return 0

    return 1


print(solution([4, 1, 3, 2]))
print(solution([4, 1,  2]))
