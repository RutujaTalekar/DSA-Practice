class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        #iterative BFS
        def bfsExplore(r,c):


            q = deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                if (r,c) not in visited and r < rows and c < cols and r >= 0 and c >=0 and grid[r][c] == '1':
                    grid[r][c] = '0'
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c+1))
                    q.append((r,c-1))
            
            return True
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfsExplore(i,j)
                    res+=1
        
        return res
                

        



        