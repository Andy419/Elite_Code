    def findWords(self, words: List[str]) -> List[str]:
        ''' sets and iterate through sets
        '''
        
        every = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
        ans = []
        
        for word in words:
            l = len(word)
            for sett in every:
                count = 0
                
                for let in word:
                    if let.lower() in sett:
                        count += 1
                
                if count == l:
                    ans.append(word)
        
        return ans