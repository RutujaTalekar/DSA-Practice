class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        island_info = []
        island_info_set = set()

        def mapDirection(island_info) -> tuple[tuple]:
            # there will always be atleast one coordinate in island_info when this method is called
            rb, cb = island_info[0]
            directions = []
            for r,c in island_info:
                rd = r - rb
                cd = c - cb
                directions.append((rd,cd))

            print(island_info, directions)

            return tuple(directions)

        def dfsExplore(r :int, c :int) -> None:
            if r < 0 or r >= rows or c < 0 or c >=cols or grid[r][c] == 0:
                return None
            
            grid[r][c] = 0
            island_info.append([r,c])

            dfsExplore(r+1, c)
            dfsExplore(r, c+1)
            dfsExplore(r-1, c)
            dfsExplore(r, c-1)
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfsExplore(r,c)
                    island_info_set.add(mapDirection(island_info))
                    island_info.clear()
        
        return len(island_info_set)











        