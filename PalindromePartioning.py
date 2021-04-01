def partition(self, s: str) -> List[List[str]]:
        
        # this one's a similar permutations problem but a little tuff
        # code speaks for itself, if you can think in recursion a little 
        
        def part(s, cur):
            if s == "":
                result.append(cur)
            else:
                for i in range(1, len(s)+1):
                    if s[0:i] == s[0:i][::-1]:
                        part(s[i:], cur + [s[0:i]])
        result = []
        part(s, [])
        return result