from typing import List
class Solution:
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        k = k%len(nums)
          
        newHead=nums[-k:]
        newTail=nums[0:len(nums)-(k-1)]
        newHead.extend(newTail)
    
        for index in range(len(nums)):
            nums.insert(index,newHead[index])
            nums.pop()
        
sol = Solution()
nums = [-1,-100,3,99]
k = 2
result = sol.rotate(nums,k)
print(nums)
   