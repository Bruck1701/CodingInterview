from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:

		maxprofit = 0 
		minbp = float('inf')
		for i,val in enumerate(prices):
			if val < minbp:
				minbp = val
			else:
				maxprofit = max(maxprofit,val-minbp)
		print(maxprofit)


sol = Solution()
stock = [7,1,5,3,6,4]
print(sol.maxProfit(stock))