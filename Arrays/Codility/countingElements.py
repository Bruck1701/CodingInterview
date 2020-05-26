def solution(N, A):

    A = [x-1 for x in A]
    # print(A)

    dicio = {k: 0 for k in range(N)}
    # print(dicio)

    largest = 0
    startLine = 0

    for inst in A:
        #print(inst, dicio)
        if inst < N:
            if dicio[inst] < startLine:
                value = 1+startLine
            else:
                value = dicio[inst]+1

            if value > largest:
                largest = value
            dicio[inst] = value
        else:
            startLine = largest

    # print(dicio)
    output = [max(v, startLine) for k, v in dicio.items()]
    return output


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))

print(solution(1, [1, 1, 1, 2, 4]))
