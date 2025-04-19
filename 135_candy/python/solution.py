from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        total_candies = 0
        prev_candies = prev_rate = float("-inf")
        prev_max_rate_idx = 0
        overflow_candies = candies_to_add = 0
        
        for idx in range(len(ratings)):
            if ratings[idx] > prev_rate:
                candies_to_add += 1
            else:
                candies_to_add = 1

            if ratings[idx] >= prev_rate:
                prev_max_rate_idx = idx
                overflow_candies = candies_to_add - 2

            if ratings[idx] < prev_rate:
                if prev_candies <= candies_to_add:
                    total_candies += idx - prev_max_rate_idx - (1 if overflow_candies > 0 else 0)
                    overflow_candies -= 1
            total_candies += candies_to_add
            
            prev_candies = candies_to_add
            prev_rate = ratings[idx]

        return total_candies

print(Solution().candy([29,51,87,87,72,12]))