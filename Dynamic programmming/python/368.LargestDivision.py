
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # sort the nums
        nums.sort()
        cache={}
        n=len(nums)
        
        # helper function

        def dfs(i:int):
            if i == n:
                return [ ]
            if i in cache:
                return cache[i]

            res=[nums[i]]

            for j in range(i+1,n):
                if nums[j] % nums[i] ==0:
                    temp=[nums[i]]+dfs(j)

                    if len(temp) > len(res):
                        res=temp

            cache[i]=res

            return cache[i]


        res=[]
        for i in range(n):
            temp=dfs(i)
            if len(temp) > len(res):
                res=temp
        return res

print(Solution().largestDivisibleSubset([1,2,3]))
