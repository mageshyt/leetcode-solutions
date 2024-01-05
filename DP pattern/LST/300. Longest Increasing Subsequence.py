from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache={}

        def dp(i,prev):
            if i >= len(nums):
                return 0
            
            if (i,prev) in cache:
                return cache[(i,prev)]
            
            taken=0
            notTaken=dp(i+1,prev) # skip this number

            if nums[i] > prev:
                taken=1+dp(i+1,nums[i]) # take this number

            cache[(i,prev)]=max(taken,notTaken)

            return cache[(i,prev)]
        
        return dp(0,float('-inf'))
    
    def lengthOfLIS2(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
    
    


