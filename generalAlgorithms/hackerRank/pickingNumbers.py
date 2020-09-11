
from collections import Counter

def pickingNumbers(a):
	hmap = Counter(a)

	if len(hmap)==1:
		print(len(a))
		return len(a)

	a = sorted(set(a))
	print(a)
	print(hmap)

	largest_count = [(k, v) for k, v in sorted(hmap.items(), key=lambda item: item[1])][-1][1]

	#largest_count = 0


	for i in range(0,len(a)-1):
		diff = a[i+1]-a[i]
		if diff <= 1 and (hmap[a[i+1]]+hmap[a[i]]) > largest_count:
			largest_count = hmap[a[i+1]]+hmap[a[i]]


	print(largest_count)
	return largest_count

# pickingNumbers([1,2, 2, 3, 1, 2])
# pickingNumbers([4,6,5,3,3,1])

lstr="66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66 66"

pickingNumbers([int(x) for x in lstr.split()])

lstr = "4 97 5 97 97 4 97 4 97 97 97 97 4 4 5 5 97 5 97 99 4 97 5 97 97 97 5 5 97 4 5 97 97 5 97 4 97 5 4 4 97 5 5 5 4 97 97 4 97 5 4 4 97 97 97 5 5 97 4 97 97 5 4 97 97 4 97 97 97 5 4 4 97 4 4 97 5 97 97 97 97 4 97 5 97 5 4 97 4 5 97 97 5 97 5 97 5 97 97 97"


pickingNumbers([int(x) for x in lstr.split()])
