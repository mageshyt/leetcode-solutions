from typing import List
<<<<<<< HEAD
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
=======


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        w_s, w_e = 0, 1
        sub_count = 0
        pre_sum = nums[0]
        while w_s < len(nums):
            pass
        return sub_count


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
>>>>>>> 167b9ae (sliding window problem)
