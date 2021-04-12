    def constructArray(self, n: int, k: int) -> List[int]:
        ''' Quite Tricky. basically a switch algorithm 
            until k is 0
        '''
        
        
        
        ans = []
        left = 1
        flag = True
        while k != 0:
            if flag:
                ans.append(n)
                n -= 1
            else:
                ans.append(left)
                left += 1
            k -= 1
            flag = not flag
        
        if flag:
            for i in range(left, n+1):
                ans.append(i)
        else:
            for i in range(n, left-1, -1):
                ans.append(i)

        return ans