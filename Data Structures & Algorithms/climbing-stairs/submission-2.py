class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        total = 0
        first = 1
        second = 2
        for i in range(n-2):
            total = first + second
            first = second
            second = total
        
        return total

        