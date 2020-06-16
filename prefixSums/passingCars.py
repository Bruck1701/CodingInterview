
def solution(A):
    if len(A) == 1:
        return 0

    count = 0
    while A[count] == 1:
        count += 1
        if count == len(A):
            return 0

    passing = 0
    zero_car = 0

    for el in A[count:]:
        if el == 0:
            zero_car += 1
        else:
            passing += (zero_car*el)
            if passing > 1000000000:
                return -1

    return passing


print(solution([0, 1, 0, 1, 1]))
