'''
Least integer not in list and not being able to be made of the sum of two elements in the list.

'''


from itertools import combinations


def solution(A):
    B = A.copy()

    for i in range(2, len(A)):
        subset = combinations(A, i)
        newElements = [sum(x) for x in subset]

        B.extend(newElements)

    B.append(sum(A))
    B = list(set(B))
    B.sort()

    dicioB = {}
    for i in range(len(B)):
        dicioB[i+1] = B[i]

    for k, v in dicioB.items():
        if k != v:
            return k

    return len(B)+1


print(solution([1, 2, 5, 7]))

print(solution([1, 2, 2, 5, 7]))
