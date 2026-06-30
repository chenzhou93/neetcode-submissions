class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        total = 0
        first = 1
        second = 2
        for i in range(n):
            total = first + second
            first = second
            second = total
        print(total)
        return total

        