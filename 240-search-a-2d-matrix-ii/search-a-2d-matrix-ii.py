class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])
        '''
        lets do staircase approach, start from top right, go left if target is less that cur value
        go down if target is greater that cur value
        In the worst case, you move at most rows + cols steps. O(m + n)
        Optimal approach
        '''
        
        row, col = 0, cols-1

        while row < rows and col >= 0:
            current = matrix[row][col]
            if target == current:
                return True
            elif target < current:
                col = col -1
            elif target > current:
                row = row + 1
        return False
            
        
        '''
        lets think binary search, only applied to each row. skip the rows that are not the correct range for target
        In the worst case, you scan all m rows.
        For each eligible row, you do binary search → O(log n).
        So worst case it is O(m logn)
        Slightly better way if m << n (few rows, many columns)
        '''

        for row in matrix:
            if not (target >= row[0] and target <= row[-1]):
                continue

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

        