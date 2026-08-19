import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)

        left = 1
        right = n
        res = 0

        while left <= right:
            mid = (left + right) // 2
            total_hours = 0
            for num in piles:
                total_hours += (math.ceil(num / mid))
            
            if total_hours <= h:
                res = mid
                right = mid - 1
            elif total_hours > h:
                left = mid + 1
        
        return res


        