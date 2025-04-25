class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def addSides(row,col) -> int:
            sides = 0
            if row+1 >= rows or grid[row+1][col] == 0:
                sides +=1
            if row-1 < 0 or grid[row-1][col] == 0:
                sides += 1
            if col+1 >= cols or grid[row][col+1] == 0:
                sides +=1
            if col-1 < 0 or grid[row][col-1] == 0 :
                sides += 1
            return sides

            

        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += addSides(i,j)
        
        return perimeter





        