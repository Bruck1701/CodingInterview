from collections import Counter
from typing import List

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		mylist=[(key,value) for key,value in sorted(dict(Counter(nums)).items(),key=lambda  x:x[1])]
		return mylist[0][0]

sol = Solution()
print(sol.singleNumber([2,2,1]))


sol = Solution()
print(sol.singleNumber([4,1,2,1,2]))
