class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        We could use BFS to solve this, as we are looking at adjacent cells
        and essentially counting how many loops (mins) it would take to cover all cells
        '''
        rows = len(grid)
        cols = len(grid[0])

        # first check which all cells have rotten oranges to start BFS on
        q = deque()
        fresh_orange = 0

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh_orange += 1
        
        # edge case
        # if there are no fresh oranges but rotten oranges are present then we did it 0 minutes!
        if fresh_orange == 0:
            return 0
        
        
        # now start BFS
        
        minutes = -1
        
        while q:
            minutes += 1
            
            for _ in range(len(q)):
                r,c = q.popleft()
                
                if r+1 < rows and r+1 >= 0 and c < cols and c >= 0 and grid[r+1][c] == 1:
                    q.append((r+1, c))
                    fresh_orange -= 1
                    grid[r+1][c] = 2

                if r < rows and r >= 0 and c+1 < cols and c+1 >= 0 and grid[r][c+1] == 1:
                    q.append((r,c+1))
                    fresh_orange -= 1
                    grid[r][c+1] = 2

                if r < rows and r >= 0 and c-1 < cols and c-1 >= 0 and grid[r][c-1] == 1:
                    q.append((r, c-1))
                    fresh_orange -= 1
                    grid[r][c-1] = 2

                if r-1 < rows and r-1 >= 0 and c < cols and c >= 0 and grid[r-1][c] == 1:
                    q.append((r-1, c))
                    fresh_orange -= 1
                    grid[r-1][c] = 2
                    
            
        
        if fresh_orange != 0:
            return -1

        return minutes


                    
                    





