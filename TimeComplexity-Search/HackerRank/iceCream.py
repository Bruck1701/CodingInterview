'''
Ice Cream Parlor Problem


'''


def whatFlavors(cost, money):

    dcindex = {}
    result = []

    for index in range(len(cost)):  # O(N)
        comp = max(0, money-cost[index])

        if cost[index] in dcindex:  # if a given price for an ice cream is already on the hashmap, you have your pair of ice creams stored on dcindex
            tmp = [dcindex[cost[index]], index+1]
            tmp.sort()
            result.append((tmp[0], tmp[1]))
        else:

            # the trick is to store the difference of the price and money as key and the index+1 of ice cream as value
            dcindex[comp] = index+1

    result = result[0]
    print(" ".join(str(x) for x in list(result)))


if __name__ == '__main__':
    # t = int(input())

    # for t_itr in range(t):
    #     money = int(input())

    #     n = int(input())

    #     cost = list(map(int, input().rstrip().split()))

    whatFlavors([1, 4, 5, 3, 2], 4)
    whatFlavors([2, 2, 4, 3], 4)
    whatFlavors([1, 2, 3, 5, 6], 5)
