def countApplesAndOranges(s, t, a, b, apples, oranges):
	#house = 

	countApples = 0
	countOranges = 0

	for el in apples:
		if el+a in range(s,t+1):
			countApples+=1
	for el in oranges:
		if el+b in range(s,t+1):
			countOranges+=1

	print(countApples)
	print(countOranges) 
