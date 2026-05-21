class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return
        
        n = len(arr)
        tmp_max = old_max = arr[n-1]

        for i in range(n-1, -1, -1):
            if arr[i] > tmp_max:
                old_max = tmp_max
                tmp_max = arr[i]
                arr[i] = old_max
            else:
                arr[i] = tmp_max
            
        arr[-1] = -1
        return arr

            
