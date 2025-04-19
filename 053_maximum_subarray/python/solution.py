from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        sums = [ cur_sum := cur_sum + nums[i] for i in range(len(nums)) ]

        max_diff = float("-inf")
        for idx1 in range(-1, len(sums)):
            for idx2 in range(idx1 + 1, len(sums)):
                max_diff = max(max_diff, sums[idx2] - sums[idx1] if idx1 >= 0 else sums[idx2])
        return max_diff

print(Solution().maxSubArray([0,1,2,-10,10]))