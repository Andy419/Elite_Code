def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # similar problem to combinations
        # quite inefficent solution as it is extremely slow
        def combo(nums, cur):
            if sum(cur) == target:
                cur.sort()
                if cur not in already:
                    result.append(cur)
                    already.append(cur)
                
            elif sum(cur) < target:
                # iterate through every combo as long as it is lower than the target
                for i in range(len(nums)):
                    combo(nums, cur + [nums[i]])
        
        # result holds the sums
        result = []
        # already acts as a set
        already = []
        combo(candidates, [])
        return result