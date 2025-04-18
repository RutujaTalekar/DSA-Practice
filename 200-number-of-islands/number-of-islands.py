
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        # helper dfs function
        def dfs(i,j):
            # check for edge conditions
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return
            # assign the island cell as 0 to represent visisted island
            grid[i][j] = '0'
            
            # check the children nodes, i.e check in each direction for continuous islands
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        # output num of islands 
        numIslands = 0
        
        # start with the root node (0,0)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' :
                    dfs(row,col)
                    numIslands += 1
        
        return numIslands

'''
# BFS SOLUTION
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        # helper function to check bounds, check water/'0' and already visitd land
        def is_island(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0'  or (i,j) in visited:
                return
            visited.add((i,j))
            q.append((i,j))

        # to store the num of islands
        num_islands = 0

        # iterate over each cell in the grid to check if its island
        # if it is island then check if we have already discovered it
        # if not discovered add it to our q and then check for contiguous land by running BFS starting from that root
        # repeat
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    num_islands +=1
                    q.append((i,j))
                    visited.add((i,j))
                    while (q):
                        r,c = q.popleft()
                        is_island(r+1,c)
                        is_island(r-1,c)
                        is_island(r,c+1)
                        is_island(r,c-1)
        
        return num_islands
'''
                    
        