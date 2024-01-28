class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0

        for i in range(1,len(s)):
            if s[i-1].lower() != s[i].lower():
                count+=1
                


        return count
    

s=Solution()
print(s.countKeyChanges("bBBb"))

from typing import List
from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=0

        cache={}
        nums.sort()
        print(nums)

        def dp(i,j,k):
            if i >= len(nums) or j >= len(nums):
                return 0
            
            if (i,j,k) in cache:
                return cache[(i,j,k)]
            
            # we can include this element or not
            res=0
            # if j in i^x 
            if pow(nums[i],k) == nums[j]:
                res=1+dp(j,j+1,k)

            res=max(res,dp(i,j+1,k))

            cache[(i,j,k)]=res

            return res



s=Solution()
print(s.maximumLength([5,4,1,2,2]))

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        if n <= 1 or m <= 1:
            return 0

        # 0 is alice, 1 is bob
        dp={}
        def dfs(n,m,turn ):
            if n <= 0 or m <= 0 and turn == "alice":
                return  True
            if (n,m,turn) in dp:
                return dp[(n,m,turn)]
            res=False

            if turn == "alice":
                res= dfs(n-1,m,"bob") or dfs(n,m-1,"bob")
            else:
                res=dfs(n-1,m,"alice") and dfs(n,m-1,"alice")

            dp[(n,m,turn)]=res
            return res

        
        dfs(n,m-1,"bob")
        # now count the number of true for alice
        count=0
        for key in dp:
            if dp[key] == True and key[2] == "alice":
                count+=1

        return count

s=Solution()
print(s.flowerGame(4,4))


class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Initialize dp array to store the minimum bitwise OR after i operations
        dp = [[0] * (k + 1) for _ in range(n)]
        
        # Initialize dp array with the bitwise OR of all elements
        for i in range(n):
            dp[i][0] = nums[i]
        
        # Iterate over operations
        for op in range(1, k + 1):
            for i in range(n - 1):
                # Calculate the AND operation
                # print(dp[i][op-1],dp[i+1][op-1])
                dp[i][op] = dp[i][op-1] | dp[i + 1] [op-1]
        
        # Return the minimum bitwise OR after k operations
                

        return dp[0][k]


s=Solution()
print(s.minOrAfterOperations([10,7,10,3,9,14,9,4],1))