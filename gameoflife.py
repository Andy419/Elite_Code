 def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # function calculates the count around a given coord
        # and returns whether the coord survived or not
        def neighbors(i, j):
            count = 0
            
            # loop to get top row (can't be the top row)
            if i > 0:
                for k in range(max(0,j-1), min(j+2, cols)):
                    count += board[i-1][k]
            
            # loop to get bottom row (can't be the bottom row)
            if i < rows-1:
                for k in range(max(0,j-1), min(j+2, cols)):
                    count += board[i+1][k]
            
            # get the sides if they exist
            if j-1 >= 0:
                count += board[i][j-1]
            if j+1 < cols:
                count += board[i][j+1]
            
            # calculate if the given coord survives
            if board[i][j] == 1:
                if 2 <= count <= 3:
                    return 1
                else:
                    return 0
            else:
                if count == 3:
                    return 1
                else:
                    return 0
        
        rows = len(board)
        cols = len(board[0])
        ans = []
        
        # empty n*m matrix
        for _ in range(rows):
            ans.append([0]*cols)
        
        for i in range(rows):
            for j in range(cols):
                ans[i][j] = neighbors(i, j)
        
        # transfer info to original
        for i in range(rows):
            for j in range(cols):
                board[i][j] = ans[i][j]