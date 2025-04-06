from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        skip = 0
        matched = 1
        prev = nums[0]
        for idx in range(1, len(nums)):
            nums[idx - skip] = nums[idx]
            if nums[idx] == prev:
                matched += 1
                if matched > 2:
                    skip += 1
            else:
                matched = 1
            prev = nums[idx]
        return len(nums) - skip

print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))