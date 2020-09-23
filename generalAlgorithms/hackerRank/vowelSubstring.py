
def findSubstring(s, k):
	# Write your code here
	vowels = ['a','e','i','o','u']
	maxValue = 0
	pos = 0

	
	for i in range(0,len(s)-k+1):
		#print(s[i:])
		if i==0:
			count=0
			for j in range(0,k):
				if s[j] in vowels:
					count+=1
			substringVal=count
		else:
			count = substringVal
			if s[i-1] in vowels:
			
				count-=1
			if s[i+k-1] in vowels:
			
				count+=1
			substringVal = count
			
		
		if substringVal>maxValue:
			maxValue = substringVal
			pos = i

	if maxValue == 0:
		return "Not found!"



	print(s[pos:pos+k])



findSubstring('caberqiitefg',5)
findSubstring('azerdii',5)
findSubstring('aeiouia',3)