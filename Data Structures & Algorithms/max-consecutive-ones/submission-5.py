class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 1 or len(nums) > 100000:
            return -1

        result = 0
        max_res = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if max_res < result:
                    max_res = result
                result = 0
            else:
                result += 1
                
        return max(result, max_res) 
