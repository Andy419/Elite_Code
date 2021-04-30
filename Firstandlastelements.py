def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if nums == []:
            return [-1, -1]
        
        ls = l = 0
        rs = r = len(nums) - 1
        
        while l != r:
            mid = l + (r-l)//2
            
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        if nums[l] != target:
            return [-1, -1]
        
        while l != rs:
            mid = 1+ l + (rs-l)//2
            
            if nums[mid] == target:
                l = mid
            
            else:
                rs = mid - 1
        
        return [r, rs]