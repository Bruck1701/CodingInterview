import math


def solution(A, B, K):
    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0
    first_el = math.ceil(A/K)
    last_el = math.floor(B/K)

    return last_el-first_el+1


print(solution(6, 11, 2))
