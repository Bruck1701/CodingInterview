'''
Missing element on array problem
'''


def solution(A):
    '''
    if the array is empty the smallest number not present is one since the range of each elem of the array is [1..100,001]
    else:
        sort A so we can have the smallest numbers first. We could check if the first element is 1 and return it as well. 
        create a dictionary and in the loop insert key:value pairs. key i starting from 1 -> len(A)+1 and values A[i]
        Lastly check the key:value pairs of the dictionary. if k!=v, k is the smallest number not present.
    '''

    if len(A) == 0:
        return 1

    A.sort()  # O(NlogN)
    dicio = {}

    for i in range(len(A)):  # O(N)
        dicio[i+1] = A[i]

    for k, v in dicio.items():  # O(N)
        if k != v:
            return k

    return len(A)+1

# Score 100%
# Complexity O(NlogN)
