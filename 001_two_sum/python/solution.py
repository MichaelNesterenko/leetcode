class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}
        for idx, i in enumerate(nums):
            if target - i in seen:
                return [idx, seen[target - i]]
            else:
                seen[i] = idx

print(Solution().twoSum([1, 2 ,3], 5))