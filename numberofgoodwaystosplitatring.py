def numSplits(self, s: str) -> int:
        '''
        Simple dictionary and set
        '''
        
        
        left = dict()
        lcount = 0
        for let in s:
            if let not in left:
                left[let] = 1
                lcount += 1
            else:
                left[let] += 1
        
        right = set()
        
        good = 0
        rcount = 0
        for i in range(len(s)-1):
            let = s[i]
            if let not in right:
                right.add(let)
                rcount += 1
            
            left[let] -= 1
            if left[let] == 0:
                lcount -= 1
            
            if rcount == lcount:
                good += 1
                         
        
        return good