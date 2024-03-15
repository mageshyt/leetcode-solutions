from typing import List
class Solution:
    # Time : O(n) Space: O(1)
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(goal):

            if goal < 0:
                return 0
            
            res=0
            left,curr=0,0

            for r in range(len(nums)):
                curr+=nums[r]
                while curr > goal:
                    curr-=nums[left]
                    left+=1
                # add size of subarray
                res+=r-left+1
            return res


        return helper(goal)-helper(goal-1)

    

sol=Solution()
print(sol.numSubarraysWithSum([0,0,0,0,0],0))