class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        tmp_sum = 0
        self.comboSum(0, nums, path, res, tmp_sum, target)
        return res
    
    def comboSum(self, i, nums, path, res, tmp_sum, target):
        n = len(nums)

        if i == n:
            return
        
        if tmp_sum > target:
            return
        
        if tmp_sum == target:
            res.append(path.copy())
            return
        
        tmpVal = nums[i]
        tmp_sum += tmpVal
        path.append(nums[i])
        self.comboSum(i, nums, path, res, tmp_sum, target)
        
        path.pop()
        tmp_sum -= tmpVal

        self.comboSum(i+1, nums, path, res, tmp_sum, target)

        

