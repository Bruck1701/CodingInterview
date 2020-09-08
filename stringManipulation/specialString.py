def substrCount(n, s):
    l=[]
    current = None
    count = 0
    ans = 0

    for el in s:
        if el == current:
            count+=1
        else:
            if current is not None:
                l.append((current,count))
            current = el
            count = 1
    l.append((current,count))
    
    for i in range(len(l)):
        el = l[i]
        ans+= (el[1]*(el[1]+1)) //2

        if i in range(1,len(l)-1):
            el1 = l[i-1]
            el2 = l[i]
            el3 = l[i+1]
        
            if el1[0]==el3[0] and el2[1]==1:
                ans+=min(el1[1],el3[1])

    return ans


substrCount(42,"aaabbc")
substrCount(42,"asasd")
substrCount(42,"abcbaba")
substrCount(42,"aaaa")