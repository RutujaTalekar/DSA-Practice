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
        def dfsExplore(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in visitedIsland or grid[r][c] == '0':
                return False

            visitedIsland.add((r,c))

            dfsExplore(r+1, c)
            dfsExplore(r-1, c)
            dfsExplore(r, c-1)           
            dfsExplore(r, c+1)

            return True
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visitedIsland and dfsExplore(r,c) == True:
                    res +=1
        
        return res


        