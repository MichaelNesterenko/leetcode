class Solution:
    def climbStairs(self, n: int) -> int:
        n2 = n1 = 1
        for _ in range(1, n):
            n2, n1 = n1, n1 + n2
        return n1
print(Solution().climbStairs(3))