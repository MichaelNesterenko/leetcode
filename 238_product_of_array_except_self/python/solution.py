from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        partial_product = 1
        for idx in range(1, len(nums)):
            partial_product *= nums[idx - 1]
            product[idx] = partial_product
        partial_product = 1
        for idx in range(len(nums) - 2, -1, -1):
            partial_product *= nums[idx + 1]
            product[idx] *= partial_product
        return product

print(Solution().productExceptSelf([1, 2, 3, 4, 5]))