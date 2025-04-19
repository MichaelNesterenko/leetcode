from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        seen = [False] * len(nums)
        bklg = [0]

        while bklg:
            idx = bklg.pop()
            if seen[idx]:
                continue
            seen[idx] = True
            if idx + 1 == len(nums):
                return True
            bklg += list(range(idx + 1, min(idx + 1 + nums[idx], len(nums))))
        return False

print(Solution().canJump([2,3,1,1,4]))