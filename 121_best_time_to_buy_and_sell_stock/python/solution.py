from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v = prices[0]
        profit = 0
        for v in prices:
            if v < min_v:
                min_v = v
            else:
                profit = max(profit, v - min_v)
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))