from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        skip = 0
        for idx in range(len(nums)):
            if nums[idx] == val:
                skip += 1
            else:
                nums[idx - skip] = nums[idx]
        return len(nums) - skip

print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
