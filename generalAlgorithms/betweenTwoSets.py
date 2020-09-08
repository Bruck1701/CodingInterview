def getTotalX(a, b):
    
    a.sort()
    b.sort()
    c = [x for x in range(a[0],b[-1]+1)]

    count =0 

    for el in c:
        cond=True
        for j in a:
            if el%j !=0:
                cond = False
                break
        if cond==True:
            for k in b:
                if k%el!=0:
                    cond = False
                    break
        if cond ==True:
            count+=1

    return count

    print(count)


getTotalX([2,4],[16,32,96])