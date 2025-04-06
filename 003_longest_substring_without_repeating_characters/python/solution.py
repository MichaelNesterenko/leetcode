class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        max_length = 0
        min_idx = 0

        for idx, chr in enumerate(s):
            if chr in seen_chars:
                min_idx = max(min_idx, seen_chars[chr] + 1)
            seen_chars[chr] = idx
            max_length = max(max_length, idx - min_idx + 1)

        return max_length

print(Solution().lengthOfLongestSubstring("abba"))