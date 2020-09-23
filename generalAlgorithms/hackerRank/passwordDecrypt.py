
def decryptPassword(s):
	# Write your code here
	numbers = []
	count = 0

	for el in s:
		if el.isalpha():
			break
		else:
			numbers.append(el)
			count +=1
	
	newS = list(s[count:])
	
	for i in range(len(newS)):
		if newS[i]=='*':
			newS[i-1],newS[i-2] = newS[i-2],newS[i-1]

		elif newS[i]=='0':
			newS[i]=str(numbers.pop())
	
	result = "".join(newS)
	result = result.replace('*','')

	print(result)
	return result

decryptPassword("pTo*Ta*O")
decryptPassword("51Pa*0Lp*0e")
decryptPassword("43Ah*ck0rr0nk")
decryptPassword("p")


