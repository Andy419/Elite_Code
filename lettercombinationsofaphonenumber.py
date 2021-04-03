def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ''' Another very similar permutations problem
            a little tricky but the logic is pretty clear
            if you understand permutations problems
        '''
        
        phonebook = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        
        def combos(comb, cur):
            if comb == "":
                result.append(cur)
            else:
                num = comb[0]
                now = phonebook[int(num)]
                for i in range(len(now)):
                    combos(comb[1:], cur + now[i])
                    
                    
            
        result = []
        combos(digits, "")
        return result