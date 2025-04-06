from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        current_idx = idx1 = idx2 = 0
        median_idx = (len(nums1) + len(nums2) - 1) // 2
        limit_idx = median_idx + (1 if (len(nums1) + len(nums2)) % 2 == 0 else 0)
        last_nums = [0, 0]

        while current_idx <= limit_idx:
            while current_idx <= limit_idx and idx1 < len(nums1) and (idx2 >= len(nums2) or nums1[idx1] <= nums2[idx2]):
                last_nums[current_idx % len(last_nums)] = nums1[idx1]
                idx1 += 1
                current_idx += 1
            while current_idx <= limit_idx and idx2 < len(nums2) and (idx1 >= len(nums1) or nums2[idx2] <= nums1[idx1]):
                last_nums[current_idx % len(last_nums)] = nums2[idx2]
                idx2 += 1
                current_idx += 1

        return (last_nums[median_idx % len(last_nums)] + last_nums[limit_idx % len(last_nums)]) / 2

print(Solution().findMedianSortedArrays([1,3], [2]))
            