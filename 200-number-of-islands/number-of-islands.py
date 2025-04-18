class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # recursive DFS
        rows = len(grid)
        cols= len(grid[0])
        visitedIsland = set()
        res = 0

        def dfsExplore(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in visitedIsland or grid[r][c] == '0':
                return False

            visitedIsland.add((r,c))

            dfsExplore(r+1, c)
            dfsExplore(r-1, c)
            dfsExplore(r, c-1)           
            dfsExplore(r, c+1)
            
            return True
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visitedIsland and dfsExplore(r,c) == True:
                    res +=1
        
        return res

        

        #iterative BFS
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0

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

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    bfsExplore(i,j)
                    res+=1
        
        return res

        
                

        



        