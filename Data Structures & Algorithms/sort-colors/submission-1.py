class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [1,0,1,2]
        stat = [0] * 3 # stat = [0, 1, 2]

        for num in nums:
            stat[num] += 1 # stat[1] += 1; stat[0] += 1; stat[1] += 1; stat[2] += 1
        
        i = 0
        for k in range(len(stat)): # range(4) k = 0, 1, 2
            cnt = stat[k] # stat[0] = 1
            for j in range(cnt): # j in range(1)
                nums[i] = k # nums[0] = 0
                i += 1
            
        