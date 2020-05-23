'''
Cyclic Rotaion problem
'''


def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return []

    K = K % len(A)
    for _ in range(K):  # O(N)
        A.insert(0, A.pop())

    return A
