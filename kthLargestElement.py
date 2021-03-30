def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # load dictionary and list
        sec = {}
        alnums = []
        for num in nums:
            if num not in sec:
                alnums.append(num)
                sec[num] = 1
            else:
                sec[num] += 1
        
        # sort list O(nlog(n))
        alnums.sort()
        cur = alnums[-1]
        count = 1
        
        # find k largest
        while k != 1:
            sec[cur] -= 1
            if sec[cur] == 0:
                count += 1
                cur = alnums[-count]
            k -= 1
        return cur
            