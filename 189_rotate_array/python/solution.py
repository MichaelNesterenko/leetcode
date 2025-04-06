from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        N = len(nums)
        idx = -1
        while N > 0:
            idx += 1
            start_idx = idx
            next_number = nums[idx]
            while True:
                idx = (idx + k) % len(nums)
                next_number, nums[idx] = nums[idx], next_number

                N -= 1
                if start_idx == idx:
                    break
            

Solution().rotate([-1,-100,3,99], 2)