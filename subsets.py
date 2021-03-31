 def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # slow and needs to be refined later with more knowledge
        # basic permutations problem but slow
        def sec(nums, cur):
            cur.sort()
            if cur not in ans:
                ans.append(cur)
                for i in range(len(nums)):
                    sec(nums[:i] + nums[i+1:], cur + [nums[i]])

        ans = []
        sec(nums, [])
        
        return ans
        