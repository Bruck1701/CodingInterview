def serviceLane(n, cases,width):
	result = []
	for el in cases:
		max_size = min(width[el[0]:el[1]+1])
		result.append(max_size)
	return result

n= 8 
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
width = [2,3,1,2,3,2,3,3]

result = serviceLane(n,cases,width)
print(result)