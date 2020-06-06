def solution(A):
    # write your code in Python 3.6 Solution in O(N), but uses too much memory, since it stores the indices of every occurence of the leader.

    if len(A) == 0:
        return -1

    if len(A) == 1:
        return 0

    maxCount = 0
    hashCount = {}
    hashIndex = {}

    for i in range(len(A)):
        el = A[i]
        if el not in hashCount:
            hashCount[el] = 1
            hashIndex[el] = {i}
            count = 1
        else:
            count = hashCount[el]+1
            hashCount[el] = count
            hashIndex[el].add(i)
            if count > maxCount:
                maxCount = count
                maxIndex = el

    if maxCount > (len(A)/2):
        return list(hashIndex[maxIndex])[0]
    else:
        return -1


print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
