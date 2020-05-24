'''
Two Sum problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
This problem is similar to the Ice cream problem from Hackerrank. What you store in the hashmap is the difference from a specific target 
but you check the current number of the array it is in the hashmap.
'''


class Solution:
    def twoSum(self, nums, target):

        hashmap = {}

        for idx in range(len(nums)):
            el = nums[idx]

            comp = target-el

            if el not in hashmap:
                hashmap[comp] = idx
            else:
                return [hashmap[el], idx]


print(Solution().twoSum([2, 7, 11, 15], 9))


'''
    first solution: 552 ms

        hashmapV = {}
        hashmapK = {}
        for index in range(len(nums)):
            hashmapV[index] = nums[index]
            hashmapK[nums[index]] = index
            complement = target - nums[index]
            if complement in hashmapV.values() and hashmapK[complement] != index:
                return [index, hashmapK[complement]]

        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in hashmapV.values() and hashmapK[complement] != index:
                return [index, hashmapK[complement]]

'''
