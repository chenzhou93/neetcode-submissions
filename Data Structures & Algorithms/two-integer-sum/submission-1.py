class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m_index = {}
        res = []

        for i in range(len(nums)):
            m_index[target - nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in m_index:
                j = m_index[nums[i]]
                if j < i:
                    tmp = i
                    i = j
                    j = tmp
                
                if j != i:
                    res.append(i)
                    res.append(j)
                    break
        
        return res
        