def birthday(s, d, m):

	if len(s)==1 and m==1 and s[0]== d:
		return m

	count = 0 
	for i in range(0,len(s)-m+1):
		soma = 0
		ct = 0 
		while ct<m:
			soma += s[i+ct]
			ct+=1
				
		if soma == d:
			
			count+=1
			print("Count: ",count)

	print(count)
	return count


lstr = "2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1"
birthday([int(x) for x in lstr.split()],18,7)

lstr = "1 2 1 3 2"
birthday([int(x) for x in lstr.split()],3,2)