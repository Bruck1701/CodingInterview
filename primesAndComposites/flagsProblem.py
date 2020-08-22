def solution(A):

	if len(A)==1:
		return 0


	peaks = [0 for el in A]
	peaks[-1] = len(A)
	countPeaks=1

	for idx in range(len(A)-2,-1,-1):
		if A[idx] <= A[idx+1]:
			peaks[idx] = peaks[idx+1]
		else:
			peaks[idx] = idx
			countPeaks+=1
	
	#solution( [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
	print(peaks)

	flags = countPeaks

	while flags > 1:

		countFlag = flags-1
		flagPos = peaks[peaks[0]]
		
		while countFlag > 0:
			
			nextPos=flagPos+flags

			if nextPos > len(peaks)-1:
				break
			
			else:
				countFlag-=1
				flagPos=peaks[nextPos]
		
		if countFlag == 0:
			return flags

		flags-=1
	
	return 0

print(solution( [1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))

print(solution( [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

print(solution( [1]))