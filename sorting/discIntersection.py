#from operator import itemgetter


def solution(A):
    # write your code in Python 3.6
    arrows = []
    for i in range(len(A)):
        arrows.append((i-A[i], 1))
        arrows.append((i+A[i], -1))

    arrows = sorted(arrows, key=lambda tup: (tup[0], -tup[1]))

    value = 0
    circ = []
    for el in arrows[1:len(arrows)-1]:
        if el[1] == 1:
            value += 1
            circ.append(value)
            #print(el[1], value)
        else:
            value -= 1

    solution = sum(circ)
    if solution > 10000000:
        return -1
    return solution


print(solution([1, 5, 2, 1, 4, 0]))
