class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        
        # O(nm) time, O(n+m) space
        '''
        rows, cols = len(matrix), len(matrix[0])
        lucky_row = [math.inf] * rows
        lucky_col = [-math.inf] * cols

        res = []

        for i in range(rows):
            for j in range(cols):
                lucky_row[i] = min(lucky_row[i], matrix[i][j])
        
        for i in range(cols):
            for j in range(rows):
                lucky_col[i] = max(lucky_col[i], matrix[j][i])

        if max(lucky_row) == min(lucky_col):
            return [max(lucky_row)]
        else:
            return []
        '''

        # Slightly faster, O(nm) time, O(1) space
        res = []
        for i in range(len(matrix)):
            min_val = matrix[i][0]
            min_col = 0
            for j in range(1, len(matrix[0])):
                val = matrix[i][j]
                if val < min_val:
                    min_val = val
                    min_col = j
            for k in range(len(matrix)):
                if matrix[k][min_col] > min_val:
                    break
            else:
                res.append(min_val)
                break
        return res
        


        