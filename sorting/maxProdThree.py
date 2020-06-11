
def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    if A[-1] == 0:
        return 0

    elif A[-1] < 0:
        return A[-1]*A[-2]*A[-3]
    else:
        return max(A[-1]*A[-2]*A[-3], A[0]*A[1]*A[-1])


print(solution([-3, 1, 2, -2, 5, 6]))
print(solution([-5, 5, -5, 4]))
