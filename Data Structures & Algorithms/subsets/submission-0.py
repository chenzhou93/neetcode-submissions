class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        res = []
        path = []
        
        res1 = self.backTrack(0, nums, path, True, res)
        res.append(res1.copy())
        path.pop()
        res2 = self.backTrack(0, nums, path, False, res)
        res.append([])

        return res
    
    def backTrack(self, i, nums, path_list, add: bool, res):
        n = len(nums)

        if add:
            path_list.append(nums[i])
        
        if i == n - 1: #last element, the "leaf"
            return path_list
        
        res1 = self.backTrack(i+1, nums, path_list, True, res)
        res.append(res1.copy())
        #print('res1', res1)
        
        path_list.pop()
        
        res2 = self.backTrack(i+1, nums, path_list, False, res)
        # res.append(res2.copy())
        # print('res2', res2)

        #print('path list to return', path_list)

        return path_list
        
        

