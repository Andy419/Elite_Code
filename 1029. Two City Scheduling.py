class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        # Faster nlog(n) sol.
        
        # idea is that we take the smallest relative difference between the two options.
        
        # What the fuck does 'realative difference' mean??? Take the example [[4, 400], [4,5]]
        
        # i.e. it is better to take A on [4, 400] vs [4, 5] clearly
        
        # we can represent this array as A-B or [(4-400), (4-5)] == [-395, -1]. 
        
        # Sort the array and the most negative numbers will go to A and the most postive will go to B
        
        # This is practically impossible to come up with in an interview but suck it up.
        
        costs.sort(key = lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        
        res = 0
        for i in range(n):
            res += costs[i][0]
        
        for i in range(n, len(costs)):
            res += costs[i][1]
            
        
        return res
        
        

        # Brute Force (Too Slow) 2^n -ish
#         def dfs(personIdx, curCost, Aleft, Bleft):
#             if curCost > self.mincost:
#                 return
            
#             if personIdx == len(costs):
#                 self.mincost = min(self.mincost, curCost)
#                 return
            
#             if Aleft > 0:
#                 dfs(personIdx + 1, curCost + costs[personIdx][0], Aleft-1, Bleft)
            
#             if Bleft > 0:
#                 dfs(personIdx + 1, curCost + costs[personIdx][1], Aleft, Bleft - 1)
        
#         n = len(costs) // 2
#         self.mincost = 1000 * (len(costs) + 1)
        
#         dfs(0, 0, n, n)
        
#         return self.mincost