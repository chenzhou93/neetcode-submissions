class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) < 1 or len(nums) > 100000:
            return -1

        result = 0
        res_list = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res_list.append(result)
                result = 0
            elif i == len(nums) - 1:
                result += nums[i]
                res_list.append(result)
            else:
                result += 1
        
        return max(res_list) 
