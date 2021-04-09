def matrixScore(self, A: List[List[int]]) -> int:
        ''' Bascially make the biggest binary number possible
        '''
        
        
        
        rows = len(A)
        cols = len(A[0])
        
        # start by making most significant digit 1
        for i in range(rows):
            if A[i][0] == 0:
                for j in range(cols):
                    A[i][j] = 1 - A[i][j]
        
        # add the most significant digits to the count
        count = (2**(cols-1)) * rows
        
        
        # next swap the cols to make most 1's as possible
        for i in range(1, cols):
            total = 0
            for j in range(rows):
                total += A[j][i]
            
            if total > rows//2:
                count += (2**(cols-i-1)) * total
            else:
                count += (2**(cols-i-1)) * (rows-total)
            
        
        return count