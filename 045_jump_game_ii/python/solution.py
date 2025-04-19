from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [float("inf")] * len(nums)
        jumps[-1] = 0
    
        for idx in range(len(nums) - 2, -1, -1):
            min_jumps = float("inf")
            for prev_jump_jdx in range(idx + 1, min(len(nums), idx + nums[idx] + 1)):
                min_jumps = min(min_jumps, jumps[prev_jump_jdx])
            jumps[idx] = min_jumps + 1

        return jumps[0]

print(Solution().jump([2,3,1,1,4])) 