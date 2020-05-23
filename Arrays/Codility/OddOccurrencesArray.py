def solution(A):
    # write your code in Python 3.6
    hashmap = {}

    if len(A) == 1:
        return A[0]

    for number in A:
        if number not in hashmap:
            hashmap[number] = 1

        else:
            hashmap[number] += 1

    for k, v in hashmap.items():
        if v % 2 != 0:
            return k
