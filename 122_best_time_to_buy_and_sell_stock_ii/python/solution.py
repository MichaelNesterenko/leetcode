from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prev_price = float("-inf")
        for price in prices:
            if price < prev_price:
                if buy_price >= 0:
                    profit += prev_price - buy_price
                    buy_price = -1
            elif price > prev_price:
                if buy_price < 0:
                    buy_price = prev_price
            prev_price = price
        if buy_price >= 0 and prev_price > buy_price:
            profit += prev_price - buy_price
        return profit

print(Solution().maxProfit([1,2]))