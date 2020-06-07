
def solution(A):
    # write your code in Python 3.6
    if len(A) <= 1:
        return 0

    maxProfit = -1*float('inf')
    minBuyPrice = float('inf')

    for el in A:
        if el < minBuyPrice:
            minBuyPrice = el
        elif el-minBuyPrice > maxProfit:
            maxProfit = el-minBuyPrice

    return max(0, maxProfit)


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
