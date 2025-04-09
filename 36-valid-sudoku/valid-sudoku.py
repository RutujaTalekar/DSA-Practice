class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # always iterate withing 0-3, 3-6, 6-9 indices for col and rows

        # The cell is valid if -
            # its not empty
            # its value is between 1-9
            # no repeat values for 3X3 box
        
        
        valid_nums = {'1','2','3','4','5','6','7','8','9'}
        rowMap = {k:set() for k in range(0,9)}
        colMap = {k:set() for k in range(0,9)}        

        def validBox(rs, cs):
            box = set()
            for r in range(rs, rs+3):
                for c in range(cs, cs+3):
                    cur = board[r][c]
                    if cur in valid_nums:
                        if cur in box or cur in rowMap[r] or cur in colMap[c]:
                            return False
                        box.add(cur)
                        rowMap[r].add(cur)
                        colMap[c].add(cur)
           
            return True

        # row col bounds before [0,3], [3, 6], [6,9]
        # row start values [0,3,6] for each iterate in col start values [0,3,6]

        for rs in range(0,9,3):
            for cs in range(0,9,3):
                result = validBox(rs, cs)
                if result == False:
                    return False  
        
        return True

        '''
        # cleaner solution -
        row = defaultdict(list)
        col = defaultdict(list)
        sq = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row[i] 
                or board[i][j] in col[j] 
                or board[i][j] in sq[(i//3, j//3)]):
                    return False
                
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                sq[(i//3, j//3)].append(board[i][j])

        return True
        '''
            
        


                
        

        
        


        