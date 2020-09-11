from collections import Counter

def triplets(a, b, c):

	h1 = Counter(a)
	h2 = Counter(b)
	h3 = Counter(c)

	a = list(set(a))
	a.sort()
	b = list(set(b))
	b.sort()
	c = list(set(c))
	c.sort()

	count = 0

	#print(a)

	for p in a:
		#print("p->",p)
		for q in b:
			#print("q->",q)
			if q < p:
				continue
			else:
				for r in c:
					#print(p,q,r)
					if r <= q:
						count += 1 #h1[p]*h2[q]*h3[r]
						print(p,q,r)
					else:
						break
	print(count)
	return count

# triplets([3,5,7],[3,6],[4,6,9])
# triplets([1,3,5],[2,3],[1,2,3])
# triplets([1,3,5],[2,3],[1,2,3])

triplets([1,4,5],[2,3,3],[1,2,3])



