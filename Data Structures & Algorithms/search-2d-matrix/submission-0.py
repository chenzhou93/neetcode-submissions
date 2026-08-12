class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left_out = 0
        right_out = m - 1
        
        while left_out <= right_out:
            mid_out = (left_out + right_out) // 2
            #print(f'left: {left_out}, righ: {right_out}, mid: {mid_out}')
            if target < matrix[mid_out][0]:
                right_out = mid_out - 1
            elif target >= matrix[mid_out][0] and target <= matrix[mid_out][n-1]:
                left_in = 0
                right_in = n - 1
                while left_in <= right_in:
                    mid_in = (left_in + right_in) // 2
                    if matrix[mid_out][mid_in] < target:
                        left_in = mid_in + 1
                    elif matrix[mid_out][mid_in] > target:
                        right_in = mid_in - 1
                    else:
                        return True
                return False
            elif target > matrix[mid_out][n-1]:
                left_out = mid_out + 1
        
        return False


