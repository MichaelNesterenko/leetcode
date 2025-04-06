from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = n_freq = (freq.get(n) or 0) + 1
            if n_freq > len(nums) // 2:
                return n


