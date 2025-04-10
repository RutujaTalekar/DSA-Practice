class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        idx_tuple_set = set()
        output = []
        
        
        row, col = 0, 0
        while(len(output) != m*n):
            # traverse right
            for c in range(0, n):
                if (row, c) not in idx_tuple_set:
                    output.append(matrix[row][c])
                    idx_tuple_set.add((row,c))
                    col = c
            # print(output)
            # print("after traverse right col -", col)
            #traverse down
            for r in range(0, m):
                if (r,col) not in idx_tuple_set:
                    output.append(matrix[r][col])
                    idx_tuple_set.add((r,col))
                    row = r
            # print(output)
            # print("after traverse down row -",row)

            #traverse left
            for c in range(n-1,-1,-1):
                if (row,c) not in idx_tuple_set:
                    output.append(matrix[row][c])
                    idx_tuple_set.add((row,c))
                    col = c
            # print(output)
            # print("after traverse left col -", col) 

            #traverse up
            for r in range(m-1, -1, -1):
                if (r,col) not in idx_tuple_set:
                    output.append(matrix[r][col])
                    idx_tuple_set.add((r,col))
                    row = r
            # print(output)
            # print("after traverse up row -",row) #expect it to be 2
            
        return output