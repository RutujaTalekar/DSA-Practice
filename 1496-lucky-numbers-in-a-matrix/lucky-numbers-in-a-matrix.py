class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

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
        return res
        