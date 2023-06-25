from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        dp={}

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff=nums[j]-nums[i]
                dp[(j,diff)]=dp.get((i,diff),1)+1


        return max(dp.values())


sol=Solution()

print(sol.longestArithSeqLength([3,6,9,12]))
