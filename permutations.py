    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return nums

        # cheek solution as it calls another function

        def pars(nums, act):
            if nums == []:
                result.append(act)
            for i in range(len(nums)):
                pars(nums[0:i] + nums[i + 1:], act + [nums[i]])

        result = []
        pars(nums, [])
        return result