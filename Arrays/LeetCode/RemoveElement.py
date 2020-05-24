class Solution:

    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        # print(nums)
        return len(nums)


if __name__ == "__main__":
    print(Solution().removeElement([3, 2, 2, 3], 3))
