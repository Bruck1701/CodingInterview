def solution(A):
    # write your code in Python 3.6
    A = list(set(A))
    A.sort()

    if A[-1] <= 0:
        return 1

    dicio = {}
    counter = 1

    for el in A:
        if el > 0:
            dicio[counter] = el
            counter += 1

    for k, v in dicio.items():
        if k != v:
            return k

    return len(A)+1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))

print(solution([-1]))
print(solution([1]))
