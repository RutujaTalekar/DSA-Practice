class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # lets think binary search
        rows = len(matrix)
        cols = len(matrix[0])
        
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

        