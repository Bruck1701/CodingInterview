from  typing import List

#from bisect import bisect_left



class Solution:


	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		result = set()
		for left in range(len(nums)-2):
			if left > 0 and nums[left]==nums[left-1]:
				continue
			
			middle = left+1
			right = len(nums)-1

			while middle<right:
				s = nums[left]+nums[middle]+nums[right]
				if s < 0:
					middle+=1
				elif s > 0:
					right -=1
				else:
					print(s)
					result.add((nums[left],nums[middle],nums[right] ))
					middle+=1
					right-=1

		output = [list(i) for i in result]
		
		return output



sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]) )