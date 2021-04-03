    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # basic Sudoku set up, sets for rows, cols and squares
        # Does not account for diagonals
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                
                num = board[i][j]
                x = i//3
                y = j//3
                
                if (num in rows[i]) or (num in cols[j]) or (num in squares[x][y]):
                    return False
                else:
                    rows[i].add(num)
                    cols[j].add(num)
                    squares[x][y].add(num)
        
        return True