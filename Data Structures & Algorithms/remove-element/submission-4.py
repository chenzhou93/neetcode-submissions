class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left] = nums[right]
                nums[right] = val
                left += 1
                right -= 1
            else:
                left += 1
        print(nums)
        k = -1
        for i in range(len(nums)):
            if nums[i] == val:
                k = i
                return k

        return len(nums)

        