def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ''' Classic compare dictionary solution. One is the
            target (static dictionary) and one is a travelling
            dictionary that adds and removes as it sections
        '''
        
        lp = len(p)
        l = len(s)
        
        # edge case
        if lp > l:
            return []
        
        # Create dictionary of p
        pset = dict()
        for let in p:
            if let not in pset:
                pset[let] = 1
            else:
                pset[let] += 1
        
        # initiate travelling dictionary
        tdict = dict()
        for i in range(lp):
            if s[i] not in tdict:
                tdict[s[i]] = 1
            else:
                tdict[s[i]] += 1
        
        # anagrams index storage
        ana = []
        
        for i in range(l-lp+1):
            # compare
            if tdict == pset:
                ana.append(i)
            
            # adjust dict for next run
            tdict[s[i]] -= 1
            if tdict[s[i]] == 0:
                tdict.pop(s[i])
            if i != l-lp:
                if s[i+lp] not in tdict:
                    tdict[s[i+lp]] = 1
                else:
                    tdict[s[i+lp]] += 1
        
        return ana