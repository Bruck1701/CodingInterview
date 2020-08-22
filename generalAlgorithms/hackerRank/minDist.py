#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
	list_of_two_occurrences=[]
	hashmap={}
	for i,val in enumerate(a):
		if val not in hashmap:
			hashmap[val]=[i]
		else:
			hashmap[val].append(i)
			list_of_two_occurrences.append(val)
	
	global_min = float('inf')
	for el in list_of_two_occurrences:
		local_min=float('inf')
		lista=hashmap[el]
		for j in range(1,len(lista)):
			result = lista[j]-lista[j-1]
			if result < local_min:
				local_min = result
		if local_min<global_min:
			global_min = local_min
	return global_min



 
a = [7,1,3,4,1,7]
result = minimumDistances(a)
print(result)

