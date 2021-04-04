def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # take dict and create a set for O(1) look up
        words = set()
        for word in wordDict:
            if word not in words:
                words.add(word)
        
        # starts holds all the words that fit and where they end
        # we iterate over to see if we reach a new high
        # at the end if our high reaches the len(s), success
        
        starts = [0]
        for i in range(len(s)):
            # print(starts)
            for j in starts:
                if s[j:i+1] in words:
                    starts.append(i+1)
                    break
        
        return starts[-1] == len(s)
                