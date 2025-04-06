from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = -200
        skip = 0
        for idx in range(len(nums)):
            if nums[idx] == prev:
                skip += 1
            else:
                nums[idx - skip] = nums[idx]
            prev = nums[idx]
        return len(nums) - skip
