from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maXValue = max(candies)
        return [(x+extraCandies) >= maXValue for x in candies]


print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))


print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))

print(Solution().kidsWithCandies([12, 1, 12], 10))
