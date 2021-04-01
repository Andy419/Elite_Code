    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        r = length-1
        l = 0
        total = 0
        
        # basically start at the edges and work your way in with the smaller edge being
        # replaced. Not exactly intuitive but similar in intution to bfs or equivalence
        
        while l < r:
            cur = (r-l) * min(height[l], height[r])
            total = max(total, cur)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return total