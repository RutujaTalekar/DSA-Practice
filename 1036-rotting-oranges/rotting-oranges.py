class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        We could use BFS to solve this, as we are looking at adjacent cells
        and essentially counting how many loops (mins) it would take to cover all cells
        '''

        # Before we can start BFS, we have to find which cells can initiate BFS i.e. which cells are rotten - append in queue
        # Another thing to keep track of is, how many fresh oranges do we have?
        # This counter will help us to return -1 if rotten oranges could not reach all of the fresh oranges

        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        # edge case - if there are no fresh oranges then we can return 0, cause it took us 0 mins to reach to that state
        if fresh == 0:
            return time
        
        # lets starts the BFS, and keep it going untill we have nothing in queue or fresh oranges are covered
        while q and fresh > 0:
            for _ in range(len(q)):     # range function takes snap shot of length at that time, and does level by level traversal
                i, j = q.popleft()
                for dr, dc in directions:
                    r = i + dr
                    c = j + dc
                    if r < rows and r >= 0 and c < cols and c >= 0 and grid[r][c] == 1:
                        fresh -= 1
                        q.append((r,c))
                        grid[r][c] = 2
            time += 1
        
        return time if fresh == 0 else -1


                
