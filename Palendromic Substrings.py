class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # each individual letter is its own palindrome
        count = len(s)
        
        # iterate with a bracket
        for i in range(2,len(s)+1):
            for j in range(len(s)-i+1):
                # set the current with the bracket
                cur = s[j:i+j]
                
                if cur == cur[::-1]:
                    count += 1
        
        return count