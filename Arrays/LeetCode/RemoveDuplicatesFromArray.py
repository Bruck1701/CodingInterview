class Solution:
    def removeDuplicates(self, nums):
        # hashmap = {}

        # # for idx in range(len(nums)):
        # idx = 0
        # while idx < len(nums):
        #     changeidx = True
        #     print(idx, nums[idx])
        #     if nums[idx] in hashmap:
        #         nums.pop(idx)          # pop(k) has O(K) so this solution is O(N^2)
        #         changeidx = False
        #     else:
        #         hashmap[nums[idx]] = True

        #     if changeidx:
        #         idx += 1

        # an O(N) solution needs two pointers i keeps on moving forwards, and edited only advances when it finds a different number.

        if not nums or len(nums) == 1:
            return len(nums)

        i = 1
        edited = 1

        while i < len(nums):
            if nums[i-1] != nums[i]:
                nums[edited] = nums[i]
                edited += 1
            i += 1

        # return edited

        print(nums[0:edited])


Solution().removeDuplicates([1, 1, 2])
Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
#
