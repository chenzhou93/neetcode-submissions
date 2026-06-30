class Solution:
    def feb(self, n: int) -> int:
        if n < 0:
            return 0

        if n == 0:
            return 1

        return self.feb(n-1) + self.feb(n-2)

    def climbStairs(self, n: int) -> int:
        return self.feb(n)
        