import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n = len(nums)
        q = n - k
        for i in range(q):
            heapq.heappop(nums)
        
        print(nums[0])

        return nums[0]