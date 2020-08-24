def chocolateFeast(n, c, m):
	choc = 0
	money = n
	cost = c
	trade = m
	wraps = 0

	choc += money//cost
	wraps = choc

	while (wraps >=trade):
		#print('choc:',choc,'wraps:',wraps)
		new_choc = wraps//trade
		wraps =  wraps%trade + new_choc
		choc+=new_choc
	
		
	return choc


result = chocolateFeast(15,3,2)
print(result)


result = chocolateFeast(10,2,5)
print(result)


result = chocolateFeast(12,4,4)
print(result)


result = chocolateFeast(6,2,2)
print(result)
