def carryOver(x,y):
    num1 = str(x)[::-1]
    num2 = str(y)[::-1]
    
    if len(num1)>len(num2):
        t = list(num2)
        for i in range(0,len(num1)-len(num2)):
            t.append(0)
        num2 = "".join([str(x) for x in t])
    
    elif len(num2)>len(num1):    
        t = list(num1)
        for i in range(0,len(num2)-len(num1)):
            t.append(0)
        num1 = "".join([str(x) for x in t])
    

    carry = 0
    carryCount = 0
    for i in range(len(num1)):
        result = carry + int(num1[i])+int(num2[i])
        carry = result//10
        
        if carry>0:
            carryCount+=1
        print(result,carry,carryCount)


    print(num1)
    print(num2)

carryOver(1234,5678)    