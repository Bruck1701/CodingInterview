from collections import Counter
def freqQuery(queries):
	freq = Counter() #key:value  = number_in_array: how_many_times_this_number_occurs_in_array
	occ = Counter() # key:value = number_of_repeated_ocurrences: how_many_of_these_repetitions_are_there
	arr = []

	for q in queries:
		op = q[0]
		qvalue = q[1]
		if op==1:
			if occ[freq[qvalue]]>0:
				occ[freq[qvalue]]-=1
			
			freq[qvalue]+=1
			occ[freq[qvalue]]+=1

		elif op==2:
			if freq[qvalue]>0:
				occ[freq[qvalue]]-=1
				freq[qvalue]-=1
				occ[freq[qvalue]]+=1

		else:
			if occ[qvalue]>0:
				arr.append(1)
			else:
				arr.append(0)
	return arr




queries = [[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
r = freqQuery(queries)
print(r)

queries = [[3, 4], [2, 1003], [1, 16], [3, 1]]
r = freqQuery(queries)
print(r)

queries = [[1, 3], [2, 3], [3, 2], [1, 4], [1, 5], [1, 5], [1, 4], [3, 2], [2, 4], [3, 2]]
r = freqQuery(queries)
print(r)