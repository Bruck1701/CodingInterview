def maximumToys(prices, k):

    prices.sort()

    count=0
    idx=0
    while True:

        if idx<len(prices):
            k=k-prices[idx]

        if k>=0 and idx<len(prices):
            count+=1
            idx+=1
        else:
            break
    
    
    return count
    
    

    print(prices)


maximumToys([1,12,5,111,200,1000,10],50)
maximumToys([1,2,3,4],7)
maximumToys([1],100)
