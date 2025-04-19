from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)
        for idx in range(len(sorted_citations) + 1):
            if idx == len(sorted_citations) or idx + 1 > sorted_citations[idx]:
                return idx
        return 0

print(Solution().hIndex([3, 0, 6, 1, 5]))  # Output: 3