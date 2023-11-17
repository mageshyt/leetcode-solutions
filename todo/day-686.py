class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        result=0
        while left <=right:
            result=max(result,nums[left]+nums[right])
            left+=1
            right-=1

        return result
