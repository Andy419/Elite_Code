def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ''' ok solution, basically just store the coords on a stack
            and go through each coord and change the sections to 0
            
            *** Optimized a little by adding sets to not over write
            rows and cols that are already zeros ***
        '''
        
        stack = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    stack.append([i,j])
        
        rowalready = set()
        colalready = set()
        
        while stack:
            cur = stack.pop()
            row = cur[0]
            col = cur[1]
            
            if row not in rowalready:
                for i in range(cols):
                    matrix[row][i] = 0
                
                rowalready.add(row)
            
            if col not in colalready:
                if row > 0:
                    for i in range(row-1, -1, -1):
                        matrix[i][col] = 0

                if row < rows-1:
                    for i in range(row+1, rows):
                        matrix[i][col] = 0
                
                colalready.add(col)
        
        return matrix