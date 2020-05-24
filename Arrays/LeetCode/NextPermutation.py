'''
Problem next permutation
Naive approach: O(N!)

solution: O(N)
'''


from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        for idx in range(len(nums)-1):
            if(nums[idx] >= nums[idx+1]):
                count += 1
        if count == len(nums)-1:
            n = len(nums)
            for i in range(0, int(n / 2)):
                nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
            print(nums)
            return nums

        init = len(nums)-2

        while init >= 0 and nums[init+1] <= nums[init]:
            init -= 1

        #print(init, nums[init], nums)
        largest = nums[init]
        end = init+1

        while end < len(nums):
            if nums[end] > largest:
                end += 1
            else:
                break

        nums[init], nums[end-1] = nums[end-1], nums[init]

        nums[init+1:] = sorted(nums[init+1:])
        retur nums


# print(Solution().nextPermutation([1, 3, 2]))

# print(Solution().nextPermutation([2, 3, 1]))


# # print("next")
# print(Solution().nextPermutation([3, 2, 1]))
# # print("next")
# print(Solution().nextPermutation([1, 1, 5]))
print(Solution().nextPermutation([2, 2, 7, 5, 4, 3, 2, 2, 1]))
