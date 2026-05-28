class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return
        
        n = head = len(nums)
        ans = [0] * (n * 2)

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[head] = nums[i]
            head += 1
        
        return ans


        