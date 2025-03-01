class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i, p1 = 0, 0

        while i < len(nums)-1:
            if nums[i] != 0:
                if nums[i] == nums[i+1]:
                    res[p1] = nums[i]*2
                    i += 1
                else:
                    res[p1] = nums[i]
                p1 += 1
            i += 1

        if i < len(nums) and nums[i] != 0:
            res[p1] = nums[i]

        return res
