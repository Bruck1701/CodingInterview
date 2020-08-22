def timeInWords(h, m):
	unit={1:'one', 2: 'two', 3:'three', 4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10: 'ten',11:'eleven',12:'twelve',13:'thirteen',\
	14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',\
		21:'twenty one',22:'tweenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',\
			29:'twenty nine',30:'half'}



	if m==0:
		return unit[h]+" o\' clock"
	if m<=30:
		if m==15 or m==30:
			return unit[m]+" past "+unit[h]
		if m==1:
			minute="minute"
		else:
			minute="minutes"
		return unit[m]+" "+minute+" past "+unit[h]
	if m>30:
		hour=(h+1)%12
		minute=60-m

		if minute==15:
			return unit[minute]+" to "+unit[hour]
		return unit[minute]+" minutes to "+unit[hour]



result = timeInWords(5,0)
print(result)


result = timeInWords(5,47)
print(result)

result = timeInWords(3,0)
print(result)

result = timeInWords(7,15)
print(result)
