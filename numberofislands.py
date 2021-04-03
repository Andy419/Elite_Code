def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        ''' very similar solution to all these permuation problems
            going through each coordinate and changing them if they are
            connected
        '''
        
        def explore(i, j):
            if grid[i][j] == "1":
                grid[i][j] = "0"
                
                if i-1 > -1:
                    explore(i-1, j)
                if i+1 < rows:
                    explore(i+1, j)
                if j-1 > -1:
                    explore(i, j-1)
                if j+1 < cols:
                    explore(i, j+1)
        
        
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    explore(i, j)
                    count += 1
        
        return count