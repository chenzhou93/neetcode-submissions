class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = n = len(nums) - 1
        left = 0

        while left <= right:
            mid = (left + right) // 2
            # print('left', left)
            # print('right', right)
            # print('mid', mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1


