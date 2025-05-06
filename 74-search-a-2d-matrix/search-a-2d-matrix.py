class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        row + col binary search can be applied because of this point - 
        The first integer of each row is greater than the last integer of the previous row.
        This cannot be applied if in leetcode 240
        '''
        # lets apply binary search on cols as well as rows O(log rows * logn cols)
        rows = len(matrix)
        cols = len(matrix[0])

        top, bottom = 0, rows - 1 
        while top <= bottom:
            mid_row = (top + bottom)//2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
                
            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
                
            else:
                # then target value is actually in this loop, then break and start doing bin search on that row
                break
        
        left, right = 0, cols -1
        # mid_row = (top + bottom)//2
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[mid_row][mid]:
                return True
            elif target < matrix[mid_row][mid]:
                right = mid -1
            else:
                left = mid + 1
        
        return False


        
        # lets think binary search
        rows = len(matrix)
        cols = len(matrix[0])
        
        for row in matrix:
            left, right = 0, cols-1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return False




        # brute force
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    return True
        
        return False
        