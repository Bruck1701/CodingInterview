from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            el = nums[i]
            if target <= el:
                return i

        return len(nums)


print(Solution().searchInsert([1, 3, 5, 6], 5))
print(Solution().searchInsert([1, 3, 5, 6], 2))

print(Solution().searchInsert([1, 3, 5, 6], 7))

print(Solution().searchInsert([1, 3, 5, 6], 0))
