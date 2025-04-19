from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(start_idx: int, end_idx: int) -> None:
            if start_idx >= end_idx:
                return
            s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
            reverse(start_idx + 1, end_idx - 1)
        reverse(0, len(s) - 1)

Solution().reverseString(["h", "e", "l", "l", "o"])
